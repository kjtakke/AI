import pandas as pd

def removeValues(file, column, newFile, removeValues=[], showNweAndOldValues=False):
    df = pd.read_csv(file, header=0, dtype=str)
    index = []

    for item in df[column]:

        item = str(item)
        item = item.lower()
        for rep in removeValues:
            rep = rep.lower()
            item = item.replace(rep, "")

        item = item.strip()
        index.append(item)
    if showNweAndOldValues == True:
        df = df[column].tolist()
        df = list(zip(df, index))
        df = pd.DataFrame(df)
        df.columns = [column, column + " (New)"]
    else:
        df = pd.DataFrame(index)
        df.columns = [column]

    print(df.head())
    df.to_csv(newFile)
