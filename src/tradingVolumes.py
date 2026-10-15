import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
appl = data[data["Name"] == "AAPL"]
fig, axes = plt.subplots(2,2, figsize=(12,8))

axes[0, 0].plot(appl["date"], appl["close"])
axes[0, 0].set_title("Price")
axes[0, 1].plot(appl["date"], appl["volume"])
axes[0, 1].set_title("Volume")

returns = appl["close"].pct_change() *100
axes[1, 0].plot(appl["date"], returns, linewidth=0.7)
axes[1, 0].set_title("Daily % change")
axes[1, 1].hist(returns.dropna(), bins = 50)
axes[1, 1].set_title("Distribution of daily % change")

fig.suptitle("Apple at a glance")
plt.tight_layout()
plt.savefig("images/apple_dashboard.png", dpi=200, bbox_inches="tight")
plt.show()



