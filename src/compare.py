import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])

mcd = data[data["Name"] == "MCD"]
msft = data[data["Name"]=="MSFT"]
aal = data[data["Name"] == "AAL"]
mchp = data[data["Name"] == "MCHP"]

plt.plot(msft["date"], msft["close"])
plt.plot(mcd["date"], mcd["close"])
plt.plot(mchp["date"], mchp["close"])
plt.plot(aal["date"], aal["close"])
plt.savefig("images/my_first_chart.png")
plt.show()


