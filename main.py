import pandas as pd
import json
import AiClass
import CreateReferences

file = "Australian Post Code Information"
jsonFileName = "postcodes"
indexColumn = "Suburb Name"
removeValues = [" HMAS", " Barracks", " bks", " SA", " WA", " NT", " QLD"," NSW", " VIC", " ACT", " TAS"]

def createRefenceFile(file, jsonFileName, indexColumn, removeValues = []):
    """This function creates the json dictionary reference file to be used in the AiClass"""

    df = pd.read_csv(file + ".csv", header=0, dtype=str)

    index = df[indexColumn].tolist()

    baseDictionary = {
        "passed":[],            #words that passed the test
        "two": {                #two letters ("ab", "ba")
            "first":[],       #first three letters and number of times found in correct match
            "mid":[],         #between 2 and -3 letters and number of times found in correct match
            "end":[]          #last three letters and number of times found in correct match
        },
        "three": {              #thress letters ("abc", "bac")
            "first":[],
            "mid":[],
            "end":[]
        },
        "four": {               #four letters ("abcd", "badc")
            "first":[],
            "mid":[],
            "end":[]
        },
        "scores":[]        #all scores
    }

    indexDictionary = dict.fromkeys(index, baseDictionary)

    for keys, values in indexDictionary.items():
        strLen = len(keys)

        for x in range(strLen-1): #two letters
            strShort = keys[x:x+2].lower()
            if x <= 2:
                values["two"]["first"].append([strShort,0])
            elif x <= strLen - 4:
                values["two"]["mid"].append([strShort,0])
            else:
                values["two"]["end"].append([strShort,0])

        for x in range(strLen-2): #three letters
            strShort = keys[x:x+3].lower()
            if x <= 4:
                values["three"]["first"].append([strShort,0])
            elif x <= strLen - 5:
                values["three"]["mid"].append([strShort,0])
            else:
                values["three"]["end"].append([strShort,0])

        if strLen > 5:
            for x in range(strLen-3): #four letters
                strShort = keys[x:x+4].lower()
                if x <= 5:
                    values["four"]["first"].append([strShort,0])
                elif x <= strLen - 6:
                    values["four"]["mid"].append([strShort,0])
                else:
                    values["four"]["end"].append([strShort,0])
        print(values)
        z = z + 1
        if z == 3: break
  
  return indexDictionary

indexDictionary = createRefenceFile(file, jsonFileName, indexColumn, removeValues)
