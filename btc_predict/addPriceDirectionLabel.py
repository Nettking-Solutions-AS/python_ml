def addPriceDirectionLabel(df):
    # Add price direction label to the dataframe
    df['PriceDiff'] = df['Price'].diff()
    df['Label'] = (df['PriceDiff'] > 0).astype(int)