# Import the btc_predict module which contains the functions needed for this script
from btc_predict import *

def main():
    """
    This is the main function that runs the script.
    """

    # Get historic data from an API
    data = getHistoricData()

    # Write the data to a file
    writeToFile(data)

    # Convert the data to a pandas dataframe
    df = convertDataToDf(data)

    # Add the RSI (Relative Strength Index) to the dataframe
    addRSIToDf(df)

    # Add a label indicating the direction of the price change to the dataframe
    addPriceDirectionLabel(df)

    # Split the dataframe into train and test data
    train_data, test_data = splitData(df)

    # Create a machine learning model
    model = createMlModel()

    # Train and test the machine learning model
    runModel(model, df, train_data, test_data)

if __name__ == '__main__':
    main()