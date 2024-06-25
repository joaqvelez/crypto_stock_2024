import yfinance as yf
import pandas as pd

sp500_ticker = '^GSPC'
nasdaq_ticker = '^IXIC'

sp500_data = yf.download(sp500_ticker, start='2024-01-01', end='2024-06-24')
nasdaq_data = yf.download(nasdaq_ticker, start='2024-01-01', end='2024-06-24')

df = pd.DataFrame({
    'Date': sp500_data.index,
    'S&P 500': sp500_data['Close'],
    'NASDAQ': nasdaq_data['Close']
})

df.set_index('Date', inplace=True)

df.to_csv('yahoo_sp500_nasdaq_2024.csv')

print("CSV file has been saved.")
