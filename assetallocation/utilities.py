from datetime import date


def stocks(number_of_stocks):

    stocks = []
    for i in range(number_of_stocks):
        symbol = raw_input("enter the symbol for stock {}".format(i+1))
        stocks.append(symbol)

    return stocks


def returns(close_price, stock_symbols):
    returns = {}
    for symbol in stock_symbols:
        returns[symbol] = close_price[symbol].pct_change(1)

    return returns



def time_period_number(start_year,end_year,time_period):
    """
    obtainig data from yahoo finance

    Parameters
    ----------
    start_year : Starting year
    end_year : Ending year
    time_period : weekly, monthly, quarterly, yearly

    Returns
    -------
    How many time periods are between the dates
    """
    start_year = start_year.date()
    end_year = end_year.date()
    date_difference = end_year - start_year
    number_of_days = date_difference.days


    if time_period == "W":
        time_period_number = int(number_of_days/7)
    elif time_period == "M":
        time_period_number = int(number_of_days/30)
    elif time_period == "Q":
        time_period_number = int(number_of_days/91)
    elif time_period == "A":
        time_period_number = int(number_of_days/365)

    return time_period_number

def normalise(input_list,norm):
    
    norm = norm
    input_list = input_list

    for i in range(len(input_list)):
        push = (1+input_list[i])*norm
        norm = push
        input_list[i] = push

    return input_list
