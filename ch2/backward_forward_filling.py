import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import nasdaqdatalink


nasdaqdatalink.read_key(filename="/data/nasdaqdatalinkkey")

# Get the inflation data
df = nasdaqdatalink.get(
    dataset="RATEINF/CPI_USA", start_date="2015-01-01", end_date="2020-12-31"
).rename(columns={"Value": "cpi"})

# introduce 5 missing values at random
np.random.seed(42)
rand_indices = np.random.choice(df.index, 5, replace=False)
df["cpi_missing"] = df.loc[:, "cpi"]
df.loc[rand_indices, "cpi_missing"] = np.nan
print(df.head())

# fill in the missing values using different methods:
for method in ["bfill", "ffill"]:
    df[f"method{method}"] = df[["cpi_missing"]].fillna(method=method)

print(df.loc[rand_indices].sort_index())
fig, ax = plt.subplots(3, 1, sharex=True)
# ax[0].plot(df["cpi_missing"])
# ax[0].set_title = "Different ways of filling missing values"
# ax[1].plot(df["methodbfill"])
# ax[1].set_title = "back fill"
# ax[2].plot(df["methodffill"])
# ax[2].set_title = "forward fill"

#
# print(
#     df.loc[:"2017-01-01"]
#     .drop(columns=["cpi_missing"])
#     .plot(title="Different ways of filling missing values")
# )
#
# Can use linear interpolation technique
df["method_interpolate"] = df[["cpi_missing"]].interpolate()
# print(df.loc[rand_indices]).sort_index()
# ax[2].plot(df["method_interpolate"])
ax[0].plot(df.loc[:, "cpi_missing"])
ax[0].set_title = "Different ways of filling missing values"
ax[1].plot(df.loc[:, "method_interpolate"])
ax[1].set_title = "method_interpolate"
plt.show()
