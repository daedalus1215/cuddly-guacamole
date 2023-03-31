import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("IBM",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

# Calculate and plot the Bollinger Bands
close_delta = df['Close'].diff()

# make two series: one for lower closes and one for higher closes
up = close_delta.clip(lower=0)
down = -1 * close_delta.clip(upper=0)

periods = 14
# exponential moving average
# ma_up = up.ewm(com=periods-1, adjust=True, min_periods=periods).mean()
# ma_down = down.ewm(com=periods-1, adjust=True, min_periods=periods).mean()

# simple moving average
ma_up = up.rolling(window=periods).mean()
ma_down = down.rolling(window=periods).mean()

rsi = ma_up / ma_down
rsi = 100 - (100 / (1 + rsi))

fig, ax = plt.subplots()
df['Close'].plot(ax=ax, title="Relative Strength Index (RSI)")
# ax.hlines(y=30,
#           xmin=df.index.min(),
#           xmax=df.index.max(),
#           color="red")
# ax.hlines(y=70,
#           xmin=df.index.min(),
#           xmax=df.index.max(),
#           color="red")
plt.show()
