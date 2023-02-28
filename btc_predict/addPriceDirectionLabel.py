def addPriceDirectionLabel(df):
    """
    Adds a label indicating the direction of the price change to the given dataframe.

    Args:
        df (pandas.DataFrame): The dataframe to add the label to. Must contain a 'Price' column.

    Returns:
        None

    Raises:
        ValueError: If the 'Price' column is not found in the dataframe.
    """

    # Check that the 'Price' column is present in the dataframe
    if 'Price' not in df.columns:
        raise ValueError("The 'Price' column is not present in the dataframe.")

    # Calculate the price difference between each row
    price_diff = df['Price'].diff()

    # Add a label indicating the direction of the price change (1 if positive, 0 if negative or zero)
    df['Label'] = (price_diff > 0).astype(int)
