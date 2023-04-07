import pandas as pd
import nasdaqdatalink
import seaborn as sns
import statsmodels.tsa.seasonal as seasonal
import matplotlib.pyplot as plt

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

# Download the monthly US unemployment rate from the years 2010 to 2019:
df = (
    nasdaqdatalink.get(dataset="FRED/UNRATENSA",
                       start_date="2010-01-01",
                       end_date="2019-12-31")
        .rename(columns={"Value": "unemp_rate"})
)

# Add rolling mean and standard deviation
WINDOW_SIZE = 12
df["rolling_mean"] = df["unemp_rate"].rolling(window=WINDOW_SIZE).mean()
df["rolling_std"] = df["unemp_rate"].rolling(window=WINDOW_SIZE).std()

fig, ax = plt.subplots()

df.plot(ax=ax, title="Unemployment rate")
# plt.show()

# From the trend we can infer that there is a linear pattern. Therefore, we will use additive decomposition in the next step:

decomposition_results = seasonal.seasonal_decompose(df["unemp_rate"], model="additive")
(decomposition_results.plot().suptitle("Additive Decomposition"))
plt.show()

# "We can see the extracted component series: trend, seasonal, and random (residual). To evaluate whether the decomp
# makes sense, we can look at the random component. If there is no discernible pattern (in other words, the random
# component is indeed random and behaves consistently over time), then the fit makes sense. In this case, it looks
# like the variance in the residuals is slightly higher in the first half of the dataset. This can indicate that a
# constant seasonal pattern is not good enough to accurately capture the seasonal component of the analyzed time series."

# It could also indicate that the data is not stationary.