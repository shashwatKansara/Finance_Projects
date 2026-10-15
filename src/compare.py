import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
mcdPrice = data[data["Name"] == "MCD"]

fig, (x1,x2) = plt.subplots(1,2)

x1.plot(mcdPrice["date"], mcdPrice["open"])
x1.set_title("Opening Price of MCD stock")
x1.set_xlabel("Date in years")
x1.set_ylabel("Opening Price in USD")

x2.plot(mcdPrice["date"], mcdPrice["close"])
x2.set_title("Closing Price of MCD Stock")
x2.set_xlabel("Date in years")
x2.set_ylabel("Closing Price in USD")

plt.tight_layout()
plt.show()


