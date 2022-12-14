import json
from attackcti import attack_client

class APT:
  def __init__(self, name, description, aliases, techniques):
    self.name = name
    self.description = description
    self.aliases = aliases
    self.techniques = techniques

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

# lift = attack_client()
# groups = lift.get_groups()
# techniques = lift.get_techniques()
# with open("apt.json", "w") as f:
#   f.write(techniques)
lift = attack_client()
techniques_used = lift.get_techniques_used_by_all_groups()

groups = lift.get_groups()
#groups = lift.remove_revoked(groups)
apt_list = []

for g in groups:
  if g["revoked"]:
    continue

  techniques_list = []

  for gut in techniques_used:
    if gut["revoked"]:
      continue

    if g['name'] == gut['name']:
      technique_dict = dict()
      technique_dict['techniqueId'] = gut['technique_id']
      technique_dict['techniqueName'] = gut['technique']
      technique_dict['comment'] = gut['relationship_description']
      technique_dict['tactic'] = []
      for tactic in gut['tactic']:
        technique_dict['tactic'].append(tactic.phase_name)
      technique_dict['group_ref'] = []
      for refs in gut['external_references']:
        if hasattr(refs, "url") or "url" in refs:
          technique_dict['group_ref'].append(refs["url"])
      techniques_list.append(technique_dict)

  aliases = [gut['name']]
  if hasattr(g, "aliases"):
    aliases = g["aliases"]

  apt_list.append(APT(g['name'], g["description"], aliases, techniques_list))


with open("apts.json", "w") as f:
  json_string = json.dump([apt.__dict__ for apt in apt_list], f)