import requests
import sys
import json
import os
import yaml
# from tools import ToolSchema
# from techniques import TechniqueSchema
from jsonschema import validate
from dotenv import load_dotenv

load_dotenv("..\.env")
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

merged_issues = []

headers = {"Accept": "application/vnd.github+json", "Authorization": "Bearer "+GITHUB_API_KEY, "X-GitHub-Api-Version": "2022-11-28", }
r = requests.get('https://api.github.com/repos/arttoolkit/arttoolkit.github.io/contents/_wadcoms', headers=headers)
issues = r.json()
if "message" in issues:
    print("[-] Error: " + issues["message"])
    sys.exit(-1)

print("[+] Found " + str(len(issues)) + " issues.")

files = []
for file in issues:
    download_url = file['download_url']
    file_name = file['name']
    print(f'Downloading {file_name}...')
    response = requests.get(download_url)
    content = response.content.decode('utf-8')
    try:
        obj = yaml.safe_load(content[3:-3])
    except:
        print("Ignoring {} because of wrong format!".format(file_name))
    files.append(response)

for file in files:
    file.description.split("")

print("Done")