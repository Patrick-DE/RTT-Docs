import json
from urllib.parse import urlparse
from aptTypes import APT, APT_min, exclusion_list
#from getReleaseDate import getReleaseDate
from attackcti import attack_client
from dateutil import parser

lift = attack_client()
techniques_used = lift.get_techniques_used_by_all_groups()

groups = lift.get_groups()
#groups = lift.remove_revoked(groups)
apt_list = []
apt_list_min = []

for g in groups:
  if g["revoked"]:
    continue

  techniques_list = []
  techniques_list_min = []

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
          creation_date = None
          if urlparse(refs["url"]).netloc == "attack.mitre.org":
            creation_date = parser.parse(gut["modified"]).strftime('%d.%m.%Y')
          if refs["url"] not in exclusion_list:
            technique_dict['group_ref'].append({'date': creation_date, 'url': refs["url"]})
      techniques_list.append(technique_dict)
      techniques_list_min.append({'techniqueId': gut['technique_id']})

  aliases = [gut['name']]
  if hasattr(g, "aliases"):
    aliases = g["aliases"]

  apt_list.append(APT(g['name'], g["description"], aliases, techniques_list))
  apt_list_min.append(APT_min(g['name'], techniques_list_min))


with open("apts.json", "w") as f:
  json.dump([apt.__dict__ for apt in apt_list], f, indent=2)

with open("apts_min.json", "w") as f:
  json.dump([apt.__dict__ for apt in apt_list_min], f, indent=2)

print("Fetching release dates...")
#getReleaseDate()