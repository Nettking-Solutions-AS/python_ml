import requests
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Define the API endpoint and parameters
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
params = {'start': '2011-01-01', 'end': '2023-02-27'}

# Send a request to the API and get the response
response = requests.get(url, params=params)
data = response.json()['bpi']

# Convert the data to a pandas dataframe
df = pd.DataFrame.from_dict(data, orient='index', columns=['Price'])
df['PriceDiff'] = df['Price'].diff()
df['Label'] = (df['PriceDiff'] > 0).astype(int)

# Split the data into training and testing sets
train_data = df.loc['2011-01-01':'2021-12-31']
test_data = df.loc['2022-01-01':'2023-02-27']

# Create the machine learning model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
X_train = train_data['Price'].values.reshape(-1, 1)
y_train = train_data['Label']
model.fit(X_train, y_train)

# Test the model on the testing data
X_test = test_data['Price'].values.reshape(-1, 1)
y_test = test_data['Label']
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = model.score(X_test, y_test)

# Print the accuracy of the model
print('Accuracy:', accuracy)

# Print the predicted price direction for the next day
last_price = df['Price'].iloc[-1]
next_price = model.predict(last_price.reshape(1, -1))[0]
print('Next day price direction:', 'up' if next_price == 1 else 'down')
