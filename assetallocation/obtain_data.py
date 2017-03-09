from close_price import close_price

def close_price_data(start_year, end_year, stock_symbols, time_period):
    """
    obtainig data from yahoo finance

    Parameters
    ----------
    start_year : Starting year of the stock data to be needed.
    end_year : Ending year of the stock data to be needed.
    stocks : Ticker symbol of stocks
    time_period : weekly, monthly, quarterly, yearly

    Returns
    -------
    Close price of symbol in requested period.
    """

    # initialising start date and end date
    start_date =  start_year
    end_date = end_year

    # creating dictionary to obtain close_price_data
    close_price_data = {}

    # for each TICKER symbol in stock
    for symbol in stock_symbols:
        # add TICKER symbol with .NS to obtain National Stock exchange TICKER symbol
        query = str(symbol)+".NS"

        # obtain all the close_price_data
        close_price_data[symbol] = close_price(query,start=start_date, end=end_date )

        # filter  close_price_data according to the time_period
        close_price_data[symbol] = close_price_data[symbol].resample(time_period).last()


    return close_price_data
