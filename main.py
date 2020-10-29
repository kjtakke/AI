import json
import Ai
import pandas as pd
import pprint #https://docs.python.org/3/library/pprint.html#module-pprint

file = "https://raw.githubusercontent.com/kjtakke/AI/main/APC.csv"
trainingSet = "https://raw.githubusercontent.com/kjtakke/AI/main/trainingSet.csv"
jsonFileName = "postcodes.json"
indexColumn = "Suburb Name"
valueColumns = ["Postcode","State"]
removeValues = [" HMAS", " Barracks", " bks", " SA", " WA", " NT", " QLD"," NSW", " VIC", " ACT", " TAS"]

postcode = Ai.AI_Phraser
postcode().base_set(file=file, jsonFileName=jsonFileName, indexColumn=indexColumn, valueColumns=valueColumns)
#postcode.trainAI(trainingSet, jsonFileName, False)




#Sandpit
'''
with open(jsonFileName, 'r') as fp:
    indexDictionary = json.load(fp)

pp = pprint.PrettyPrinter(indent=2, width=80)
pp.pprint(indexDictionary["Belconnen Town Centre"])

valueColumns = ["Postcode","State"]
df = pd.read_csv("https://raw.githubusercontent.com/kjtakke/AI/main/APC.csv", header=0, dtype=str)




for x in range(len(valueColumns)):
    indexValues = []
    for key in valueColumns:
        lst = df[key].tolist()
        indexValues.append(lst[x])
    print(indexValues)

# State Map Region   District            Suburb Name Postcode
'''
