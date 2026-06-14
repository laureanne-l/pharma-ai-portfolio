import pandas as pd
df = pd.read_csv("trials.csv")

print(df.shape)
print(df.columns.tolist())