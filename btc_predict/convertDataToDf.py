import pandas as pd

def convertDataToDf(data):
    """
    Converts the given data dictionary to a pandas dataframe.

    Args:
        data (dict): The data to convert. Must be a dictionary with Unix timestamp keys and price values.

    Returns:
        pandas.DataFrame: The converted dataframe.

    Raises:
        ValueError: If the data is not in the expected format.
    """

    try:
        # Convert the data to a pandas dataframe, using the Unix timestamps as the index
        df = pd.DataFrame.from_dict(data, orient='index', columns=['Price'])

        return df

    except Exception as e:
        # If there is an error, raise a ValueError with a descriptive error message
        raise ValueError("Error converting data to dataframe: {}".format(e))
