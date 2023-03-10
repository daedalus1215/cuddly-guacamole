import plotly.graph_objects as go
import mplfinance as mpf
import pandas as pd
import yfinance as yf


import cufflinks as cf
from plotly.offline import iplot
cf.go_offline()



df = yf.download(
    "TWTR", start="2018-01-01", end="2018-12-31", progress=False, auto_adjust=True
)

qf = cf.QuantFig(
df, title="Twitter's Stock Price",
legend="top", name="Twitter's stock prices in 2018"
)

qf.add_volume()
qf.add_sma(periods=20, column="Close", color="red")
qf.add_ema(periods=20, color="green")

qf.iplot()


fig = go.Figure(
    data=go.Candlestick(
        x=df.index, open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"]
    )
)

fig.update_layout(title="Twitter's stock prices in 2018", yaxis_title="Price ($)")
fig.show()
