import numpy as np
from scipy.stats import norm

def historical_var(returns, alpha):
    return np.percentile(returns, (1 - alpha) * 100)

def parametric_var(mean, std, alpha):
    z = norm.ppf(1 - alpha)
    return mean + z * std
