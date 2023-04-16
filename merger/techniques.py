import numbers
from helpertypes import Requirements,Results
from typing import List, Set
import json
import uuid
from tools import Command

class Step(object):
    def __init__(self):
        self.id : str=str(uuid.uuid4())
        self.name: str= "NoName"
        self.description: str= "N/A"
        #self.commands: List[Command] = []
        self.requirements : str = ""
        self.results : str = ""

class Technique(object):
    def __init__(self):
        self.id : str=str(uuid.uuid4())
        self.name : str= "NoName"
        self.phase : str = "NoPhase"
        self.ttp : str = "T0000"
        self.external : bool = False
        self.description : str = "NoDescription"
        self.content : str = ""
        self.category: str = ""
        self.stealthy: bool = False
        self.changes: List[str] = []
        self.tools: List[str] = []
        self.steps: List[Step] = []
        self.references: str = []
        
    def to_json(self):
        delattr(self, "changes")
        return json.dumps(self, default=lambda o: o.__dict__)

class Meta(object):
    """Statistics object for bloodhound"""
    def __init__(self):
        self.type: str = "Technique"
        self.count: int = 0
        self.version: int = 1

class Methodology(object):
    def __init__(self):
        self.methodology : List[Technique] = []
        self.meta: Meta = Meta()

    def print_requirement_result(self):
        requirements: list = []
        results: list = []
        for method in self.methodology:
            for requirement in method.requirements:
                requirements.append(requirement.to_string())
            for result in method.results:
                results.append(result.to_string())
        print("Requirements:")
        if len(requirements) > 0:
            print("\n".join(sorted(set(requirements))))
        print("Results:")
        if len(results) > 0:
            print("\n".join(sorted(set(results))))

    def to_json(self):
        self.meta.count = len(self.methodology)
        delattr(self, "changes")
        return json.dumps(self, default=lambda o: o.__dict__)

#https://codebeautify.org/json-to-json-schema-generator
TechniqueSchema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "definitions": {
        "Technique": {
            "title": "Technique",
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string","format": "uuid"},
                "name": {"type": "string"},
                "phase": {"type": "string"},
                "ttp": {"type": "string"},
                "external": {"type": "boolean"},
                "description": {"type": "string"},
                "content": {"type": "string"},
                "category": {"type": "string"},
                "stealthy": {"type": "boolean"},
                "changes": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "tools": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "steps": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/Step"}
                },
                "references": {
                    "type": "array",
                    "items": {"type": "string"}
                },
            },
            "required": ["id","name","phase","ttp","description",],
        },
        "Step": {
            "type": "object",
            "properties": {
                "id": {"type": "string","format": "uuid"},
                "name": {"type": "string"},
                "description": {"type": "string"},
                "requirements": {"type": "string"},
                "results": {"type": "string"}
            },
            "required": ["id","name",],
        }
    }
}