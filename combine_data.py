import pandas as pd

binance = pd.read_csv('binance_2024.csv', index_col='Date', parse_dates=True)
yahoo = pd.read_csv('yahoo_2024.csv', index_col='Date', parse_dates=True)

final_combined_df = binance.join(yahoo, how='outer')
final_combined_df.to_csv('data_2024.csv')
