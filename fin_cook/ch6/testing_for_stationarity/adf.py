from statsmodels.tsa.stattools import adfuller
import pandas as pd
import nasdaqdatalink

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

# Download the monthly US unemployment rate from the years 2010 to 2019:
df = (
    nasdaqdatalink.get(dataset="FRED/UNRATENSA",
                       start_date="2010-01-01",
                       end_date="2019-12-31")
        .rename(columns={"Value": "unemp_rate"})
)


# Test if the time series of monthly US unemployment rates is stationary:
def adf_test(x):
    """Audmented Dickey-Fuller (ADF) test"""
    indices = ["Test Statistic",
               "p-value",
               "# of Lags Used",
               "# of Observations used"]

    adf_test = adfuller(x, autolag="AIC")
    results = pd.Series(adf_test[0:4], index=indices)

    for key, value in adf_test[4].items():
        results[f"Critical Value ({key})"] = value

    return results

print(adf_test(df["unemp_rate"]))

# null hypothesis of the ADF test states that the time series is not stationary. With a p-value of 0.26 (or equivalently,
# the test statistic is greater than the cricial value for the selected confidence level), we have no reason to reject
# the null hypothesis, meaning that we can conclude that the series is not stationary.
