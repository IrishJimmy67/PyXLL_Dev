import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Generate a dynamic list of tickers to pull from Yahoo Finance API based on the imported file with tickers.

# Stock comparison code
def get(tickers, startdate, enddate):
    def data(ticker):
        return (yf.download(ticker, start=startdate, end=enddate))

    datas = map(data, tickers)
    return (pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))


portfolio_df = pd.read_excel('..\ExistingPortfolio.xlsx')
portfolio_df.head(10)


end_of_last_year = datetime.datetime(2020, 12, 31)

stocks = ["AAPL", "JNJ"]
stocks_start = "2020-12-01"
stocks_end = "2021-02-26"
stocks_end2 = "2021-02-25"

all_data = get(stocks, stocks_start, stocks_end)

# Also only pulling the ticker, date and adj. close columns for our tickers.
adj_close = all_data[['Adj Close']].reset_index()
print(adj_close.head(5))

# Grabbing the ticker close from the end of last year
adj_close_start = adj_close[adj_close['Date'] == end_of_last_year]
print(adj_close_start.head())

# Grab the latest stock close price
adj_close_latest = adj_close[adj_close['Date'] == stocks_end2]
print(adj_close_latest.head())

adj_close_latest.set_index('Ticker', inplace=True)
print(adj_close_latest.head())


# Set portfolio index prior to merging with the adj close latest.
portfolio_df.set_index(['Ticker'], inplace=True)
print(portfolio_df.head())

# Merge the portfolio dataframe with the adj close dataframe; they are being joined by their indexes.
merged_portfolio = pd.merge(portfolio_df, adj_close_latest, left_index=True, right_index=True)
print(merged_portfolio.head())

# The below creates a new column which is the ticker return; takes the latest adjusted close for each position
# and divides that by the initial share cost.
merged_portfolio['ticker return'] = merged_portfolio['Adj Close'] / merged_portfolio['Unit Cost'] - 1
print(merged_portfolio.head(5))

# stocks = ["AAPL", "JNJ"]
# data = yf.download(stocks, start="2020-01-01", end="2020-01-31")
# print(data.head(5))
# columnNames = data.columns.values.tolist()
# print((columnNames))