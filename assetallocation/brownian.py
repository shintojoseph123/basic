 # customised imports
from obtain_data import close_price_data
from utilities import yearly_periods

# import all libraries
import pandas as pd
import numpy as np
from scipy.linalg import cholesky




def convert_to_prices(brownian_motion, row, column):
    # method used for calculating prices
    price_matrix = np.full((row+1,column),100)
    for i in range(column):
        for j in range(row):
            price_matrix[j+1,i]=(brownian_motion[j,i])*price_matrix[j,i]

    return price_matrix


def brownian_motion(log_returns,n_assets):
    #generate correlated random values
    sigma = log_returns.std().values

    # correlated matrix
    corr_matrix = log_returns.corr()
    # perform cholesky decomposition
    upper_cholesky = cholesky(corr_matrix, lower=False)

    rand_values = np.random.standard_normal(size = (len(log_returns), n_assets))
    Wiener_process = rand_values.dot(upper_cholesky)*sigma
    return Wiener_process


def geometric_brownian_motion(time_period,log_returns,n_assets):
    #This method constructs a sequence of log returns which, when exponentiated, produce a random Geometric Brownian Motion (GBM).
    #param param: model parameters object
    #return: returns the log returns of a geometric brownian motion process
    #here we will calculate geometric brownian motion process using equation exp((mu-0.5*sigma**2)*dt+(sigma*wt))
    #first part 'sigma_pow_mu_delta'
    #second part is the  Wiener_process for that we call another method  brownian_motion_log_returns()

    #  data downloded as quarterly
    yearly_period = yearly_periods(time_period)
    dt = 1./yearly_period

    mu = log_returns.mean().values
    sigma = log_returns.std().values

    sigma_pow_mu_delta = (mu-0.5*sigma**2)*dt
    Wiener_process = brownian_motion(log_returns,n_assets)
    geometric_brownian_motion = sigma_pow_mu_delta + Wiener_process
    geometric_brownian_motion = np.exp(geometric_brownian_motion)

    return geometric_brownian_motion


def geometric_brownian_motion_levels(start_year, end_year, stock_symbols, time_period):
    #Returns a sequence of price levels for an asset which evolves according to a geometric brownian motion
    #return: the price levels for the asset

    # obtainig close_price_data data
    close_price = close_price_data(start_year, end_year, stock_symbols, time_period)

    print "close_price",close_price

    # calculating log returns
    # log_returns - used to find mu and sigma for geometric_brownian_motion
    log_returns=np.log(close_price/close_price.shift()).dropna()

    # set up the parameters for the simulation
    n_assets = len(stock_symbols)

    brownian_motion = geometric_brownian_motion(time_period, log_returns, n_assets)

    # dimension of log_returns matrix
    log_shape=log_returns.shape
    row=log_shape[0]
    column=log_shape[1]

    return convert_to_prices(brownian_motion, row, column)
