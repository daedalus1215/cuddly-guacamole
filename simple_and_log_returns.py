import pandas as pd
import numpy as np
import yfinance as yf

# DOwnload the data and keep the adjusted close prices only:
df = yf.download("AAPL",
                 start="2010-01-01",
                 end="2020-12-31",
                 progress=False)

df = df.loc[:, ["Adj Close"]]

# Calculate the simple and log returns using the adjusted close prices:
df["simple_rtn"] = df["Adj Close"].pct_change()
df["log_rtn"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))

df.head()
print(df)