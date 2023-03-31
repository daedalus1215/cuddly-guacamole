import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("IBM",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

# calculate and plot the SMA

df["sma_20"] = df["Close"].rolling(window=20).mean()

fig, ax = plt.subplots()
df[["sma_20"]].plot(ax=ax, title="20-day Simple Moving Average (SMA)")

plt.show()

# Calculate and plot the Bollinger Bands