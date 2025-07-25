import pandas as pd

df = pd.read_csv("output/raw_wallet_data.csv")

# Feature: borrow_supply_ratio
df["borrow_supply_ratio"] = df["total_borrow_usd"] / (df["total_supply_usd"] + 1e-6)

# Feature: repayment_ratio = repayments / borrows
df["repayment_ratio"] = df["repayments"]  # already between 0–1 (simulated)

# Save processed features
df.to_csv("output/processed_features.csv", index=False)
print("✅ Feature engineering complete. Saved to output/processed_features.csv")
