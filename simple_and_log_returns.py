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

# pct_change = calculates the percentage change between the current and prior element (we can specify the number of
# lags, but for this specific case the default value of 1 suffices)
df["simple_rtn"] = df["Adj Close"].pct_change()

# To calc the log return, we use the log return formula. When dividing each elemebnt of the series by its lagged value,
# we used the shift method with a calue of 1 to access the prior element. In the end we took the natural logarithm of
# the divided values by using np.log func
df["log_rtn"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))

df.head()
print(df)