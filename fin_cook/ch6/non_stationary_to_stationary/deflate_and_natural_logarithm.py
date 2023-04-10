import pandas as pd
import numpy as np
import nasdaqdatalink
import cpi
from datetime import date, time
import matplotlib.pyplot as plt
from chapter_6_utils import test_autocorrelation

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

df = (
    nasdaqdatalink.get(dataset="WGC/GOLD_MONAVG_USD",
                       start_date="2000-01-01",
                       end_date="2010-12-31")
        .rename(columns={"Value": "price"})
        .resample("M")
        .last()  # just get the last date of the month, def ensures we get no dups
)

# Deflate the gold prices to the 2010-12-31 USD values and plot the results
# Can adjust the gold prices to another point in time, as long as it is the same point for the entire series.
DEFL_DATE = date(2010, 12, 31)

df["dt_index"] = pd.to_datetime(df.index)
df["price_deflated"] = df.apply(
    lambda x: cpi.inflate(x["price"], x["dt_index"], DEFL_DATE),
    axis=1
)
(
    df.loc[:, ["price", "price_deflated"]]
        .plot(title="Gold Price (deflated) to 2010 prices")
)

# Apply the natural logarithm to the deflated series and plot it together with the rolling metrics:
WINDOW = 12
selected_columns = ["price_log", "rolling_mean_log", "rolling_std_log"]

df["price_log"] = np.log(df.price_deflated) # iron out any appeared exponential trend into linear.
df["rolling_mean_log"] = df.price_log.rolling(WINDOW).mean()
df["rolling_std_log"] = df.price_log.rolling(WINDOW).std()
(
    df[selected_columns].plot(title="Gold Price (deflated + logged)", subplots=True)
)

### Are we stationary?
fig = test_autocorrelation(df["price_log"])
### ACF/PACF plots indicate that we are not stationary enough


# Apply differencing to the series and plot the results
selected_columns_diff = ["price_log_diff", "roll_mean_log_diff", "roll_std_log_diff"]
df["price_log_diff"] = df.price_log.diff(1)
df["roll_mean_log_diff"] = df.price_log_diff.rolling(WINDOW).mean()
df["roll_std_log_diff"] = df.price_log_diff.rolling(WINDOW).std()
df[selected_columns_diff].plot(title="Gold Price (deflated + log + diff)")
df[selected_columns_diff].plot()
# The transformed gold prices give the impression of being stationary - the series oscillates around 0 with no visible
# trend and approximately constant variance.

# Test if time series is finally stationary
fig = test_autocorrelation(df["price_log_diff"].dropna())

plt.show()
