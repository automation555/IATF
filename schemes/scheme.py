from dataclasses import dataclass,asdict
import json
import datetime

@dataclass
class Plane(object):
    @property
    def GetJson(self):
        j = asdict(self)
        return json.dumps(j,indent = 2)


@dataclass
class Document_header(Plane):
    title:str
    members:list = field(default_factory = list)
    start_date:datetime


@dataclass
class Document(Plane):
    header:Document_header
    contents:str

@dataclass
class Documents(Plane):
    documents:list[Document] = filed(default_factory = list)

    

