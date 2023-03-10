import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("MSFT", start="2020-01-01", end="2020-12-31", auto_adjust=False, progress=False )
df["simple_rtn"] = df["Adj Close"].pct_change()
df = df.dropna()

fig, ax = plt.subplots(2, 1, sharex=True)

df["Adj Close"].plot(ax=ax[0])
ax[0].set(title="MSFT time series",
          ylabel="Stock price ($)")
df["simple_rtn"].plot(ax=ax[1])
ax[1].set(ylabel="Return (%)")
plt.show()