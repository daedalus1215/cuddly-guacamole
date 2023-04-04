import pandas as pd
import nasdaqdatalink
import seaborn as sns
import statsmodels.tsa.seasonal
import matplotlib.pyplot as plt

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

df = (
    nasdaqdatalink.get(dataset="FRED/UNRATENSA",
                       start_date="2010-01-01",
                       end_date="2019-12-31")
        .rename(columns={"Value": "unemp_rate"})
)

# print(df)

# fig, ax = plt.subplots()
# df.plot(ax=ax, title="US unemployment rate from the years 2010 to 2019")

statsmodels.tsa.seasonal.seasonal_decompose(df, model='additive').plot()
