import yfinance as yf
from sktime.transformations.series.outlier_detection import HampelFilter
import matplotlib.pyplot as plt

df = yf.download("TSLA",
                 start="2019-01-01",
                 end="2020-12-31",
                 progress=False)
df["rtn"] = df["Adj Close"].pct_change()

# Instantiate the HampelFilter class and use it for detecting the outliers:
hampel_detector = HampelFilter(window_length=10,
                               return_bool=True)
df["outlier"] = hampel_detector.fit_transform(df["Adj Close"])

# Plot Tesla's stock price and mark the outliers
fig, ax = plt.subplots()

df[["Adj Close"]].plot(ax=ax)
ax.scatter(df.loc[df["outlier"]].index,
           df.loc[df["outlier"], "Adj Close"],
           color="black",
           label="outlier")
ax.set_title("Tesla's stock price")
ax.legend(loc="center left", bbox_to_anchor=(1,0.5))
# plt.show()

# For comparison's sake, we can also apply the very same filter to the returns calculated using the adjusted close prices
df["outlier_rtn"] = hampel_detector.fit_transform(df["rtn"])
# We just need to fit the hampel filter to the new data (returns) and transform it to get the boolean flag
# Plot Tesla's daily returns and mark the outliers
fig, ax = plt.subplots()
df[["rtn"]].plot(ax=ax)
ax.scatter(df.loc[df["outlier_rtn"]].index,
           df.loc[df["outlier_rtn"], "rtn"],
           color="black", label="outlier")
ax.set_title("Tesla's stock returns")
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

# plt.show()

# Can investigate the overlap and see how many times they converge.
print(df.query("outlier == True and outlier_rtn == True"))
