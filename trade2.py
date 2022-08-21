from alpaca.trading.client import TradingClient
import config

# paper=True enables paper trading
trading_client = TradingClient(config.API_KEY, config.API_SECRET, paper=True)

#account = trading_client.get_account()
account = trading_client.get_account()

print(account)
