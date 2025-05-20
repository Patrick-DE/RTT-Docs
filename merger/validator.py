
import json
from jsonschema import validate


def custom_validate(data, select):
    # if data is string, parse it
    if isinstance(data, str):
        data = parse_json(data)
    error = 0
    # custom validation
    if select == 'technique':
        schema = TechniqueSchema
    elif select == 'tool':
        schema = ToolSchema
        data = autofix(data, select)
        error = validate_commands(data)
        error = validate_results(data)
    else:
        raise ValueError('Invalid schema type')

    # General validation
    error = validate_schema(data, schema)

    return error



def parse_json(data):
    try:
        body = json.loads(data)
    except Exception as ex:
        print(ex)
        return 1
    return body

def validate_commands(data):
    print("  [+] Validating commands...")
    if not isinstance(data, list):
        data = [data]

    for tool in data:
        for command in tool['commands']:
            if not command:
                print('    [!] Empty command for tool: ' + tool['name'])
                return False
    return True 

def validate_results(data):
    print("  [+] Validating results...")
    if not isinstance(data, list):
        data = [data]

    for tool in data:
        for command in tool['commands']:
            if command and 'results' not in command:
                return False
    return True

def validate_schema(data, schemaa):
    print("  [+] Validating json schema...")
    try:
        validate(data, schema=schemaa)
        return True
    except Exception as ex:
        print(ex)
        return False

def autofix(data, select):
    print("  [+] Autofixing errors if possible...")
    if select == 'tool':
        replace_nulls_with_empty_string(data, 'language')
        remove_nulls_from_attribute(data, 'commands')
    return data

def replace_nulls_with_empty_string(data, attribute):
    """Recursively replace attribute values that are None with empty strings in a nested dictionary."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == attribute and value is None:
                print("    [!] Replacing null value with empty string for attribute: " + attribute)
                data[key] = ""
            else:
                # Recursively call the function for nested dictionaries or lists
                replace_nulls_with_empty_string(value, attribute)
    elif isinstance(data, list):
        for item in data:
            replace_nulls_with_empty_string(item, attribute)

def remove_nulls_from_attribute(data, attribute):
    """Remove null (None) values from the specified attribute in the data."""
    if isinstance(data, dict):
        # Check if the attribute exists and is a list
        if attribute in data and isinstance(data[attribute], list):
            # Filter out None values from the specified attribute list
            data[attribute] = [item for item in data[attribute] if item is not None]
        
        # Recursively call the function for nested dictionaries or lists
        for key, value in data.items():
            remove_nulls_from_attribute(value, attribute)

    elif isinstance(data, list):
        for item in data:
            remove_nulls_from_attribute(item, attribute)

ToolSchema = {
    "$comment": "https://www.jsonschemavalidator.net/, https://jsonformatter.org/json-to-jsonschema",
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "array",
    "items": {
        "$ref": "#/definitions/Tool"
    },
    "definitions": {
        "Tool": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {"type": "string", "minLength": 2},
                "phases": {"type": "array","items": {"$ref": "#/definitions/Phase"}, "minItems": 1},
                "category": {"type": "string"},
                "stealthy": {"type": "boolean"},
                "platforms" : {"type": "array","items": {"type": "string"}, "minItems": 1},
                "source": {"type": "string","format": "uri","qt-uri-protocols": ["http","https"]},
                "description": {"type": "string"},
                "undetected": {"type": "array","items": {"type": "string"}},
                "detected": {"type": "array","items": {"type": "string"}},
                "content": {"type": "string"},
                "commands": {"type": "array","items": {"type": "array", "$ref": "#/definitions/Command"}},
                "references": {"type": "array","items": {"type": "string"}},
                "latest_commit": {"type": "string"},
                "language": {"type": "string"}
            },
            "required": ["name", "phases", "category", "platforms", "source", "description"],
        },
        "Command": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string","format": "uuid"},
                "name": {"type": "string", "minLength": 2},
                "description": {"type": "string"},
                "cmd": {"type": "string"},
                "tag": {"type": "string"},
                "results": {"type": "array","items": {"type": "string"}},
                "requirements": {"type": "object"},
                "detected": {"type": "array","items": {"type": "string"}},
                "undetected": {"type": "array","items": {"type": "string"}},
                "references": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "uri",
                        "qt-uri-protocols": [
                            "http",
                            "https"
                        ]
                    }
                }
            },
            "required": ["cmd","description","id","name","results","tag"],
            "title": "Command"
        },
        "Phase": {
            "type": "string",
            "enum": [
                "00. Infrastructure",
                "01. Initial Access",
                "02. Reconnaissance",
                "03. Host Enumeration",
                "04. Persistence",
                "05. Privilege Escalation",
                "06. Domain Enumeration",
                "07. Lateral Movement",
                "08. Credentials & User Impersonation",
                "09. AD Misconfigurations",
                "10. Bypassing Defenses",
            ],
            "title": "Phase"
        }
    }
}

#https://codebeautify.org/json-to-json-schema-generator
TechniqueSchema = {
    "$comment": "https://www.jsonschemavalidator.net/, https://jsonformatter.org/json-to-jsonschema",
    "$schema": "http://json-schema.org/draft-06/schema#",
    "type": "array",
    "items": {
        "$ref": "#/definitions/Technique"
    },
    "definitions": {
        "Technique": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {"type": "string", "minLength": 2},
                "id": {"type": "string","format": "uuid"},
                "phase": {"$ref": "#/definitions/Phase"},
                "ttp": {"type": "string", "minLength": 2},
                "description": {"type": "string", "minLength": 2},
                "external": {"type": "boolean"},
                "stealthy": {"type": "boolean"},
                "content": {"type": "string"},
                "category": {"type": "string"},
                "changes": {"type": "array","items": {"type": "string"}},
                "tools": {"type": "array","items": {"type": "string"}},
                "steps": {"type": "array","items": {"$ref": "#/definitions/Step"}},
                "references": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "format": "uri",
                        "qt-uri-protocols": [
                            "http",
                            "https"
                        ]
                    }
                }
            },
            "required": [
                "name",
                "id",
                "category",
                #"changes",
                #"content",
                "description",
                "external",
                "phase",
                "stealthy",
                "steps",
                #"tools",
                "ttp"
            ],
            "title": "Technique"
        },
        "Step": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {"type": "string","format": "uuid"},
                "name": {"type": "string"},
                "description": {"type": "string"},
                "requirements": {"type": "object"},
                "results": {"type": "array","items": {"type": "string"}},
                "commands": {"type": "array","items": {"$ref": "#/definitions/Command"}}
            },
            "required": [
                "description",
                "id",
                "name",
                "requirements",
                "results"
            ],
            "title": "Step"
        },
        "Phase": {
            "type": "string",
            "enum": [
                "00. Infrastructure",
                "01. Initial Access",
                "02. Reconnaissance",
                "03. Host Enumeration",
                "04. Persistence",
                "05. Privilege Escalation",
                "06. Domain Enumeration",
                "07. Lateral Movement",
                "08. Credentials & User Impersonation",
                "09. AD Misconfigurations",
                "10. Bypassing Defenses"
            ],
            "title": "Phase"
        },
        "Command": {
            "type": "string",
            "title": "Command"
        },
    }
}
