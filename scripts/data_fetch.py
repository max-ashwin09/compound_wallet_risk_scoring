import pandas as pd
import random
import os

# Load wallet list
wallets_df = pd.read_csv('wallets.csv')

# Simulate raw transaction features (replace this with actual API later)
def simulate_wallet_data(wallet_id):
    return {
        "wallet_id": wallet_id,
        "total_supply_usd": round(random.uniform(100, 5000), 2),
        "total_borrow_usd": round(random.uniform(50, 4000), 2),
        "num_liquidations": random.randint(0, 3),
        "repayments": round(random.uniform(0, 1), 2),
        "last_active_days": random.randint(1, 180)
    }

data = [simulate_wallet_data(w) for w in wallets_df['wallet_id']]
df = pd.DataFrame(data)

# Save raw data
os.makedirs("output", exist_ok=True)
df.to_csv("output/raw_wallet_data.csv", index=False)
print("✅ Data fetching complete. Saved to output/raw_wallet_data.csv")
