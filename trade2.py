from alpaca.trading.client import TradingClient
from rich.console import Console
import config

console = Console()

# paper=True enables paper trading
trading_client = TradingClient(config.API_KEY, config.API_SECRET, paper=True, raw_data=False)

account = trading_client.get_account()
open_pos = trading_client.get_open_position("BTCUSD")
all_open_pos = trading_client.get_all_positions()
clock = trading_client.get_clock()

print("\n")

if clock.is_open == True:
    console.print("The market is: ")
    console.print("Open", style="bold")
    console.print(clock.timestamp)
else:
    console.print("The market is Close")
    console.print(clock.next_close)
print("\n")

console.print("Current cash in account:", account.cash, "$")
console.print("Open Position: ", open_pos.symbol)
console.print("Quantity: ", open_pos.qty)
