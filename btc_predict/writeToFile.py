from btc_predict.fileImport import *

def writeToFile(data):
    """
    Writes Bitcoin price data to a file.

    Args:
        data (dict): A dictionary containing the Bitcoin price data.

    Returns:
        None
    """

    # Convert the data to a string, replacing all single quotes with double quotes
    dataString = str(data)
    dataJSON = dataString.replace("'", '"')

    # Read the existing file contents
    existingFile = str(fileImport("output.txt"))

    # Check if the new data is different from the existing data
    if dataJSON == existingFile:
        print('Output.txt already contains up-to-date data.')
    else:
        # Open a file for writing
        with open("output.txt", "w") as f:
            # Write the data to the file
            f.write(dataJSON)

        print("Data saved to output.txt.")
