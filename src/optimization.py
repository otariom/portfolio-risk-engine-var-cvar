import numpy as np
from scipy.optimize import minimize

def mean_cvar_optimization(returns, cvar_func):
    n = returns.shape[1]
    weights = np.ones(n) / n

    def objective(w):
        portfolio_returns = returns @ w
        var = np.percentile(portfolio_returns, 5)
        return cvar_func(portfolio_returns, var)

    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    bounds = [(0, 1)] * n

    result = minimize(objective, weights, bounds=bounds, constraints=constraints)
    return result.x
