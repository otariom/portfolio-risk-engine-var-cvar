import pandas as pd
import numpy as np

def covariance_matrix(returns):
    return returns.cov()

def correlation_matrix(returns):
    return returns.corr()

def diversification_benefit(returns, weights):
    cov = returns.cov()
    portfolio_var = np.dot(weights.T, np.dot(cov, weights))
    indiv_var = np.sum(weights * np.diag(cov))
    return indiv_var - portfolio_var
