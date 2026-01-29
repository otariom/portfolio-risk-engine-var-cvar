import numpy as np

def backtest_var(returns, var_series):
    breaches = returns < var_series
    return breaches.sum(), len(returns)
