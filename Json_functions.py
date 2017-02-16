import json
import sys
import os


def readJson (filePath):
    if not os.path.isfile(filePath):
        print("There is no file in this path")
        sys.exit(1)
    with open(filePath, mode="r", encoding="utf-8") as jsonFile:
        movieDB = json.loads(jsonFile.read())
        return movieDB
