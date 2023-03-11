import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download Tesla’s stock prices from 2019 to 2020 and calculate
df = yf.download("TSLA", start="2019-01-01", end="2020-12-31", progress=False)

df["rtn"] = df["Adj Close"].pct_change()
df = df[["rtn"]].copy()

# Calculate the 21-day rolling mean and standard deviation:
df_rolling = df[["rtn"]].rolling(window=21).agg(["mean", "std"])
df_rolling.columns = df_rolling.columns.droplevel()

# Join the rolling data back to the initial DataFrame
df = df.join(df_rolling)

# Calculate the upper and lower thresholds
N_SIGMAS = 3 # use 3 standard deviations as our accepted border, anything outside that will be considered an outlier
df["upper"] = df["mean"] + N_SIGMAS * df["std"]
df["lower"] = df["mean"] - N_SIGMAS * df["std"]

# Identify the outliers using the previously calculated thresholds
df["outlier"] = ((df["rtn"] > df["upper"]) | (df["rtn"] < df["lower"])) # ordinarily we should plug these values as well.
# Plot the returns together with the thresholds and mark the outliers:
fig, ax = plt.subplots()
df[["rtn", "upper", "lower"]].plot(ax=ax)
ax.scatter(df.loc[df["outlier"]].index, df.loc[df["outlier"], "rtn"], color="black", label="outlier")
ax.set_title("Tesla's stock returns")
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()
