import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
nvda = data[data["Name"]=="NVDA"]

returns = nvda["close"].pct_change().dropna()
last_price = nvda["close"].iloc[-1]

print(len(returns), " days of stock returns")
print("Today's price is ", last_price)

# future one year simulation
one_year = np.random.choice(returns,size=252)
path = last_price * (1 + one_year).cumprod()
plt.plot(path)
plt.axhline(last_price, linestyle="--", color="black")
plt.title("Simulation of Nvidia's next year ")
plt.show()
