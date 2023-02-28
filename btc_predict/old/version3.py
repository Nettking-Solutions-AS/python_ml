import requests
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Define the API endpoint and parameters
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
params = {'start': '2011-01-01', 'end': '2023-02-27'}

# Send a request to the API and get the response
response = requests.get(url, params=params)
data = response.json()['bpi']

# Convert the data to a pandas dataframe
df = pd.DataFrame.from_dict(data, orient='index', columns=['Price'])

# Add RSI to the dataframe
delta = df['Price'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
rsi = 100.0 - (100.0 / (1.0 + rs))
df['RSI'] = rsi.fillna(0)

# Add price direction label to the dataframe
df['PriceDiff'] = df['Price'].diff()
df['Label'] = (df['PriceDiff'] > 0).astype(int)

# Split the data into training and testing sets
train_data = df.loc['2011-01-01':'2021-12-31']
test_data = df.loc['2022-01-01':'2023-02-27']

# Create the machine learning model
model = RandomForestClassifier(n_estimators=400, max_depth=30, random_state=42,min_samples_split=10, n_jobs=14, max_features='log2')

# Train the model on the training data
X_train = train_data[['Price', 'RSI']].values
y_train = train_data['Label']
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

def hyp_para_op():
    # Define the range of hyperparameters to tune
    param_grid = {
        'n_estimators': [50, 100, 200, 500],
        'max_depth': [3, 5, 10, 20, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2']
    }

    # Create a Random Forest classifier
    rf = RandomForestClassifier()

    # Use grid search cross-validation to find the optimal hyperparameters
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=14)
    grid_search.fit(X_train, y_train)

    # Print the best hyperparameters
    print("Best hyperparameters: ", grid_search.best_params_)

    # Train the model with the best hyperparameters
    best_rf = RandomForestClassifier(**grid_search.best_params_)
    best_rf.fit(X_train, y_train)

    # Evaluate the model
    accuracy = best_rf.score(X_test, y_test)
    print("Accuracy:", accuracy)