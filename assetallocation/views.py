 # customised imports
from weights import assign_weights
from utilities import stocks
from weighted_returns import weighted_returns

# importing libraries
from django.shortcuts import render
from pandas.tseries.offsets import BYearEnd
from datetime import datetime


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

    # assign weights
    weights = assign_weights(start_year,end_year,time_period,stock_symbols)

    weighted_returns(start_year, end_year, input_price, stock_symbols, weights, time_period)

    return render(request, 'index.html')
