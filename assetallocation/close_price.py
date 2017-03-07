from pandas_datareader import data as web
import pandas as pd



def close_price(symbol, start, end):
    """
    Gets returns for a symbol.
    Queries Yahoo Finance

    Parameters
    ----------
    symbol : Ticker symbol, e.g. APPL.
    start : start date.
    end : end date.

    Returns
    -------
    Close price for the symbol.
    """

    # get close_price from yahoo
    close = get_symbol_from_yahoo(symbol, start, end)


    return close[symbol]


def get_symbol_from_yahoo(symbol, start, end):
    """
    Retrieves close prices for symbol from yahoo.

    Parameters
    ----------
    symbol : Symbol name to load, e.g. 'SPY'
    start : Start date.
    end : End date.

    Returns
    -------
    close price of symbol in requested period.
    """
    print start ,end
    px = web.get_data_yahoo(symbol, start=start, end=end)
    close = px[['Close']].dropna()
    # close.index = rets.index.tz_localize("UTC")
    close.columns = [symbol]

    print "close",close
    print type(close)

    return close
