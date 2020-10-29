import pandas as pd
import json
import os

class AI_Phraser:
    """This class enables the creation an AI infrastructure"""

    def __init__(self, appendUnmatchedItems=True, reiterate=True, iterationEndPoint=999999999, reiterateMatchedItems=True, reiterateAppendedItems=True):
        self.appendUnmatchedItems = appendUnmatchedItems
        self.reiterate = reiterate
        self.iterationEndPoint = iterationEndPoint
        self.reiterateMatchedItems = reiterateMatchedItems
        self.reiterateAppendedItems = reiterateAppendedItems

    def _breakdown(self):
        """This function develops the JSON format for items to be compared"""
        pass

    def _scoring(self):
        """This function creates the neural mapping by adding or subtracting scores"""
        pass

    def _blank_canvas(self):
        """This function creates a blank JSON canvas which is used if no reference file is identified/loaded"""
        pass

    def _compare(self):
        """This function compares two phrases before scoring"""
        pass

    def _init_iterate(self):
        """This function iterates through a given list"""
        pass

    def _iterate_matched_items(self):
        """This function iterates through all matched items"""
        pass

    def _iterate_transient_items(self):
        """This function iterates through all items labled 'transient'"""
        pass

    def _reiterate(self):
        """This function reiterates based in the users selection"""
        pass

    def _add_phrase(self):
        pass

    def _create_migrate_file(self):
        pass

    def _output(self):
        pass

    def _gui(self):
        pass

    def load(self):
        pass

    def migrate(self):
        pass

    def nesting(self):
        pass

    def test_file(self, file, testColumn, answerColumn, updateReferenceFile = False):
        """This function tests know values against the AI Reference File"""
        df = pd.read_csv(file, header=0, dtype=str)
        print(df.head())
        indexDictionary = {}
        print(df.count)

    def trainAI(self, trainingFile, referenceFile, updateReferenceFile = False):
        """This function trains the AI"""
        trainingSet = pd.read_csv(trainingFile, header=0, dtype=str)
        print(trainingSet.head())
        with open(referenceFile, 'r') as fp:
            indexDictionary = json.load(fp)
        print(indexDictionary["Belconnen Town Centre"])

    def create_base_set_by_deliminator(self):
        """This function is used to break text into phrases by deliminator"""
        pass

    def base_set(self, file, jsonFileName, indexColumn, valueColumns):
        """This function creates the json dictionary reference file to be used in the AI

        indexDictionary[i] = {
                "type": "fixed",        #Base list or transient list                ["type"]                    ="fixed" or "transient"
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
            :param jsonFileName:
            :param indexColumn:
            :param valueColumns:

        """
        df = pd.read_csv(file, header=0, dtype=str)
        index = df[indexColumn].tolist()

        z = 0
        indexDictionary = {}
        for i in index:
            indexValues = []

            for key in valueColumns:
                lst = df[key].tolist()
                indexValues.append(lst[z])

            indexDictionary[i] = {
                "type": "fixed",
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
