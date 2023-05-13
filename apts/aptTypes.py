from typing import List

exclusion_list = ["https://www.sans.org/cyber-security-summit/archives/file/summit-archive-1554718868.pdf",
                  "https://objective-see.com/blog/blog_0x3D.html",
                  "https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1680.do",
                  "https://www.fireeye.com/content/dam/fireeye-www/summit/cds-2019/presentations/cds19-executive-s08-achievement-unlocked.pdf",
                  
                  ]

class APT:
  def __init__(self, name, description, aliases, techniques):
    self.name: str = name
    self.description: str = description
    self.aliases: List[str] = aliases
    self.techniques: List[Technique] = techniques

class Technique:
  def __init__(self, techniqueId, techniqueName, comment, tactic, group_ref):
    self.techniqueId: str = techniqueId
    self.techniqueName: str = techniqueName
    self.comment: str = comment
    self.tactic: List[str] = tactic
    self.group_ref: List[Ref] = group_ref

class Ref:
  def __init__(self, date, url):
    self.date: str = date
    self.url: str = url

  # def toJSON(self):
  #   return json.dumps(self, default=lambda o: o.__dict__, 
  #       sort_keys=True, indent=4)

class APT_min:
  def __init__(self, name, techniques):
    self.name = name
    self.techniques = techniques
