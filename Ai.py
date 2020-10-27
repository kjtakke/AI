import pandas as pd
import json


def testAgainstReferenceFile(file, updateReferenceFile = False):
    """This function tests know values against the AI Reference File"""
    pass






def createRefenceFile(file, jsonFileName, indexColumn, valueColumns):
    """This function creates the json dictionary reference file to be used in the AI

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
                    "stDev": 0,         #Standard Deviation                      ["scores"]["stDev"]
                    "sum": 0            #Sum                                    ["scores"]["sum"]
                },
            },
            "values": []                #csv values to bring accross            ["values"] i.e. ['2617', 'ACT']
        }

    """
    df = pd.read_csv(file + ".csv", header=0, dtype=str)
    index = df[indexColumn].tolist()

    z = 0
    indexDictionary = {}
    for i in index:
        indexValues = []

        for key in valueColumns:
            lst = df[key].tolist()
            indexValues.append(lst[z])

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
            },
            "values": indexValues
        }
        z = z + 1

    for keys, values in indexDictionary.items():
        strLen = len(keys)

        for x in range(strLen-1):       #two letters
            strShort = keys[x:x+2].lower()

            if x < 1:
                values["two"]["first"].append([strShort,0])
            elif x >= strLen - 2:
                values["two"]["end"].append([strShort,0])
            else:
                values["two"]["mid"].append([strShort,0])

        for x in range(strLen-2):       #three letters
            strShort = keys[x:x+3].lower()

            if x < 1:
                values["three"]["first"].append([strShort,0])
            elif x >= strLen - 3:
                values["three"]["end"].append([strShort,0])
            else:
                values["three"]["mid"].append([strShort,0])

        if strLen > 8:

            for x in range(strLen-3):   #four letters
                strShort = keys[x:x+4].lower()

                if x < 1:
                    values["four"]["first"].append([strShort,0])
                elif x >= strLen - 4:
                    values["four"]["end"].append([strShort,0])
                else:
                    values["four"]["mid"].append([strShort,0])

    with open(jsonFileName + ".json", 'w') as fp:
        json.dump(indexDictionary, fp)


