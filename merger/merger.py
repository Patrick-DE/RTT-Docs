import traceback
import requests
import sys
import json
import os
from fetchAllGitData import fetchAllGitData
from tools import ToolSchema
from techniques import TechniqueSchema
from jsonschema import validate
from dotenv import load_dotenv

load_dotenv("..\.env")
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

merged_issues = []
tools_file = "dist/tools.json"
techniques_file = "dist/techniques.json"

headers = {"Accept": "application/vnd.github+json", "Authorization": "Bearer "+GITHUB_API_KEY, "X-GitHub-Api-Version": "2022-11-28"}
r = requests.get('https://api.github.com/repos/Patrick-DE/RTT-Docs/issues', headers=headers)
issues = r.json()
if "message" in issues:
    print("[-] Error: " + issues["message"])
    sys.exit(-1)

print("[+] Found " + str(len(issues)) + " issues.")

# read base files
with open(tools_file, 'r') as f:
    toolBase = json.load(f)
with open(techniques_file, 'r') as f:
    techniqueBase = json.load(f)

for issue in issues:
    if not any(label["name"] == 'reviewed' for label in issue["labels"]) and issue['author_association'] != 'OWNER':
        continue

    if "New tool:" in issue["title"]:
        typ = ToolSchema
        base = toolBase
        print("[+] Loading tool json for " + issue["title"])
        
    elif "New technique:" in issue["title"]:
        typ = TechniqueSchema
        base = techniqueBase
        print("[+] Loading technique json for \"" + issue["title"] + "\"")

    else:
        continue

    # Load JSON from issue
    try:
        body = json.loads(issue["body"][3:-3])
    except Exception as ex:
        last_line = traceback.format_exc().strip().splitlines()[-1]
        print(last_line)
        continue
    
    # Validation of JSON
    print("  [+] Validating json...")
    try:
        validate(body, schema=typ)
    except Exception as ex:
        print("  [-]: " + issue["title"] + " is not a valid serialized json!\n" + ex.message)
        continue
    
    count = 0
    for elem in base:
        if typ == ToolSchema:
            if elem["name"] == body["name"]:
                break
        elif typ == TechniqueSchema:
            if elem["id"] == body["id"]:
                break
        count+=1
    
    if count < len(base):
        print("  [+] Merging existing entry")
        base[count] = body
    else:
        print("  [+] Adding new entry")
        base.append(body)

    if typ == ToolSchema:
        f = open(tools_file, 'w')
    elif typ == TechniqueSchema:
        f = open(techniques_file, 'w')

    f.write(json.dumps(base, indent=4))
    f.close

    merged_issues.append(issue)

print("\n\nFetching latest commits for git sources...")
fetchAllGitData(tools_file)

print ("Commit message:")
for iss in merged_issues:
    print ("close #" + str(iss["number"]),end=', ')
