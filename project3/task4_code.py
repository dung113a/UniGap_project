import pandas as pd 
df = pd.read_csv("movies.csv")

total = df['revenue'].sum()
 
print(f"Total revenue: {total} ")
