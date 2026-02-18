import matplotlib.pyplot as plt
import yfinance as yf

tickers = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(tickers, start='2021-01-01', end='2021-12-31')
print(data)
adj_close = data['Close']

plt.figure(figsize = (12,6))
for ticker in tickers:
    plt.grid()
    plt.plot(adj_close.index, adj_close[ticker], label=ticker)

plt.legend()
plt.show()
