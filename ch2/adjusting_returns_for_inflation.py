import nasdaqdatalink
import pandas as pd
import numpy as np
import yfinance as yf
import cpi

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

# df = nasdaqdatalink.get(dataset="WIKI/AAPL", start_date="2011-01-01", end_date="2021-12-31")


# DOwnload the data and keep the adjusted close prices only:
df = yf.download("AAPL",
                 start="2009-12-01",
                 end="2020-12-31",
                 progress=False)

df = df.loc[:, ["Adj Close"]]

# Resample daily prices to monthly:
df = df.resample("M").last()

# Download inflation data from Nasdaq Data Link:
df_cpi = (
    nasdaqdatalink.get(dataset="RATEINF/CPI_USA",
                       start_date="2009-12-01",
                       end_date="2020-12-31")
        .rename(columns={"Value": "cpi"})
)

df_cpi

# join inflation data to prices:
df = df.join(df_cpi, how="left")

# calculate simple returns and infaltion rate:
df["simple_rtn"] = df["Adj Close"].pct_change()
df["inflation_rate"] = df["cpi"].pct_change()

# Adjust the returns for inflation and calculate the real returns:
df["real_rtn"] = (
        (df["simple_rtn"] + 1) / (df["inflation_rate"] + 1) - 1
)

print(df)

# Obtain the default CPI series, of the default CPI index.
# ie, all items in US city average, all urban consumers, not seasonally adjusted

cpi_series = cpi.series.get()

df_cpi_2 = cpi_series.to.dataframe()

# Filter the Df and view the top 12 observations
# Anything from 2010 or above, in intervals of months, only keep 2 columns.
df_cpi_2.query("period_type == 'monthly' and year >= 2010") \
    .loc[:, ["date", "value"]] \
    .set_index("date") \
    .head(12)
