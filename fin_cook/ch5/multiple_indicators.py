import pandas as pd
import talib
import yfinance as yf
import matplotlib.pyplot as plt
from ta import add_all_ta_features

df = yf.download("IBM",
                 start="2020-01-01",
                                                                                                                                     end="2020-12-31",
                 progress=False,
                 auto_adjust=True)

# discard all previous calculated indicators
df = df[["Open", "High", "Low", "Close", "Volume"]].copy()

# calculate all the technical indicators available in the ta library
df = add_all_ta_features(df,
                         open="Open",
                         high="High",
                         low="Low",
                         close="Close",
                         volume="Volume")

print(df)
