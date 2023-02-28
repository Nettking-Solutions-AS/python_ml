# BTC Predict
This is a Python project that uses machine learning to predict the direction of Bitcoin prices.

# Overview
Bitcoin prices are notoriously difficult to predict, with frequent and dramatic fluctuations that make it challenging to forecast future price movements. This project aims to address this challenge by using machine learning algorithms to analyze historical Bitcoin price data and identify patterns that can be used to predict future price movements.

The project consists of several Python scripts that perform various tasks, including:

-Retrieving historical Bitcoin price data from the Coindesk API
-Converting the data to a pandas dataframe
-Adding technical indicators (such as RSI) to the dataframe
-Labeling the data with the direction of price movements
-Splitting the data into training and testing sets
-Creating a Random Forest classifier to predict price movements
-Optimizing the hyperparameters of the classifier using grid search cross-validation
-Training and testing the classifier on the data
-Outputting the predicted price direction for the next day

The project is designed to be modular and extensible, with each script performing a specific task that can be easily modified or replaced as needed.

# Getting started
To get started with the project, you'll need to clone the repository and install the required packages:

git clone https://github.com/your-username/btc-predict.git
cd btc-predict
pip install -r requirements.txt

You can then run the run.py script to retrieve the historical data and train the machine learning model:
python run.py
