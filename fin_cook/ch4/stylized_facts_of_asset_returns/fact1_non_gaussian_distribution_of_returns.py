import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import scipy.stats as scs
import statsmodels.api as sm
import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

# Preposition everything
df = yf.download("^GSPC",
                 start="2000-01-01",
                 end="2020-12-31",
                 progress=False)
df = df[["Adj Close"]].rename(
    columns={"Adj Close": "adj_close"}
)
df["log_rtn"] = np.log(df["adj_close"] / df["adj_close"].shift(1))
df = df[["adj_close", "log_rtn"]].dropna()

# Calculate the normal probability density function (PDF) using the mean and standard deviation of the observed returns:
r_range = np.linspace(min(df["log_rtn"]), max(df["log_rtn"]), num=1000)
mu = df["log_rtn"].mean()
sigma = df["log_rtn"].std()
norm_pdf = scs.norm.pdf(r_range, loc=mu, scale=sigma)

# Plot the histogram and the Q-Q plot:
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# histogram
sns.distplot(df.log_rtn, kde=False, norm_hist=True, ax=ax[0])
ax[0].set_title("Distribution of S&P 500 returns", fontsize=16)
ax[0].plot(r_range, norm_pdf, "g", lw=2,
           label=f"N{mu:.2f}, {sigma**2:.4f}")
ax[0].legend(loc="upper left")

# Q-Q plot
qq = sm.qqplot(df.log_rtn.values, line="s", ax=ax[1])
ax[1].set_title("Q-Q plot", fontsize=16)

plt.show()

