import requests

startDateHistory = '2011-01-01'
endDateHistory = '2023-02-27'

def getHistoricData():
    # Define the API endpoint and parameters
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    params = {'start': startDateHistory, 'end': endDateHistory}

    # Send a request to the API and get the response
    response = requests.get(url, params=params)
    data = response.json()['bpi']
    return data

if __name__ == "__main__":
    data = getHistoricData()
    print(data)