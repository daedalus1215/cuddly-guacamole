import pandas as pd
import yfinance as yf
import cufflinks as cf
from plotly.offline import iplot, init_notebook_mode
import plotly.express as px
import pandas_bokeh
from plotly.offline import iplot
import plotly.io as pio

pio.renderers.default = "notebook"
init_notebook_mode(connected=True)
cf.go_offline()
pandas_bokeh.output_notebook()

# 2.  load Microsoft’s stock prices from 2020 and calculate simple
df = yf.download(
    "MSFT", start="2020-01-01", end="2020-12-31", auto_adjust=False, progress=False
)

df["simple_rtn"] = df["Adj Close"].pct_change()
df = df.loc[:, ["Adj Close", "simple_rtn"]].dropna()
df = df.dropna()

# 3. Create the plot using cufflinks:
df.iplot(subplots=True, shape=(2, 1), shared_xaxes=True, title="MSFT time series")

# 4. Create the plot using bokeh:
df["Adj Close"].plot_bokeh(kind="line", rangetool=True, title="MSFT time series")
fig = px.line(data_frame=df, y="Adj Close", title="MSFT time series")
fig.show()
