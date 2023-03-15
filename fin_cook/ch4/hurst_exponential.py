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

# Initial take a look at the S&P
# plt.show()


# define a function calculating the Hurst exponential
def get_hurst_exponent(ts, max_lag=20):
    """Returns the Hurst exponent of the time series. The max_lag will greatly impact the results
    results can vary depending on: 1. method we use for calculating the Hurst exponent; 2. the value of the max_lag
    parameter; 3. the period we are looking at - local patterns can be very diff from the global ones.
    """
    lags = range(2, max_lag)
    tau = [np.std(np.subtract(ts[lag:], ts[:-lag])) for lag in lags]
    hurst_exp = np.polyfit(np.log(lags), np.log(tau), 1)[0]
    return hurst_exp

# Calculate the values of the Hurst exponent using diff values for the max_lag parameter
for lag in [20, 100, 250, 500, 1000]:
    hurst_exp = get_hurst_exponent(df["Adj Close"].values, lag)
    print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")

# The more lags we include, the closer we get to the verdict that the S&P 500 series is a random walk

# Narrow down the data to the years 2005 to 2007 and calculate the exponents one more time
shorter_series = df.loc["2005":"2007", "Adj Close"].values
for lag in [20, 100, 250, 500]:
    hurst_exp = get_hurst_exponent(shorter_series, lag)
    print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")
