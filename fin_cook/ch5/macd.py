import pandas as pd
import talib
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("IBM",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

df["macd"], df["macdsignal"], df["macdhist"] = talib.MACD(df["Close"],
                                                          fastperiod=12,
                                                          slowperiod=26,
                                                          signalperiod=9
                                                          )

fig, ax = plt.subplots(2, 1, sharex=True)
(
    df[["macd", "macdsignal"]].plot(ax=ax[0], title="Moving Average Convergence Divergence (MACD)")
)

ax[1].bar(df.index, df["macdhist"].values, label="macd_hist")
ax[1].legend()

plt.show()
