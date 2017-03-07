

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
