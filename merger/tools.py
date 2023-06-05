from helpertypes import Requirements,Results
from typing import List, Set
import uuid

class Command(object):
    def __init__(self):
        self.id : str= str(uuid.uuid4())
        self.name: str= "NoName"
        self.description: str= "NoDescription"
        self.requirements : List[Requirements] = []
        self.results : List[Results] = []
        self.undetected: List[str] = []
        self.detected: List[str] = []
        
class Tools(object):
    def __init__(self):
        self.tools: List[Tool] = []

class Tool:
    def __init__(self):
        self.name : str= "NoName"
        self.phases : List[str] = []
        self.category: str = ""
        self.stealthy: bool = False #now called stealth
        self.platforms : List[str] = []
        self.source: str = ""
        self.description: str = ""
        self.undetected: List[str] = []
        self.detected: List[str] = []
        self.content: str = ""
        self.commands: Command = []
        self.references: str = []

    def expand_phases(self, dirs):
        exp_phases = []
        for phase in self.phases:
            for dir in dirs:
                if phase in dir:
                    exp_phases.append(dir)
        self.phases = exp_phases

def replace_oss(arr):
    res = []
    for elem in arr:
        elem = elem.strip()
        if elem == "#py":
            if "Python" not in res: res.append("Python")
        elif elem == "#ps1" or elem == "#win":
            if "Windows" not in res: res.append("Windows")
        elif elem == "#exe":
            if "Windows" not in res: res.append("Windows")
        elif elem == "#go":
            if "Cross Platform (GO)" not in res: res.append("Cross Platform (GO)")
        elif elem == "#linux":
            if "Linux" not in res: res.append("Linux")
        else:
            if elem not in res: res.append(elem) 
    return res

ToolSchema = {
    "$comment": "https://www.jsonschemavalidator.net/, https://jsonformatter.org/json-to-jsonschema",
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "object",
    "items": {
        "$ref": "#/definitions/Welcome10Element"
    },
    "definitions": {
        "Tool": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {"type": "string"},
                "phases": {"type": "array","items": {"type": "string"}, "minItems": 1},
                "category": {"type": "string"},
                "stealthy": {"type": "boolean"},
                "platforms" : {"type": "array","items": {"type": "string"}, "minItems": 1},
                "source": {"type": "string"},
                "description": {"type": "string"},
                "undetected": {"type": "array","items": {"type": "string"}},
                "detected": {"type": "array","items": {"type": "string"}},
                "content": {"type": "string"},
                "commands": {"type": "array","items": {"$ref": "#/definitions/Command"}},
                "references": {"type": "array","items": {"type": "string"}},
                "latest_commit": {"type": "string","format": "uri","qt-uri-protocols": ["http","https"]},
                "language": {"type": "string"}
            },
            "required": ["name", "phases", "category", "platforms", "source", "description"]
        },
        "Command": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string","format": "uuid"},
                "name": {"type": "string"},
                "description": {"type": "string"},
                "cmd": {"type": "string"},
                "tag": {"type": "string"},
                "results": {"type": "array","items": {"type": "string"}},
                "requirements": {"type": "object"},
                "detected": {"type": "array","items": {"type": "string"}},
                "undetected": {"type": "array","items": {"type": "string"}}
            },
            "required": ["cmd","description","id","name","results","tag"],
            "title": "Command"
        }
    }
}