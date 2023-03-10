from datetime import date

import pandas as pd
import yfinance as yf
import numpy as np
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, curdoc

# import cufflinks as cf
# from plotly.offline import iplot, init_notebook_mode
# import plotly.express as px
# import pandas_bokeh
# from bokeh.io import output_notebook
# from bokeh.resources import INLINE
#
# output_notebook(INLINE)
#
# cf.go_offline()
# pandas_bokeh.output_notebook()
#
# # 2.  load Microsoft’s stock prices from 2020 and calculate simple
df = yf.download(
    "MSFT", start="2020-01-01", end="2020-12-31", auto_adjust=False, progress=False
)
#
df["simple_rtn"] = df["Adj Close"].pct_change()
df = df.loc[:, ["Adj Close", "simple_rtn"]].dropna()
df = df.dropna()
df = date(df["Date"])
print(df)
#
# # 3. Create the plot using cufflinks:
# df.iplot(subplots=True, shape=(2, 1), shared_xaxes=True, title="MSFT time series")
#
# # 4. Create the plot using bokeh:
# df["Adj Close"].plot_bokeh(kind="line", rangetool=True, title="MSFT time series")
# fig = px.line(data_frame=df, y="Adj Close", title="MSFT time series")
# fig.show()

source = ColumnDataSource(data=df)
p = figure()
p.line(x="Date", y="Adj Close", source=source)
show(p)
