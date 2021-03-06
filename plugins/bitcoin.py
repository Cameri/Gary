from util import http, hook


@hook.command('btc', autohelp=False)
@hook.command(autohelp=False)
def bitcoin(inp, say=None):
    """.bitcoin - Gets current exchange rate for bitcoins from BTC-E."""
    data = http.get_json("https://btc-e.com/api/2/btc_usd/ticker")
    ticker = data['ticker']
    say("Buy: \x0307${!s}\x0f - Sell: \x0307${!s}\x0f - High: \x0307${!s}\x0f - Low: \x0307${!s}\x0f - Volume: {!s} BTC".format(
            ticker['buy'], ticker['sell'], ticker['high'], ticker['low'], ticker['vol_cur']))


@hook.command('ltc', autohelp=False)
@hook.command(autohelp=False)
def litecoin(inp, say=None):
    """.litecoin - Gets current exchange rate for litecoins from BTC-E."""
    data = http.get_json("https://btc-e.com/api/2/ltc_usd/ticker")
    ticker = data['ticker']
    say("Buy: \x0307${!s}\x0f - Sell: \x0307${!s}\x0f - High: \x0307${!s}\x0f - Low: \x0307${!s}\x0f - Volume: {!s} LTC".format(
        ticker['buy'], ticker['sell'], ticker['high'], ticker['low'], ticker['vol_cur']))


@hook.command('dc', autohelp=False)
@hook.command('doge', autohelp=False)
@hook.command(autohelp=False)
def dogecoin(inp, say=None):
    """.dogecoin - Gets current exchange rate for dogecoins from BTER."""
    ticker = http.get_json("http://data.bter.com/api/1/ticker/doge_usd")
    say("Buy: \x0307${!s}\x0f - Sell: \x0307${!s}\x0f - High: \x0307${!s}\x0f - Low: \x0307${!s}\x0f - Volume: {!s} per 1000 DogeCoin".format(
             float(ticker['buy'])*1000, float(ticker['sell'])*1000, float(ticker['high'])*1000, float(ticker['low'])*1000, ticker['vol_doge']))
