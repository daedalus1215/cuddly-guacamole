import yfinance as yf
import kats.detectors.cusum_detection import CUSUMDetector
from kats.const import TimeSeriesData

df = yf.download("AAPL",
                 start="2020-01-01",
                 end="2020-12-31",
                 progress=False)

# Keey only the adjusted close price, reset the index, and rename the columns:
df = df[["Adj Close"]].reset_index(drop=False)
df.columns = ["time", "price"]

# Convert the DataFrame into a TimeSeriesData object
tsd = TimeSeriesData(df)

# Instantiate and run the changepoint detector:
cusum_detector = CUSUMDetector(tsd)
change_points = cusum_detector.detector(
    change_directions=["increase"]
)
cusum_detector.plot(change_points)
