def addRSIToDf(df):
    """
    Calculates the Relative Strength Index (RSI) for the given dataframe and adds it as a new column.

    Args:
        df (pandas.DataFrame): The dataframe to add the RSI to. Must contain a 'Price' column.

    Returns:
        None

    Raises:
        ValueError: If the 'Price' column is not found in the dataframe.
    """

    # Check that the 'Price' column is present in the dataframe
    if 'Price' not in df.columns:
        raise ValueError("The 'Price' column is not present in the dataframe.")

    # Calculate the RSI using the formula
    delta = df['Price'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))

    # Add the RSI to the dataframe, filling any missing values with 0
    df['RSI'] = rsi.fillna(0)
