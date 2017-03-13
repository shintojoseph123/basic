# customised imports
from obtain_data import close_price_data
from portfolio_profit import portfolio_profit
from utilities import returns,time_period_number,normalise
from plots import weighted_returns_plot

# importing libraries
import numpy as np
import pandas as pd


"""this is a code to test weighted returns in another way"""


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
    time_period : weekly, monthly, quarterly, yearly
    """

    portfolio_returns = []

    # create a portfolio_prices list to store all the portfolio_profits with first input price as its first
    portfolio_prices = [input_price]

    # obtainig close_price_data data
    close_price = close_price_data(start_year, end_year, stock_symbols, time_period)

    # obtaining Quarterly returns using obtain_data() function
    returns_dataframe = returns(close_price, stock_symbols)

    # finding how many time_periods are there between start date and end date
    time_period_num = time_period_number(start_year, end_year, time_period)

    # until the end of timeperiod
    for i in range(time_period_num):

        # obtain total profit
        portfolio_profits = portfolio_profit(input_price, i, close_price, weights, stock_symbols)

        # add total profit with input price
        input_price = input_price + portfolio_profits

        # append new input price to the portfolio list
        portfolio_prices.append(input_price)

    # converting portfolio_prices into dataframe
    portfolio_prices = pd.DataFrame(portfolio_prices)

    # finding returns of portfolio_prices, changing the nan to 0
    portfolio_returns_dataframe = portfolio_prices.pct_change(1).fillna(0)

    # converting dataframe to list
    portfolio_returns_list = portfolio_returns_dataframe[0].values.tolist()

    # normalise portfolio_returns_list to 100
    norm_portfolio_returns = normalise(portfolio_returns_list,100)

    # append all the norm_portfolio_returns to portfolio_returns[]
    portfolio_returns.append(norm_portfolio_returns)

    # plotting weighted_returns
    weighted_returns_plot(stock_symbols, portfolio_returns, time_period)



import numpy as np
from utilities import returns
import pandas as pd

def portfolio_profit(input_price, i, close_price_data, weights, stock_symbols):
    """
    finds the total profit and number of quarters and returns a list

    Parameters
    ----------

    input_price : amount to buy the stocks
    i : variable to loop through
    close_price_data :close price data of particular period
    weights : weights for each stock at each time_period

    """

    # finding the number of stocks
    no_of_stocks = len(stock_symbols)

    # list to store all return values
    each_stock_profit = []

    # converting to dataframe
    close_price_dataframe = pd.DataFrame(close_price_data)


    # for each TICKER symbol in stock
    for symbol in stock_symbols:

        # obtaining the weights of stock for each quadrent
        weight = weights[symbol]

        # calculating each stock price
        each_stock_price = int((input_price)*weight[i])/no_of_stocks

        # calculating number of stocks can be buyied
        number_of_stocks = each_stock_price/int(close_price_data[symbol].iloc[i])

        # obtainig price data, finding the profit or loss, changing the nan to 0, converting dataframe to list
        stock_profit = close_price_dataframe[symbol].diff().fillna(0).T.tolist()

        # taking the i+1 position value
        profit = stock_profit[i+1]

        # find the total profit of stock
        tot_ret = number_of_stocks*profit

        # add all the profits to the all returns list
        each_stock_profit.append(tot_ret)

    # sum all the profits of all stocks
    portfolio_profit = sum(each_stock_profit)


    return portfolio_profit
