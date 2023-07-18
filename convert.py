import pandas as pd
df = pd.read_parquet('data/data.parquet')
df.to_csv('data/data.csv')
