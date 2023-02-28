import pandas as pd

def convertDataToDf(data):
    try:
        # Convert the data to a pandas dataframe
        df = pd.DataFrame.from_dict(data, orient='index', columns=['Price'])
        return df
    except:
        print('Unable to convert data')