import pandas as pd
import matplotlib.pyplot as plt

rpt = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
nvda = rpt[rpt["Name"]== "NVDA"]
plt.plot(nvda["date"], nvda["open"])
plt.plot(nvda["date"], nvda["close"])
plt.plot(nvda["date"], nvda["high"])
plt.plot(nvda["date"], nvda["low"])

# Return calculation
returns = nvda["close"].pct_change() * 100
drawdown = (nvda["close"] / nvda["close"].cummax()-1) * 100
# drawdown means how much a stock has fallen from its highest price so far


# Generating 4 different graphs within one panel

plt.figure(figsize=(14,9)) # essential for the window size

plt.subplot(2,2,1)
plt.plot(nvda["date"], nvda["close"], label="Close")
plt.plot(nvda["date"], nvda["close"].rolling(50).mean(), label = "50-day avg")
plt.plot(nvda["date"], nvda["close"].rolling(200).mean(), label = "200-day avg")
plt.title("Price with moving averages")

plt.subplot(2,2,2)
plt.plot(nvda["date"], nvda["volume"])
plt.title("Daily trading volume")

plt.subplot(2,2,3)
plt.plot(nvda["date"], drawdown, 0, color="red", alpha=0.3)
plt.title("Drawdown from all-time high prices (5)")

plt.subplot(2,2,4)
plt.hist(returns.dropna(), bins=50)
plt.title("Distribution of daily % change")

plt.suptitle("NVIDIA Stock Report")
plt.tight_layout()
plt.savefig("images/nvidia_report_png")
plt.show()


