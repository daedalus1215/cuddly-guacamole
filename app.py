import pandas as pd
import yfinance as yf


df = yf.download("AAPL",
                 start="2011-01-01",
                 end="2021-12-31",
                 progress=False)

print(f"Downloaded {len(df)} rows of data.")
print(df)

aapl_data = yf.Ticker("AAPL")

aapl_data.history()