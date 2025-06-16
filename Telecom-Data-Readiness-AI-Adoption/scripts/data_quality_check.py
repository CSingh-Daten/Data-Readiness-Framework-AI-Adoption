import pandas as pd

df = pd.read_csv('data/raw/customers.csv')
missing = df.isnull().sum()
print("Missing values:\n", missing)
