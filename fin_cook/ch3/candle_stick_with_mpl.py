import plotly.graph_objects as go
import yfinance as yf
import mplfinance as mpf

df = yf.download(
    "TWTR", start="2018-01-01", end="2018-12-31", progress=False, auto_adjust=True
)

fig = go.Figure(data=go.Candlestick(x=df.index,
                                    open=df["Open"],
                                    high=df["High"],
                                    low=df["Low"],
                                    close=df["Close"])
                )

fig.update_layout(
    title="Twitter's stock prices in 2018",
    yaxis_title="Price ($)"
)

fig.show()
# mav argument to indicate 2 moving averages, 10- and 20-day ones.
mpf.plot(df, type="candle", mav=(10, 20), volume=True, style="yahoo", title="Twitter's stock prices in 2018", figsize=(8,4))
# Cannot add exponential varints atm

