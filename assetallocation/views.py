from django.shortcuts import render

# customised imports
from weights import assign_weights
from utilities import stocks
from weighted_returns import weighted_returns


# views
def index(request):

    # variables to give inputs

    # start_year = input("enter start year")
    # end_year = input("enter end year")
    # input_price = input("enter the input price")
    # time_period = raw_input(" W for weekly, M for monthly, Q for quarterly, A for yearly")
    number_of_stocks = int(input("enter the number of stocks"))

    start_year = 2007
    end_year = 2008
    input_price = 500000
    time_period = "Q"

    stock_symbols = stocks(number_of_stocks)

    # assign weights
    weights = assign_weights(start_year,end_year,time_period,stock_symbols)

    weighted_returns(start_year, end_year, input_price, stock_symbols, weights, time_period)

    return render(request, 'index.html')
