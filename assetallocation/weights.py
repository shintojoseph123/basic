from datetime import date

def assign_weights(time_period_num,stock_symbols):
    """
    obtainig weights from user for each timeperiod

    Parameters
    ----------
    stock_symbols : Ticker symbol of stocks
    time_period_num : number of time_periods
    Returns
    -------
    Weights for every stocks in each time_period
    """

    weights = {}
    # for each TICKER symbol in stocks
    for symbol in stock_symbols:
        temp = []
        for period in range(time_period_num):
            weight = input("enter the weight for {} in time_period {} :".format(symbol,period+1))
            temp.append(int(weight))
        weights[symbol] = temp

    return weights
