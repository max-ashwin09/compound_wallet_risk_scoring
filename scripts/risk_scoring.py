
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("output/processed_features.csv")

# Select features to scale
features = [
    "borrow_supply_ratio",
    "num_liquidations",
    "last_active_days",
    "repayment_ratio"
]

# Normalize features
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[features]), columns=features)

# Risk score calculation
df['risk_score'] = (
    0.4 * df_scaled['borrow_supply_ratio'] +
    0.3 * df_scaled['num_liquidations'] +
    0.2 * df_scaled['last_active_days'] +
    0.1 * (1 - df_scaled['repayment_ratio'])  # inverse of repayment
)

# Scale score to 0–1000
df['score'] = (df['risk_score'] - df['risk_score'].min()) / (df['risk_score'].max() - df['risk_score'].min()) * 1000
df['score'] = df['score'].round(0).astype(int)

# Save final output
df[['wallet_id', 'score']].to_csv("output/wallet_risk_scores.csv", index=False)
print("✅ Risk scoring complete. Final file: output/wallet_risk_scores.csv")
