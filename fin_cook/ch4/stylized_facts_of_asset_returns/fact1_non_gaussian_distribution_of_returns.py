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

# First, specify the range over which we calculate the PDF by using np.linespace (set number of points to be 1000;
# generally the more points the smoother).
r_range = np.linspace(min(df["log_rtn"]), max(df["log_rtn"]), num=1000)
mu = df["log_rtn"].mean()
sigma = df["log_rtn"].std()
# calculate the PDF using the scs.norm.pdf func. Default args correspond to the standard normal distribution, that is,
# with zero mean and unit variance
norm_pdf = scs.norm.pdf(r_range, loc=mu, scale=sigma)

# Plot the histogram and the Q-Q plot:
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# histogram
# use sns.distplot while setting kde (which does not use the Gaussian kernel density estimate) and norm_hist
# (show density instead of count)
sns.distplot(df.log_rtn, kde=False, norm_hist=True, ax=ax[0])
ax[0].set_title("Distribution of S&P 500 returns", fontsize=16)
# to see the difference between our histogram and Gaussian distribution, we superimpose a line representing the PDF of
# the Gaussian distribution with the mean and standard deviation coming from the considered return series.
ax[0].plot(r_range, norm_pdf, "g", lw=2,
           label=f"N{mu:.2f}, {sigma**2:.4f}")

ax[0].legend(loc="upper left")

# Q-Q plot
# Use this func to plot theoretical and observed against each other.
# if the empirical distribution is normal, then the vast majority of the points will lie on the red line (Gaussian).
# However, if we see that this is not the case, as points on the left hand side of the plot are more negative (that
# is lower empirical quantiles are smaller) than expected in the case of the Gaussian distribution. This means that
# the left tail of the returns distribution is heavier than that of the Gaussian distribution. Analogical conclusions
# can be drawn about the right tailm which is heavier than under normality.
qq = sm.qqplot(df.log_rtn.values, line="s", ax=ax[1])
ax[1].set_title("Q-Q plot", fontsize=16)

plt.show()

# investigating this fact is essentially plotting a histogram by visualizing the distribution of return.

