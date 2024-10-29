import json
import os
import re
from dotenv import load_dotenv
import requests

from tools import Tools, Tool

load_dotenv("..\.env")
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

def getGitHubData(url):
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
    return data

def fetchAllGitData(tools_file):
    with open(tools_file, 'r') as f:
        toolBase: Tools = json.load(f)

    for tool in toolBase:
        if "github.com" in tool["source"]:
            try:
                data = getGitHubData(tool["source"])
            except Exception as ex:
                print(ex)
                f = open(tools_file, "w")
                json.dump(toolBase, f, indent=2)
                f.close()

            if data:
                tool["latest_commit"] = data.get("pushed_at", None)
                tool["language"] = data.get("language", None)


    f = open(tools_file, "w")
    json.dump(toolBase, f, indent=2)
    f.close()

#fetchAllGitData()