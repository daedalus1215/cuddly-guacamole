import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import scipy.stats as scs
import statsmodels.api as sm
import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

# Preposition everything
df = yf.download("^GSPC",
                 start="2000-01-01",
                 end="2020-12-31",
                 progress=False)
df = df[["Adj Close"]].rename(
    columns={"Adj Close": "adj_close"}
)

# Investigate the existence of the leverage effect in the S&P 500's return

df["log_rtn"] = np.log(df["adj_close"] / df["adj_close"].shift(1))
df = df[["adj_close", "log_rtn"]].dropna()

# Calculate volatility measures as moving standard deviations:
df["moving_std_252"] = df[["log_rtn"]].rolling(window=252).std()
df["moving_std_21"] = df[["log_rtn"]].rolling(window=21).std()

fig, ax = plt.subplots(3, 1, figsize=(18, 15), sharex=True)
df["adj_close"].plot(ax=ax[0])
ax[0].set(title="S&P 500 time series", ylabel="Price ($)")

df["log_rtn"].plot(ax=ax[1])
ax[1].set(ylabel="Log returns")

df["moving_std_252"].plot(ax=ax[2], color="r", label="Rolling volatility 252d")
df["moving_std_21"].plot(ax=ax[2], color="g", label="Rolling volatility 21d")
ax[2].set(ylabel="Moving volatility", xlabel="Date")
ax[2].legend()

plt.show()
# We can investigate the leverage effect by visually comparing the price series to the rolling (volatility metric)
# In these 3 charts we can observe a pattern of increased volatility when the prices go down and decreased volatility when they are rising. This observation is in line with the fact's definition.
