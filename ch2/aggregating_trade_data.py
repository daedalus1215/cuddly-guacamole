from binance import Client
import pandas as pd
import numpy as np
import json

# instantiate the binance client and download the last 500 BTCEUR trades:
def get_api_essentals(data):
    return data['api_key'], data['api_secret']

with open('../data/settings.json', 'r') as file:
    data = json.load(file)

api_key, api_secret = get_api_essentals(data)

client = Client(api_key=api_key, api_secret=api_secret, tld="us")
check = client.get_historical_trades(symbol="BTCUSD")
print(check)
# Process the downloaded trades into a pandas DataFrame
df = (pd.DataFrame(check).drop(columns=["isBuyerMaker", "isBestMatch"]))

df["time"] = pd.to_datetime(df["time"], unit="ms")
for column in ["price", "qty", "quoteQty"]:
    df[column] = pd.to_numeric(df[column])

print(df)