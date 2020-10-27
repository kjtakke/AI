import pandas as pd
import json









def createRefenceFile(file, jsonFileName, indexColumn, removeValues = []):
    """This function creates the json dictionary reference file to be used in the AiClass

    indexDictionary[i] = {
            "passed":[],            #All accepted answers                       ["passed"]                  =["name1","name2"]
            "two": {                #Number of letters
                "first":[],             #First part of the string               ["two"]["first"]            =[["ab",0],["bc",0]]
                "mid":[],               #Middle part of the string              ["two"]["mid"]
                "end":[]                #End part of the string                 ["two"]["end"]
            },
            "three": {
                "first":[],                                                    #["three"]["first"]          =[["abc",0],["bcd",0]]
                "mid":[],                                                      #["three"]["mid"]
                "end":[]                                                       #["three"]["end"]
            },
            "four": {
                "first":[],                                                    #["four"]["first"]           =[["abcd",0],["bcde",0]]
                "mid":[],                                                      #["four"]["mid"]
                "end":[]                                                       #["four"]["end"]
            },
            "scores":{              #Acepted Scores and aggregated values
                "allScores": [],    #All accepted Scores                        ["scores"]["allScores"]
                "statistics": {     #Statistics
                    "min": 0,           #Min                                    ["scores"]["min"]
                    "max": 0,           #Max                                    ["scores"]["max"]
                    "median": 0,        #Median                                 ["scores"]["median"]
                    "average": 0,       #Average                                ["scores"]["average"]
                    "stDev": 0,         #Standard Devation                      ["scores"]["stDev"]
                    "sum": 0            #Sum                                    ["scores"]["sum"]
                },
            }
        }

    """
    df = pd.read_csv(file + ".csv", header=0, dtype=str)
    index = df[indexColumn].tolist()
    indexDictionary = {}
    for i in index:
        indexDictionary[i] = {
            "passed":[],
            "two": {
                "first":[],
                "mid":[],
                "end":[]
            },
            "three": {
                "first":[],
                "mid":[],
                "end":[]
            },
            "four": {
                "first":[],
                "mid":[],
                "end":[]
            },
            "scores":{
                "allScores": [],
                "statistics": {
                    "min": 0,
                    "max": 0,
                    "median": 0,
                    "average": 0,
                    "stDev": 0,
                    "sum": 0
                },
            }
        }

    for keys, values in indexDictionary.items():
        strLen = len(keys)

        for x in range(strLen-1):       #two letters
            strShort = keys[x:x+2].lower()

            if x <= 2:
                values["two"]["first"].append([strShort,0])
            elif x <= strLen - 4:
                values["two"]["mid"].append([strShort,0])
            else:
                values["two"]["end"].append([strShort,0])

        for x in range(strLen-2):       #three letters
            strShort = keys[x:x+3].lower()

            if x <= 4:
                values["three"]["first"].append([strShort,0])
            elif x <= strLen - 5:
                values["three"]["mid"].append([strShort,0])
            else:
                values["three"]["end"].append([strShort,0])

        if strLen > 5:

            for x in range(strLen-3):   #four letters
                strShort = keys[x:x+4].lower()

                if x <= 5:
                    values["four"]["first"].append([strShort,0])
                elif x <= strLen - 6:
                    values["four"]["mid"].append([strShort,0])
                else:
                    values["four"]["end"].append([strShort,0])

    with open(jsonFileName + ".json", 'w') as fp:
        json.dump(indexDictionary, fp)


