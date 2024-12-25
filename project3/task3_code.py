import pandas as pd 
df= pd.read_csv("movies.csv")

## high revenue of flim 
high_revenue = df.loc[df['revenue_adj'].idxmax()]
## low revenue of flim 
low_revenue = df.loc[df['revenue_adj'].idxmin()]


print("high revenue of flim")
print(high_revenue)
print("low revenue of flim")
print(low_revenue)

