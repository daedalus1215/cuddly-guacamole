import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download("^GSPC",
                 start="2000-01-01",
                 end="2019-12-31",
                 progress=False)
df["Adj Close"].plot(title="S&P 500 (years 2000-2019)")
fig, ax = plt.subplots()
df[["Adj Close"]].plot(ax=ax)
plt.show()