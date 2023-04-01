import pandas as pd
import yfinance as yf
import talib
import mplfinance as mpf
import matplotlib.pyplot as plt
from IPython.display import display

df = yf.download("BTC-USD",
                 period="9mo",
                 interval="1h",
                 progress=False)

candle_names = talib.get_function_groups()["Pattern Recognition"]

# iterate over the list of patterns and try identifying them all
for candle in candle_names:
    df["candle"] = getattr(talib, candle)(df["Open"], df["High"], df["Low"], df["Close"])

with pd.option_context("display.max_rows", len(candle_names)):
    display(df[candle_names].describe().transpose().round(2))
