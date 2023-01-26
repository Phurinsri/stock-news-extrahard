import requests


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_stock = "X64J1PIGPP49ESDN"

params_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": api_key_stock
}
response_stock = requests.get("https://www.alphavantage.co/query", params=params_stock)
response_stock.raise_for_status()

data_stock = response_stock.json()["Time Series (Daily)"]
data_stock_list = [value for (key, value) in data_stock.items()]
data_stock_close_yesterday = float(data_stock_list[0]["4. close"])
data_stock_close_before_yesterday = float(data_stock_list[1]["4. close"])

diff_price = abs(data_stock_close_yesterday - data_stock_close_before_yesterday)
percent = (diff_price / data_stock_close_yesterday) * 100
if data_stock_close_yesterday > data_stock_close_before_yesterday:
    up_down = f"🔺{percent}%"
elif data_stock_close_yesterday < data_stock_close_before_yesterday:
    up_down = f"🔻{percent}%"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
api_key_news = "e5cc4d2129ef47899385e66c20af82d9"
params_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": api_key_news
}
response_news = requests.get("https://newsapi.org/v2/everything", params=params_news)
response_news.raise_for_status()

data_news = response_news.json()["articles"][:3]


data_news_list = [f"Headline: {data['title']}. {up_down}.\nBrief: {data['description']}." for data in data_news]
for article in data_news_list:
    print(article)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
