import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("IBM",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

# Calculate and plot the Bollinger Bands
df["tp"] = (df["Close"] + df["Low"] + df["High"]) / 3
df["std"] = df["Close"].rolling(20).std(ddof=0)
df["bolu"] = df["sma_20"] + 2 * df["std"]
df["bold"] = df["sma_20"] - 2 * df["std"]
# calculate and plot the SMA
df["sma_20"] = df["Close"].rolling(20).mean()

fig, ax = plt.subplots()
df[["sma_20", "Close", "bolu", "bold"]].plot(ax=ax, color=["blue", "purple", "yellow", "green"], title="Bollinger Bands")
ax.fill_between(df.index, df["bold"], df["bolu"], color="gray", alpha=.4)
plt.show()

