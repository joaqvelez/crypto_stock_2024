import yfinance as yf
import pandas as pd

# Tickers
sp500_ticker = '^GSPC'
nasdaq_ticker = '^IXIC'
tickers = ['TSLA', 'MSFT', 'NVDA', 'AMZN', 'GOOGL', 'META', 'V', 'AAPL']

# Download data for S&P 500 and NASDAQ
sp500_data = yf.download(sp500_ticker, start='2024-01-01', end='2024-06-24')
nasdaq_data = yf.download(nasdaq_ticker, start='2024-01-01', end='2024-06-24')

# Initialize the DataFrame
df = pd.DataFrame({
    'Date': sp500_data.index,
    'S&P 500': sp500_data['Close'],
    'NASDAQ': nasdaq_data['Close']
})

# Download data for additional tickers
for ticker in tickers:
    data = yf.download(ticker, start='2024-01-01', end='2024-06-24')
    df[ticker] = data['Close']

# Set the index
df.set_index('Date', inplace=True)

# Save to CSV
df.to_csv('yahoo_2024.csv')

print("CSV file has been saved.")
