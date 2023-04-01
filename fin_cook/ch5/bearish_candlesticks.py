import pandas as pd
import yfinance as yf
import talib
import mplfinance as mpf
import matplotlib.pyplot as plt

df = yf.download("BTC-USD",
                 period="9mo",
                 interval="1h",
                 progress=False)

# identify the three strike pattern:
df["3_line_strike"] = talib.CDL3LINESTRIKE(
    df["Open"], df["High"], df["Low"], df["Close"]
)

# Locate and plot the bearish pattern
print(df[df["3_line_strike"] == -100].head())

mpf.plot(df["2022-07-24 22:00:00+00:00": "2022-07-25 10:00:00+00:00"], type="candle")
# Locate and p lot the bullish pattern
print(df[df["3_line_strike"] == 100])
# plt.show()