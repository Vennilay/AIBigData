import pandas as pd
import matplotlib.pyplot as plt

try:
    import yfinance as yf
except ImportError:
    raise SystemExit("install yfinance: pip install yfinance")

start = "2021-01-01"
end = "2021-12-31"

aapl = yf.download("AAPL", start=start, end=end, progress=False)["Adj Close"]
msft = yf.download("MSFT", start=start, end=end, progress=False)["Adj Close"]
goog = yf.download("GOOG", start=start, end=end, progress=False)["Adj Close"]

prices = pd.concat([aapl, msft, goog], axis=1)
prices.columns = ["AAPL", "MSFT", "GOOG"]

plt.plot(prices.index, prices["AAPL"], label="AAPL")
plt.plot(prices.index, prices["MSFT"], label="MSFT")
plt.plot(prices.index, prices["GOOG"], label="GOOG")
plt.legend()
plt.show()
