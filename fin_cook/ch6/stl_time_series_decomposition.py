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



stl_decomposition = seasonal.STL(df[["unemp_rate"]]).fit()
stl_decomposition.plot().suptitle("STL Decomposition")

plt.show()

