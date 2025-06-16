import pandas as pd

df = pd.read_csv('data/processed/customers_clean.csv')
df['high_usage'] = df['data_usage_gb'] > 5
df.to_csv('data/processed/customers_features.csv', index=False)
