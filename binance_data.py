import pandas as pd
import requests
from binance.client import Client
from datetime import datetime

client = Client()
url = "https://api.coingecko.com/api/v3/coins/markets"

parameters = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 20,
    'page': 1,
    'sparkline': False
}

response = requests.get(url, params=parameters)

data = response.json()

stablecoins = {'usdt', 'usdc', 'busd', 'dai', 'tusd', 'eurt', 'wbtc', 'weeth'}
filtered_data = [crypto for crypto in data if crypto['symbol'] not in stablecoins]

binance_symbols = [info['symbol'] for info in client.get_exchange_info()['symbols']]
filtered_data = [crypto for crypto in filtered_data if
                 f"{crypto['symbol'].upper()}USDT" in binance_symbols]

top_20_cryptos = filtered_data[:10]

symbols = [crypto['symbol'].upper() for crypto in top_20_cryptos]
print(symbols)


def get_historical_klines(symbol, interval, start_str, end_str=None):
    klines = client.get_historical_klines(symbol, interval, start_str, end_str)
    data = []
    for kline in klines:
        data.append({
            'Date': datetime.fromtimestamp(kline[0] / 1000).date(),
            'close': float(kline[4])
        })
    return pd.DataFrame(data)


start_date = "2024-01-03"
end_date = datetime.today().strftime('%Y-%m-%d')
interval = Client.KLINE_INTERVAL_1DAY

all_data = {}

for symbol in symbols:
    pair = f"{symbol}USDT"
    try:
        df = get_historical_klines(pair, interval, start_date, end_date)
        all_data[symbol] = df.set_index('Date')
    except Exception as e:
        print(f"No se pudieron obtener datos para {symbol}: {e}")

combined_df = pd.concat(all_data.values(), axis=1, keys=all_data.keys())
combined_df.columns = combined_df.columns.droplevel(1)

print(combined_df.head())

combined_df.to_csv('binance_2024.csv')
