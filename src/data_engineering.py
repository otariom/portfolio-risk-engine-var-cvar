import yfinance as yf
import pandas as pd
from config.settings import TICKERS, START_DATE, END_DATE

def fetch_price_data():
    data = yf.download(
        TICKERS,
        start=START_DATE,
        end=END_DATE,
        auto_adjust=True
    )["Close"]

    data.dropna(inplace=True)
    data.to_csv("data/raw_prices.csv")
    return data
