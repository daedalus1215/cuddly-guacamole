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
df["log_rtn"] = np.log(df["adj_close"] / df["adj_close"].shift(1))
df = df[["adj_close", "log_rtn"]].dropna()
# Define the parameters for creating the autocrrelation plots:
N_LAGS = 50
SIGNIFICANCE_LEVEL = 0.05

# Fourth Fact by creating the ACF plots of squared and absolute returns
fig, ax = plt.subplots(2, 1, figsize=(12, 10))
smt.graphics.plot_acf(df["log_rtn"] ** 2, lags=N_LAGS, alpha=SIGNIFICANCE_LEVEL, ax=ax[0])
ax[0].set(ylabel="Squared Returns", title="Autocorrelation Plots")
smt.graphics.plot_acf(np.abs(df["log_rtn"]), lags=N_LAGS, alpha=SIGNIFICANCE_LEVEL, ax=ax[1])
ax[1].set(ylabel="Absolute Returns", xlabel="Lag")

plt.show()

# We can observe the small and decreasing values of auto correlation for the squared and absolute returns, which are in
# line with the fourth stylzed fact.