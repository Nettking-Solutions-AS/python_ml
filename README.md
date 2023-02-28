# BTC Predict
This is a Python project that uses machine learning to predict the direction of Bitcoin prices.

## Overview
Bitcoin prices are notoriously difficult to predict, with frequent and dramatic fluctuations that make it challenging to forecast future price movements. This project aims to address this challenge by using machine learning algorithms to analyze historical Bitcoin price data and identify patterns that can be used to predict future price movements.

###### The project consists of several Python scripts that perform various tasks, including:

-Retrieving historical Bitcoin price data from the Coindesk API <br />
-Converting the data to a pandas dataframe <br />
-Adding technical indicators (such as RSI) to the dataframe <br />  
-Labeling the data with the direction of price movements <br />
-Splitting the data into training and testing sets <br />
-Creating a Random Forest classifier to predict price movements <br />
-Optimizing the hyperparameters of the classifier using grid search cross-validation <br />
-Training and testing the classifier on the data <br />
-Outputting the predicted price direction for the next day <br />

The project is designed to be modular and extensible, with each script performing a specific task that can be easily modified or replaced as needed.

## Getting started
To get started with the project, you'll need to clone the repository and install the required packages:<br />
<br />

git clone https://github.com/your-username/btc-predict.git<br />
cd btc-predict<br />
pip install -r requirements.txt<br />

You can then run the run.py script to retrieve the historical data and train the machine learning model:<br />
python run.py
