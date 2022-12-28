import requests
import sys
import json
import os
from tools import ToolSchema
from techniques import TechniqueSchema
from jsonschema import validate
from dotenv import load_dotenv

load_dotenv()
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

headers = {"Accept": "application/vnd.github+json", "Authorization": "Bearer "+GITHUB_API_KEY, "X-GitHub-Api-Version": "2022-11-28"}
r = requests.get('https://api.github.com/repos/Patrick-DE/RTT-Docs/issues', headers=headers)
issues = r.json()
if hasattr(issues, "message"):
    print("[-] Error: " + issues["message"])
    sys.exit(-1)

print("[+] Found " + str(len(issues)) + " issues.")

# read base files
with open('tools.json', 'r') as f:
    toolBase = json.load(f)
with open('techniques.json', 'r') as f:
    techniqueBase = json.load(f)

for issue in issues:
    if "New tool:" in issue["title"]:
        typ = ToolSchema
        base = toolBase
        print("[+] Loading tool json for " + issue["title"])
        
    elif "New technique:" in issue["title"]:
        typ = TechniqueSchema
        base = techniqueBase
        print("[+] Loading technique json for " + issue["title"])

    # Validation of JSON
    body = json.loads(issue["body"][1:-1])
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
        f = open('../tools.json', 'w')
    elif typ == TechniqueSchema:
        f = open('../techniques.json', 'w')

    f.write(json.dumps(base))
    f.close
