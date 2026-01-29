import pandas as pd
import numpy as np

def compute_log_returns(price_df):
    returns = np.log(price_df / price_df.shift(1))
    returns.dropna(inplace=True)
    returns.to_csv("data/clean_returns.csv")
    return returns
