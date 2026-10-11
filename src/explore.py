import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb



numData = np.genfromtxt("data/all_stocks_5yr.csv",
                        delimiter=",",
                        names=True,
                        dtype=None,
                        encoding="utf-8")

df = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
print(df.shape)
print(df.head())

isApple = numData["Name"] == "AAL"
stocksAPL = numData[isApple]
totalAppleStocks = len(stocksAPL)
print("Total Apple Stocks are: ", totalAppleStocks)


