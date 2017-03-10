from datetime import date

def assign_weights(start_year,end_year,time_period,stock_symbols):
    """
    obtainig weights from user for each timeperiod

    Parameters
    ----------
    start_year : Starting year
    end_year : Ending year
    stock_symbols : Ticker symbol of stocks
    time_period : weekly, monthly, quarterly, yearly

    Returns
    -------
    Weights for every stocks in each time_period
    """
    start_year = start_year.date()
    end_year = end_year.date()
    date_difference = end_year - start_year
    number_of_days = date_difference.days


    if time_period == "W":
        number_of_weights = int(number_of_days/7)
    elif time_period == "M":
        number_of_weights = int(number_of_days/30)
    elif time_period == "Q":
        number_of_weights = int(number_of_days/91)
    elif time_period == "A":
        number_of_weights = int(number_of_days/365)

    weights = {}
    # for each TICKER symbol in stocks
    for symbol in stock_symbols:
        temp = []
        for period in range(number_of_weights):
            weight = input("enter the weight for {} in time_period {} :".format(symbol,period+1))
            temp.append(int(weight))
        weights[symbol] = temp

    return weights
