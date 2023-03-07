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

# define a function aggregating the raw trades of info into bars:
# Bars are great for
def get_bars(df, add_time=False):
    ohlc = df["price"].ohlc()
    vwap = (
        df.apply(lambda x: np.average(x["price"], weights=x["qty"]))
        .to_frame("time")
    )
    vol = df["qty"].sum().to_frame("vol")
    cnt = df["qty"].size().to_frame("cnt")
    if add_time:
        time = df["time"].last().to_frame("time")
        res = pd.concat([time, ohlc, vwap, vol, cnt], axis=1)
    else:
        res = pd.concat([ohlc, vwap, vol, cnt], axis = 1)
    return res

# get the time bars:
print('time bars')
df_grouped_time = df.groupby(pd.Grouper(key="time", freq="1min"))
time_bars = get_bars(df_grouped_time)
print(time_bars)

# get the tick bars:
print('tick bars')
bar_size = 50
df["tick_group"] = (
    pd.Series(list(range(len(df))))
    .div(bar_size)
    .apply(np.floor)
    .astype(int)
    .values
)
df_grouped_ticks = df.groupby("tick_group")
tick_bars = get_bars(df_grouped_ticks, add_time=True)
print(tick_bars)

# volume bars:
print("volume_bars")
bar_size = 1
df["cum_qrt"] = df["qty"].cumsum()
df["vol_group"] = (
    df["cum_qrt"]
    .div(bar_size)
    .apply(np.floor)
    .astype(int)
    .values
)
df_grouped_ticks = df.groupby("vol_group")
volume_bars = get_bars(df_grouped_ticks, add_time=True)
print(volume_bars)

# Dollar Bars
bar_size = 50000
df["cum_value"] = df["quoteQty"].cumsum()
df["value_group"] = (
    df
)