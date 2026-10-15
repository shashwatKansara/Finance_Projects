import pandas as pd
import matplotlib.pyplot as plt

data2 = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
apple = data2[data2["Name"]== "AAPL"]
micro = data2[data2["Name"]== "MSFT"]
macD = data2[data2["Name"]== "MCD"]
rmd = data2[data2["Name"]=="RMD"]

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.bar(apple["date"], apple["close"], width=1)
plt.title("Apple Closing Price")

plt.subplot(2,2,2)
plt.bar(micro["date"], micro["close"], width=1)
plt.title("Microsoft Closing Price")

plt.subplot(2,2,3)
plt.bar(macD["date"], macD["close"])
plt.title("MCD Closing Price")

plt.subplot(2,2,4)
plt.bar(rmd["date"], rmd["close"])
plt.title("RMD Closing Price")

plt.savefig("images/Closing_Price_Comparison(4)")
plt.show()

