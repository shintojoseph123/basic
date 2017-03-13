 # customised imports
from weights import assign_weights
from utilities import stocks
from weighted_returns import weighted_returns
from brownian import geometric_brownian_motion_levels


# importing libraries
from django.shortcuts import render
from pandas.tseries.offsets import BYearEnd
from datetime import datetime

import pandas as pd


# views
def index(request):

    # variables to give inputs

    start_year = "2007-01-1"
    end_year = "2008-01-31"
    input_price = 500000
    time_period = "Q"


    #set BYearEnd as Buisness year end function
    BuisnessYearEnd = BYearEnd()
    # obtain the start year
    # start_year = raw_input("enter start year")+str("-01-1")
    #Last buisness day of previous year
    start_year = BuisnessYearEnd.rollback(start_year)
    # obtain the end year
    # end_year = raw_input("enter end year")+str("-01-31")
    #Last buisness day of current year
    end_year = BuisnessYearEnd.rollback(end_year)

    # input_price = input("enter the input price")
    # time_period = raw_input(" W for weekly, M for monthly, Q for quarterly, A for yearly")
    number_of_stocks = int(input("enter the number of stocks"))

    print (start_year.date(),end_year)

    stock_symbols = stocks(number_of_stocks)
#
# # working timeit
#     import timeit
#     # from utilities import stocks
#
#     sec = timeit.timeit(stocks(number_of_stocks), number=20)
#     print sec
# # working timeit

    #
    # def test():
    #     L = []
    #     for i in range(100):
    #         L.append(i)


    # if __name__ == '__main__':
    #     import timeit
    #     print "entered"
    #     print(timeit.timeit("test()", setup="from __main__ import test"))

    # assign weights
    weights = assign_weights(start_year,end_year,time_period,stock_symbols)

# athiras
    # start- function call
    price_matrix = geometric_brownian_motion_levels(start_year, end_year, stock_symbols, time_period)

    close_price = pd.DataFrame(price_matrix, columns = stock_symbols)

    print "brownian",close_price

# athiras end

    weighted_returns(start_year, end_year, input_price, stock_symbols, weights, time_period,close_price)

    # # working timeit
    # import timeit
    # # from utilities import stocks
    #
    # sec = timeit.timeit(weighted_returns(start_year, end_year, input_price, stock_symbols, weights, time_period), number=1)
    # print sec
    # # working timeit






    return render(request, 'index.html')

# import timeit
#
# t1 = timeit.Timer("index(request)",setup = "from __main__ import index; ")
# secs = t1.timeit()
# print (secs)

# from mymodule import costly_func
# timeit.timeit(costly_func, number=1000)
