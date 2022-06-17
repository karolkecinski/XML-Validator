from heapq import merge
import os
import string
from Validator import Validator

XSD_schema = "pi-grammar.xsd"
mergeDir = "./merge"
ext = ".xml"

VDT = Validator(XSD_schema)

GOOD    = 0
BAD     = 0
DEBUG   = True

def printDebug(msg = '\n'):
    if DEBUG == True:
        print(msg)

def PrettyPrint(msg = []):
    for _ in msg:
        print(_)

print([x.path for x in os.scandir(mergeDir)])

invalidFiles = []

for XMLdir in os.scandir(mergeDir):
    if not os.path.isdir(XMLdir.path):
        continue
    printDebug(f"---------------- DIRECTORY: {XMLdir.path} ----------------")
    XMLdirPath = XMLdir.path
    directory = [os.path.join(XMLdirPath, _) for _ in os.listdir(XMLdirPath) if _.endswith(ext)]
    for file in directory:
        printDebug(file)
        try:
            if VDT.validate(file):
                GOOD += 1
            else:
                BAD += 1
                printDebug(f"ERROR: XML structure doesn\'t match schema at {file} in {directory}! \n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
                invalidFiles.append(file)
        except:
            BAD += 1
            printDebug(f"ERROR: XML structure doesn\'t match schema at {file} in {directory}! \n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
            invalidFiles.append(file)
        printDebug()

print('+++ DONE +++')

str = f'''
########################################
# Found:                               #
#  - {GOOD} .xml files matching schema    #
#  - {BAD} .xml files violating schema    #
########################################
'''
print(str)
print("\n------------------------------\n")
print(f"List of files violating schema:\n")
PrettyPrint(invalidFiles)