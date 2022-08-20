from ast import If
import alpaca_trade_api as api
import config



alpaca = api.REST(config.API_KEY, config.API_SECRET, config.BASE_URL)

account = alpaca.get_account()
asset = alpaca.get_asset("BTC/USD")
clock = alpaca.get_clock()
print(account.cash)
print(asset)
if (clock.is_open == True):
    print("Market is open")
else:
    print("Market is closed")