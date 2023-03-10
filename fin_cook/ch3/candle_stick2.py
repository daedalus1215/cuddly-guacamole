import plotly.graph_objects as go
import mplfinance as mpf
import pandas as pd
import yfinance as yf


df = yf.download(
    "TWTR", start="2018-01-01", end="2018-12-31", progress=False, auto_adjust=True
)

fig = go.Figure(
    data=go.Candlestick(
        x=df.index, open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"]
    )
)

fig.update_layout(title="Twitter's stock prices in 2018", yaxis_title="Price ($)")
fig.show()
