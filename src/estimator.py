import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("data/all_stocks_5yr.csv", parse_dates=["date"])
nvda = data[data["Name"]=="NVDA"]

returns = nvda["close"].pct_change().dropna()
last_price = nvda["close"].iloc[-1]

print(len(returns), " days of stock returns")
print("Today's price is ", last_price)

np.random.seed(42)
sims = np.random.choice(returns, size=(1000, 252))     # 1000 rows × 252 days
paths = last_price * (1 + sims).cumprod(axis=1)        # chain along each row
print(paths.shape)                                     # should print (1000, 252)

# Step 5: the estimate
final = paths[:, -1]                                   # last day of every future
p5, p50, p95 = np.percentile(final, [5, 50, 95])
print(f"Bad case (5%):    ${p5:.2f}")
print(f"Typical (median): ${p50:.2f}")
print(f"Good case (95%):  ${p95:.2f}")
print(f"Chance of a loss: {(final < last_price).mean():.0%}")

plt.figure(figsize=(14, 6))

plt.subplot(1,2,1)
for i in range(1000):
    plt.plot(paths[i], color="grey", alpha=0.05)
plt.plot(np.percentile(paths,95, axis=0), color = "green", label="95th percentile")
plt.plot(np.percentile(paths,50,axis=0), color = "blue", label = "Median")
plt.plot(np.percentile(paths,5,axis=0), color = "red", label = "5th percentile")
plt.axhline(last_price, color= "black", linestyle="--", label = "Today's price")
plt.title("1,000 simulated futures")
plt.xlabel("Trading days from now")
plt.ylabel("Price (USD)")
plt.legend()

plt.subplot(1,2,2)
plt.hist(final, bins=50)
plt.axvline(p5, color="red", linestyle="--", label=f"5%: ${p5:.0f}")
plt.axvline(p50, color="blue", linestyle="--", label=f"Median: ${p50:.0f}")
plt.axvline(p95, color = "green", linestyle="--", label=f"95th Percentile: ${p95:.0f}")
plt.title("Price after 1 year")
plt.xlabel("Price (USD)")
plt.ylabel("Number of simulations")
plt.legend()


plt.suptitle("NVIDIA Monte Carlo Estimate")
plt.tight_layout()
plt.savefig("images/nvidia_MC.png")
plt.show()


