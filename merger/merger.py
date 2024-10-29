import traceback
import requests
import sys
import json
import os
from fetchAllGitData import fetchAllGitData
from dotenv import load_dotenv
from validator import custom_validate

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
with open(tools_file, 'r', encoding="UTF-8") as f:
    toolBase = json.load(f)
with open(techniques_file, 'r', encoding="UTF-8") as f:
    techniqueBase = json.load(f)

for issue in issues:
    if not any(label["name"] == 'reviewed' for label in issue["labels"]) and issue['author_association'] != 'OWNER':
        continue

    # Check if issue is a tool or technique
    if "New tool:" in issue["title"]:
        typ = "tool"
        base = toolBase
        print("[+] Loading tool json for " + issue["title"])
        
    elif "New technique:" in issue["title"]:
        typ = "technique"
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
        custom_validate(body, typ)
    except Exception as ex:
        print("  [-]: " + issue["title"] + " is not a valid serialized json!\n" + ex.message)
        continue
    
    # Check if entry already exists
    count = 0
    for elem in base:
        if typ == "tool":
            if elem["name"] == body["name"]:
                break
        elif typ == "technique":
            if elem["id"] == body["id"]:
                break
        count+=1
    
    # Merge or add new entry
    if count < len(base):
        print("  [+] Merging existing entry")
        base[count] = body
    else:
        print("  [+] Adding new entry")
        base.append(body)

    valid = custom_validate(base, typ)
    if not valid:
        print("[-] Error: Validation of tools.json failed.")
        sys.exit(-1)

    # Write to file
    if typ == "tool":
        f = open(tools_file, 'w', encoding="UTF-8")
    elif typ == "technique":
        f = open(techniques_file, 'w', encoding="UTF-8")

    f.write(json.dumps(base, indent=4))
    f.close

    # store issue number for closing
    merged_issues.append(issue)

# Validate the final JSON
print("[+] Validating final JSON...")
with open(tools_file, 'r') as f:
    valid = custom_validate(f.read(), "tool")
error = 0
if not valid:
    print("[-] Error: Validation of tools.json failed.")
    error = 1

with open(techniques_file, 'r', encoding="UTF-8") as f:
    valid = custom_validate(f.read(), "technique")
if not valid:
    print("[-] Error: Validation of techniques.json failed.")
    error = 1

if error:
    sys.exit(-1)

print("\n\nFetching latest commits for git sources...")
fetchAllGitData(tools_file)

if merged_issues:
    print ("Commit message:")
    for iss in merged_issues:
        print ("close #" + str(iss["number"]),end=', ')
else:
    print ("No issues to close.")
