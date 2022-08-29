from alpaca.trading.client import TradingClient
import config

# paper=True enables paper trading
trading_client = TradingClient(config.API_KEY, config.API_SECRET, paper=True)

account = trading_client.get_account()
open_pos = trading_client.get_open_position("BTCUSD")
all_open_pos = trading_client.get_all_positions()

print("Current cash in account:", account.cash, "$")
print("Open Position: ", open_pos.symbol)
print("Quantity: ", open_pos.qty)
