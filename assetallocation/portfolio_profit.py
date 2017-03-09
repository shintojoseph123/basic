
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
        quart_ret = close_price_dataframe[symbol].diff().fillna(0).T.tolist()

        # slicing to remove the first data from list ,ie:0
        quart_ret = quart_ret[1:]

        # taking the i position value
        profit = quart_ret[i]

        # find the total profit of stock
        tot_ret = number_of_stocks*profit

        # add all the profits to the all returns list
        each_stock_profit.append(tot_ret)

    # sum all the profits of all stocks
    portfolio_profit = sum(each_stock_profit)


    return portfolio_profit
