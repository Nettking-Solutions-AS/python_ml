import json
from btc_predict import getHistoricData, fileImport

# Import the btc_predict module which contains the functions needed for this script



    
def getData():

    inputFile = 'output.txt'
    if fileImport(inputFile) is not None:
        # Get historic data from an API is no local cache
        rawData = fileImport(inputFile)
        data = json.loads(rawData)
        print('Collecting data from local cache.')
    else:
        data = getHistoricData()
    return data