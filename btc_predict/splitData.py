def splitData(df):
    """
    Splits a dataframe containing Bitcoin price data into training and testing sets.

    Args:
        df (pandas.DataFrame): The dataframe containing the Bitcoin price data.

    Returns:
        tuple: A tuple containing the training data (pandas.DataFrame) and the testing data (pandas.DataFrame).
    """

    # Split the data into training and testing sets
    train_data = df.loc['2011-01-01':'2021-12-31']
    test_data = df.loc['2022-01-01':'2023-03-13']

    # Return the training and testing data as a tuple
    return train_data, test_data
