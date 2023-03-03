import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL",
                 start="2010-01-01",
                 end="2020-12-31",
                 progress=False)
df = df.loc[:, ["Adj Close"]]

df["log_rtn"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))

def realized_volatility(x):
    return np.sqrt(np.sum(x**2))

# Calculate monthly realized volatility
df_rv = (
    df.groupby(pd.Grouper(freq="M"))
    .apply(realized_volatility)
    .rename(columns={"log_rtn": "rv"})
)

# Annualize the values:
df_rv.rv = df_rv["rv"] * np.sqrt(12)

# plot the results
fig, ax = plt.subplots(2,1,sharex=True)
ax[0].plot(df)
ax[0].set_title("Apple's log returns (2000-2012)")
ax[1].plot(df_rv)
ax[1].set_title("Annualized realized volatility")

plt.show()



