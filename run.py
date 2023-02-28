# Local libaries
from btc_predict import *


# Get historic data
data = getHistoricData()

# Save data to local file
writeToFile(data)

# Convert data to pandas dataframe
df = convertDataToDf(data)

# Add RSI to the dataframe
addRSIToDf(df)

# Add price direction label to the dataframe
addPriceDirectionLabel(df)

# Split dataframe into train and test data
train_data, test_data = splitData(df)

# Create the machine learning model
model = createMlModel()

# Train and test ML model
runModel(model, df, train_data, test_data)