import pandas as pd
import nasdaqdatalink
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
from statsmodels.graphics.tsaplots import month_plot, quarter_plot
import plotly.express as px

nasdaqdatalink.read_key(filename="/data/nasdaqdatalinkkey")

df = nasdaqdatalink.get(
    "FRED/UNRATENSA", start_date="2014-01-01", end_date="2019-12-31"
).rename(columns={"Value": "unemp_rate"})
# fig, ax = plt.subplots(1, 1, sharex=True)
df.plot(title="Unemployment rate in years 2014-2019")
# plt.show()

# create new columns with year and month
df["year"] = df.index.year
df["month"] = df.index.strftime("%b")

sns.lineplot(
    data=df,
    x="month",
    y="unemp_rate",
    hue="year",
    style="year",
    legend="full",
    palette="colorblind",
)
plt.title("Unemployment rate - Seasonal plot")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
# plt.show()

# Create a month plot:
month_plot(df["unemp_rate"], ylabel="Unemployment rate (%)")
plt.title("Unemployment rate - Month plot")

# Create a quarter plot:
quarter_plot(df["unemp_rate"].resample("Q").mean(), ylabel="Unemployment rate (%)")
plt.title("Unemployment rate - Quarter plot")
plt.show()

# Create a polar seasonal plot using plotly.express:
fig = px.line_polar(
    df,
    r="unemp_rate",
    theta="month",
    color="year",
    line_close=True,
    title="Unemployment rate - Polar seasonal plot",
    width=600,
    height=500,
    range_r=[3, 7],
)
fig.show()
