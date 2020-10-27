import json
import Ai

import pprint #https://docs.python.org/3/library/pprint.html#module-pprint

file = "https://raw.githubusercontent.com/kjtakke/AI/main/APC"
jsonFileName = "postcodes"
indexColumn = "Suburb Name"
removeValues = [" HMAS", " Barracks", " bks", " SA", " WA", " NT", " QLD"," NSW", " VIC", " ACT", " TAS"]
Ai.createRefenceFile(file, jsonFileName, indexColumn, removeValues)

with open(jsonFileName + ".json", 'r') as fp:
    indexDictionary = json.load(fp)

pp = pprint.PrettyPrinter(indent=2, width=80)
pp.pprint(indexDictionary["Lawson"])
