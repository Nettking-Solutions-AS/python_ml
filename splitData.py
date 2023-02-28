def splitData(df):    
    # Split the data into training and testing sets
    train_data = df.loc['2011-01-01':'2021-12-31']
    test_data = df.loc['2022-01-01':'2023-02-28']
    return train_data, test_data