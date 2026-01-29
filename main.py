from src.data_engineering import fetch_price_data
from src.returns import compute_log_returns
from src.var_models import historical_var
from src.cvar_models import cvar
from src.correlation import correlation_matrix
from src.visualization import plot_correlation
from config.settings import CONFIDENCE_LEVEL

prices = fetch_price_data()
returns = compute_log_returns(prices)

portfolio_returns = returns.mean(axis=1)

var_value = historical_var(portfolio_returns, CONFIDENCE_LEVEL)
cvar_value = cvar(portfolio_returns.values, var_value)

print(f"VaR: {var_value}")
print(f"CVaR: {cvar_value}")

corr = correlation_matrix(returns)
plot_correlation(corr)
