import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
tickers = ["AAPL", "MSFT", "AAL", "MCD"]
averages = []
for i in tickers:
    averages.append(data1[data1["Name"]==i]["close"].mean())

plt.bar(tickers, averages)
plt.title("Average Closing Stock Prices, 2013-2018")
plt.show()

