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
plt.show()