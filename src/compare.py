import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
appl = df[df["Name"] == "AAL"]

plt.plot(appl["date"], appl["close"])
plt.show()

