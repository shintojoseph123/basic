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
    px = web.get_data_yahoo(symbol, start=start, end=end)
    close = px[['Close']].dropna()
    close.columns = [symbol]


    return close[symbol]
