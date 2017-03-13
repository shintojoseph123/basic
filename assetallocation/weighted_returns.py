# customised imports
from obtain_data import close_price_data
from portfolio_profit import portfolio_profit
from utilities import returns,time_period_number,normalise
from plots import weighted_returns_plot


# importing libraries
import numpy as np
import pandas as pd


def weighted_returns(start_year, end_year, input_price, stock_symbols, weights, time_period,close_price):
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

    # # obtainig close_price_data data
    # close_price = close_price_data(start_year, end_year, stock_symbols, time_period)
    # print ("close_price",close_price)

    # ATHIRAS CHANGE
    close_price = close_price
    print ("close_price",close_price)




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
