import requests

startDateHistory = '2011-01-01'
endDateHistory = '2023-02-27'

def getHistoricData():
    """
    Retrieves historical Bitcoin price data from an API.

    Returns:
        dict: A dictionary containing Unix timestamp keys and price values.
    """

    # Define the API endpoint and parameters
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    params = {'start': startDateHistory, 'end': endDateHistory}

    # Send a request to the API and get the response
    response = requests.get(url, params=params)

    # Extract the Bitcoin price data from the API response
    data = response.json()['bpi']

    # Return the Bitcoin price data as a dictionary
    return data

if __name__ == "__main__":
    data = getHistoricData()
    print(data)
