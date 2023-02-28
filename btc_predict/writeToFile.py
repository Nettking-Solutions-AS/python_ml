
from btc_predict.fileImport import *


def writeToFile(data):
    dataString = str(data)
    existingFile = str(fileImport("output.txt"))
    if dataString == existingFile:
        print('Output.txt har allerede oppdaterte data.')
    else:
        # Open a file for writing
        with open("output.txt", "w") as f:
            # Write the data to the file
            f.write(dataString)

        print("Data saved to output.txt.")