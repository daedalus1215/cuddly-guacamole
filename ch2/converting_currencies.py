import pandas as pd
import yfinance as yf
from forex_python.converter import CurrencyRates

df = yf.download("AAPL",
                 start="2020-01-01",
                 end="2020-01-31",
                 progress=False)
df = df.drop(columns=["Adj Close", "Volume"])
# Instantiate the Currency Rate Object
c = CurrencyRates()

[print(date) for date in df.index if date.weekday() < 5]
# Download the USD/EUR rate for each required date:
# Warning, this is not performant. We are grabbing the rates for each date individually upon demand.
df["usd_eur"] = [c.get_rate("USD", "EUR", date) for date in df.index if date.weekday() < 5]
# Convert the price from USD to EUR:
for column in df.columns[:-1]:
    df[f"{column}_EUR"] = df[column] * df["usd_eur"]

print(df.head())