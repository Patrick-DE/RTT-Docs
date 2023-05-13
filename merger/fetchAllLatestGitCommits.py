import json
import os
import re
from dotenv import load_dotenv
import requests

from tools import Tools, Tool

load_dotenv("..\.env")
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

def getLatestCommit(url):
    match = re.search(r"github\.com/([^/]+)/([^/]+)", url)
    if not match:
        return None

    owner = match.group(1)
    name = match.group(2)

    api_url = f"https://api.github.com/repos/{owner}/{name}"
    headers = {"Accept": "application/vnd.github+json", "Authorization": "Bearer "+GITHUB_API_KEY, "X-GitHub-Api-Version": "2022-11-28"}
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        if response.status_code == 404:
            print ("Could not find {}".format(api_url))
            return None
        else:
            raise Exception("Error: Unable to retrieve repository information for {}".format(url))

    # Extract the relevant information from the response
    data = json.loads(response.text)
    pushed_at = data["pushed_at"]
    archived = data["archived"]
    disabled = data["disabled"]

    # Return the information as a dictionary
    return pushed_at

def fetchAllLatestGitCommits():
    with open('tools.json', 'r') as f:
        toolBase: Tools = json.load(f)

    for tool in toolBase:
        if "github.com" in tool["source"]:
            if "latest_commit" not in tool:
                tool["latest_commit"] = None

            #if tool["latest_commit"] == None:
            try:
                updated = getLatestCommit(tool["source"])
                if updated == None:
                    continue

                tool["latest_commit"] = updated
            except Exception as ex:
                #print(ex)
                f = open("tools.json", "w")
                json.dump(toolBase, f, indent=2)
                f.close()

    f = open("tools.json", "w")
    json.dump(toolBase, f, indent=2)
    f.close()

#fetchAllLatestGitCommits()