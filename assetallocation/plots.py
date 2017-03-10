# importing libraries
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot


def weighted_returns_plot(stock_symbols, all_returns, time_period):

    # obtaining the TICKER symbols of the stocks
    stock_symbols = stock_symbols

    # add the TICKER symbol Equal_weighted to the stock inorder to display in graph
    stock_symbols.append("Equal_weighted")

    print ("all_returns",all_returns)

    # convert to numpy array
    all_returns = np.array(all_returns)
    shap = all_returns.shape
    row = shap[0]
    column = len(all_returns[0])

    # calculating x and y axis
    x_axis = []
    for k in range(column):
        k = time_period + str(k)
        x_axis.append(k)

    loop = {}
    for i in range(0,row):
        loop[i] = all_returns[i]

    data = []
    for i in range(0,row):
        trace = go.Scatter(
            x=x_axis,
            y=loop[i],
            fill=None,
            name = "Equal weighted",
            # name = stock_symbols[i],
        )
        data.append(trace)

    # plotting graph
    plot(data, filename='portfolio_graph.html')
