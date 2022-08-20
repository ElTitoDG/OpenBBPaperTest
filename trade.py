import alpaca_trade_api as api
import config

alpaca = api.REST(config.API_KEY, config.API_SECRET, config.BASE_URL)

account = alpaca.get_account()
asset = alpaca.get_asset("BTC/USD")
clock = alpaca.get_clock()
position = alpaca.get_position("ETHUSD")

print("\n")
print(account.cash)
print(asset.symbol, asset.exchange)
print(position.unrealized_pl)
print("\n")

if clock.is_open is True:
    print("Market is open")
else:
    print("Market is closed")
