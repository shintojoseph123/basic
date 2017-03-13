# customised imports
from obtain_data import close_price_data
from portfolio_profit import portfolio_profit
from utilities import returns,time_period_number,normalise

# importing libraries
import numpy as np
import pandas as pd


def weighted_returns(input_price, time_period_num, close_price, portfolio_profits):
    """
    function to find the returns of equal weighted portfolio and plot it

    Parameters
    -----------
    input_price : amount to buy the stocks
    time_period_num : number of time_periods
    close_price : close price at each time_period
    portfolio_profits : profits of portfolio at each time_period
    """

    portfolio_returns = []

    # create a portfolio_prices list to store all the portfolio_profits with first input price as its first
    portfolio_prices = [input_price]

    # until the end of timeperiod
    for i in range(time_period_num):

        # obtain portfolio_profit at each time_period
        portfolio_profit = portfolio_profits[i]

        # add total profit with input price
        input_price = input_price + portfolio_profit

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

    return portfolio_returns
