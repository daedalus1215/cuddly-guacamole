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
(df["log_rtn"].plot(title="Daily S&P 500 returns", figsize=(10, 6)))
plt.show()