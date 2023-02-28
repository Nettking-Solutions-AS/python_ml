from btc_predict.hyperParameterOptimize import *

def runModel(model, df, train_data, test_data):
    """
    Trains and tests a machine learning model on Bitcoin price data.

    Args:
        model (sklearn.ensemble.RandomForestClassifier): The machine learning model to train and test.
        df (pandas.DataFrame): The dataframe containing the Bitcoin price data.
        train_data (pandas.DataFrame): The training data to use for training the model.
        test_data (pandas.DataFrame): The testing data to use for testing the model.

    Returns:
        None
    """

    # Train the model on the training data
    X_train = train_data[['Price', 'RSI']].values
    y_train = train_data['Label']

    # Optimize hyperparameters if they are not already optimized
    hyperParameterOptimize(X_train, y_train)

    model.fit(X_train, y_train)

    # Test the model on the testing data
    X_test = test_data[['Price', 'RSI']].values
    y_test = test_data['Label']
    y_pred = model.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = model.score(X_test, y_test)

    # Print the accuracy of the model
    print('Accuracy:', accuracy)

    # Print the predicted price direction for the next day
    last_price = df['Price'].iloc[-1]
    last_rsi = df['RSI'].iloc[-1]
    next_price = model.predict([[last_price, last_rsi]])[0]

    print('Next day price direction:', 'up' if next_price == 1 else 'down')
