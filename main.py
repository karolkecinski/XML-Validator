import os
from Validator import Validator

XSD_schema = ""
mergeDir = "./merge"
ext = ".xml"

VDT = Validator(XSD_schema)

for XMLdir in mergeDir:
    directory = [_ for _ in os.path.abspath(XMLdir) if _.endswith(ext)]
    for file in directory:
        if VDT.validate(file):
            print("true")
        else:
            print(f"ERROR: XML structure doesn't match schema at {file}! -------------------------------- ")