import pandas as pd
import talib
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("IBM",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

df["rsi"] = talib.RSI(df["Close"])

fig, ax = plt.subplots()
df["rsi"].plot(ax=ax, title="Relative Strength Index (RSI)")

ax.hlines(y=30, xmin=df.index.min(), xmax=df.index.max(), color="red")
ax.hlines(y=70, xmin=df.index.min(), xmax=df.index.max(), color="red")

plt.show()