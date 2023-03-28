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

# create the autocorrelation function plot of log returns
acf = smt.graphics.plot_acf(df["log_rtn"], lags=N_LAGS, alpha=SIGNIFICANCE_LEVEL)

plt.show()

# only a few values lie outside the confidence interval (we do not look at lag 0) and can be considered
# statistically significant. We can assume that we have verified that there is no autocorrelation in the log returns
# series.
