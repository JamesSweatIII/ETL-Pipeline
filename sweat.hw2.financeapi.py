import requests
import json
from datetime import date

# Get user input for stock ticker symbol
symbol = input("Enter stock ticker symbol: ")

# Send request to API to get stock information
url = "https://yfapi.net/v6/finance/quote"
querystring = {"symbols": symbol}
headers = {'x-api-key': "4su9PNd3RD77y8pmLw8r2866Hz6WCcBk8s7NmRgL"}
response = requests.request("GET", url, headers=headers, params=querystring)

# Check if API call was successful
if response.status_code != 200:
    print("Error: API call was not successful")
else:
    # Parse response as JSON
    company_info = json.loads(response.text)
    company = company_info['quoteResponse']['result'][0]['symbol']
    company_name = company_info['quoteResponse']['result'][0]['longName']


    # Check if stock exists
    if company is None:
        print("Error: Stock does not exist")
    else:
        url = "https://yfapi.net/v11/finance/quoteSummary/" + symbol + "?lang=en&region=US&modules=financialData"
        querystring = {"symbols": symbol}
        headers = {'x-api-key': "4su9PNd3RD77y8pmLw8r2866Hz6WCcBk8s7NmRgL"}
        response2 = requests.request("GET", url, headers=headers, params=querystring)

        # Parse response as JSON
        financials_data = json.loads(response2.text)

        # Extract relevant information

        current_price = financials_data["quoteSummary"]["result"][0]["financialData"]["currentPrice"]["raw"]
        target_mean_price = financials_data["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]["raw"]
        cash_on_hand = financials_data['quoteSummary']['result'][0]['financialData']['totalCash']['fmt']
        profit_margins = financials_data['quoteSummary']['result'][0]['financialData']['profitMargins']['fmt']

        # Create dictionary to store information
        stock_info = {
            "symbol": symbol,
            "company_name": company,
            "current_price": current_price,
            "target_mean_price": target_mean_price,
            "cash_on_hand": cash_on_hand,
            "profit_margin": profit_margins,
            "date_pulled": str(date.today())
        }

        # Store information as JSON
        with open("stock_info.json", "w") as outfile:
            json.dump(stock_info, outfile)

        # Print out information to user
        print(f"Name Ticker: {symbol}")
        print(f"Name Company: {company_name}")
        print(f"Current Price: {current_price}")
        print(f"Target Mean Price: {target_mean_price}")
        print(f"Cash on Hand: {cash_on_hand}")
        print(f"Profit Margins: {profit_margins}")
