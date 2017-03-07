

# customised imports
from obtain_data import close_price_data
from portfolio_profit import portfolio_profit
from utilities import returns
from plots import weighted_returns_plot


# importing libraries
import numpy as np






def weighted_returns(start_year, end_year, input_price, stock_symbols, weights, time_period):
    """
    function to find the returns of equal weighted portfolio and plot it

    Parameters
    ----------
    start_year : starting year from which stock data is to be obtained
    end_year : ending year of the stock data to be obtained
    input_price : amount to buy the stocks
    stock_symbols : TICKER symbol of each stocks
    weights : weights for each stock at each time_period

    """

    # obtaining list of normalised returns of all stocks
    # all_returns = stock_performance(start_year,end_year)
    all_returns = []

    # create a portfolio list to append all the inputs with profits with first input price as its first
    portfolio = [input_price]

    # initializing variables
    loop = 0
    beg = 0




    # obtainig quarterly_price data
    close_price = close_price_data(start_year, end_year, stock_symbols, time_period)
    print type(close_price)
    print close_price
    print "returns",returns(close_price, stock_symbols)
    ret = returns(close_price, stock_symbols)
    print "profit",ret['TCS'].diff()

    # obtaining Quarterly returns using obtain_data() function
    returns_dataframe = returns(close_price, stock_symbols)


    # quarterly_price_data = quarterly_price(start_year ,end_year)

    # finding total profit
    if loop == 0:

        # obtain total profit
        portfolio_ret = portfolio_profit(input_price, beg, close_price, weights, stock_symbols)
        print "portfolio_ret",portfolio_ret

        # add total profit with input price
        input_price = input_price + portfolio_ret[0]

        # append new input price to the portfolio list
        portfolio.append(input_price)

        # obtain number of quarters to the loop variable
        loop = portfolio_ret[1]

    # finding how many quarters for calculating multivariance
    quarters = loop

    # finding how many quarters and subtracting one as a loop executed above already
    loop = int((loop)-1)



    # until the end of quarter
    for i in range(loop):

        beg = beg + 1

        # obtain total profit
        portfolio_ret = portfolio_profit(input_price, beg, close_price, weights, stock_symbols)

        # add total profit with input price
        input_price = input_price + portfolio_ret[0]

        # append new input price to the portfolio list
        portfolio.append(input_price)



    # obtaining the TICKER symbols of the stocks
    # stock = stocks()

    # obtain quarterly data inorder to draw pyfolio cause pyfolio will draw only in a particular UTC format
    data = close_price[stock_symbols[0]]

    # assign the portfolio values to the above dataset
    for i in range(len(data)):
        data[i]=portfolio[i]

    # finding returns of portfolio
    data = data.pct_change(1)

    # plotting tearsheet of portfolio using pyfolio
    # pf.create_returns_tear_sheet(data)


    # changing to numpy array
    data = np.array(data)

    # create a list to store normalised portfolio returns
    norm_portfolio_returns = []
    for i in data:
        if np.isnan(i):
            i = float(0)
            norm_portfolio_returns.append(i)
        else:
            i = float(i)
            norm_portfolio_returns.append(i)



    # normalising to 100
    norm = 100
    for i in range(len(norm_portfolio_returns)):
        push = (1+norm_portfolio_returns[i])*norm
        norm = push
        norm_portfolio_returns[i] = push

    # append all the norm_portfolio_returns to all_returns
    all_returns.append(norm_portfolio_returns)

    # plotting weighted_returns
    weighted_returns_plot(stock_symbols, all_returns, time_period)
