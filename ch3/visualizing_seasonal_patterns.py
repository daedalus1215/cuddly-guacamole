import pandas as pd
import nasdaqdatalink
import seaborn as sns
import matplotlib.pyplot as plt

nasdaqdatalink.read_key(filename='/data/nasdaqdatalinkkey')

df = (
    nasdaqdatalink.get("FRED/UNRATENSA",
                       start_date="2014-01-01",
                       end_date="2019-12-31").rename(columns={"Value":"unemp_rate"})
)
fig, ax = plt.subplots(2, 1, sharex=True)
ax[0].plot(df)
plt.show()
