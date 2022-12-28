from typing import List


class Requirements(object):
    """Only one requirement"""
    def __init__(self) -> None:
        self.name : str = ""
        self.category : str = ""
        self.exists : bool = True
    
    def parse(self, str: str) -> None:
        lis = str.split(".")
        if lis[0] == "!":
            self.value = False

        if len(lis) > 1:
            self.name = lis.pop()
            self.category = ".".join(lis)
        elif len(lis) == 1:
            self.name = lis[0]
            #self.type = "NoClue"

    def to_string(self) -> str:
        return "{}{}.{}".format(self.value, self.category, self.name)
    
class Results(object):
    """Only one result"""
    def __init__(self) -> None:
        self.name : str = ""
        self.category : str = ""
        self.exists : bool = True

    def parse(self, str: str) -> None:
        lis = str.split(".")
        if lis[0] == "!":
            self.value = False

        if len(lis) > 1:
            self.name = lis.pop()
            self.category = ".".join(lis)
        elif len(lis) == 1:
            self.name = lis[0]
            #self.type = "NoClue"

    def to_string(self) -> str:
        return "{}{}.{}".format(self.value, self.category, self.name)


class Command(object):
    def __init__(self, methodname) -> None:
        self.content: str = ""
        self.methodname: str = methodname

class MyFile(object):
    def __init__(self, name, path) -> None:
        self.name: str = name
        self.path: str = path
        self.change: List[str] = []