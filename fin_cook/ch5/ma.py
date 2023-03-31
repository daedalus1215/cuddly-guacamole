import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import talib

df = yf.download("IBM",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

# calculate and plot the SMA
df["sma_20"] = talib.SMA(df["Close"], timeperiod=20)
df[["Close", "sma_20"]].plot(title="20-day simple moving average (SMA)")

plt.show()
