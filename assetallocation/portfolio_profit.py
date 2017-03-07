
import numpy as np
from utilities import returns

def portfolio_profit(input_price, beg, close_price_data, weights, stock_symbols):
    """
    finds the total profit and number of quarters and returns a list

    Parameters
    ----------

    input_price : amount to buy the stocks
    beg : variable to loop through
    close_price_data :close price data of particular period
    weights : weights for each stock at each time_period

    """

    print "inside portfolio profit"
    # obtaining the TICKER symbols of the stocks
    # stock = stocks()

    # obtaining Quarterly returns of stock data
    returns_dataframe = returns(close_price_data, stock_symbols)

    # finding the number of stocks
    no_of_stocks = len(stock_symbols)



    # list to store all return values
    all_profits = []


    # for each TICKER symbol in stock
    for symbol in stock_symbols:
        print (symbol)
        # obtaining quarterly price data
        returns_dataframe[symbol] = close_price_data[symbol]

        # converting to numpy array for calculation
        data = np.array(close_price_data[symbol])

        # obtaining the weights of stock for each quadrent


#         print (loop)
#         print (weights)

        weight = weights[symbol]

        print ("weee",weight[beg])

        # calculating each stock price
        each_stock_price = int((input_price)*weight[beg])/no_of_stocks
        print ("each_stock_price",each_stock_price)

        # calculating number of stocks can be buyied
        number_of_stocks = each_stock_price/int(data[beg])

        # obtainig price data
        quart_ret = returns_dataframe[symbol]

        # filtering to obtain quarterly price data
        # quart_ret = quart_ret.resample('Q', how='last')


        # finding the profit or loss
        quart_ret = quart_ret.diff()


        # converting into numpy array
        data = np.array(quart_ret)

        #creating a list to convert numpy into a list of float of values
        val = []
        for i in data:
            if np.isnan(i):
                i = float(0)
                val.append(i)
            else:
                i = float(i)
                val.append(i)

        # slicing to remove the first data from list ,ie:0
        quart_ret = val[1:]

        # taking the beg position value
        rets = quart_ret[beg]

        # find the total profit of stock
        tot_ret = number_of_stocks*rets


        # add all the profits to the all returns list
        all_profits.append(tot_ret)

    # create a list to store the profit and number of quarters
    portfolio_ret = []

    # sum all the profits of all stocks
    col_sum = sum(all_profits)

    # append all profit to portfolio_ret[] list
    portfolio_ret.append(col_sum)

    # append number of quarters to portfolio_ret[] list
    portfolio_ret.append(len(quart_ret))


    return portfolio_ret
