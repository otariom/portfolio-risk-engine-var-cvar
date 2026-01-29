import numpy as np
from config.settings import MONTE_CARLO_PATHS, TRADING_DAYS

def monte_carlo_var(returns, alpha):
    mu = returns.mean()
    sigma = returns.std()

    dt = 1 / TRADING_DAYS
    simulations = []

    for _ in range(MONTE_CARLO_PATHS):
        shock = np.random.normal(0, 1)
        simulated_return = (
            (mu - 0.5 * sigma**2) * dt
            + sigma * np.sqrt(dt) * shock
        )
        simulations.append(simulated_return)

    return np.percentile(simulations, (1 - alpha) * 100)
