from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import kpss
import pandas as pd
import nasdaqdatalink
import matplotlib.pyplot as plt

df = (
    nasdaqdatalink.get(dataset="FRED/UNRATENSA",
                       start_date="2010-01-01",
                       end_date="2019-12-31")
        .rename(columns={"Value": "unemp_rate"})
)


def kpss_test(x, h0_type="c"):
    indices = ["Test Statistic", "p-value", "# of Lags"]

    kpss_test = kpss(x, regression=h0_type)
    results = pd.Series(kpss_test[0:3], index=indices)

    for key, value in kpss_test[3].items():
        results[f"Critical Value ({key})"] = value

    return results


print(kpss_test(df["unemp_rate"]))

# Null hypothesis of the KPSS test states that the time series is stationary. With a p-value of 0.01 (or a test
# statistic greater than the selected critical value), we have reasons to reject the null hypothesis in favor of the
# alternative one, indicating that the series is not stationary.

# Generate the ACF/PACF plots:

N_LAGS = 40
SIGNIFICANCE_LEVEL = 0.05

fig, ax = plt.subplots(2, 1)
plot_acf(df["unemp_rate"], ax=ax[0], lags=N_LAGS, alpha=SIGNIFICANCE_LEVEL)
plot_pacf(df["unemp_rate"], ax=ax[1], lags=N_LAGS, alpha=SIGNIFICANCE_LEVEL)

plt.show()
