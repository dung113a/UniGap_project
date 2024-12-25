import pandas as pd 
df = pd.read_csv("movies.csv")
df['profit'] = df['revenue'] - df['budget']

top10_movie = df.sort_values(by='profit',ascending= False).head(10)

top10_movie.to_csv('task5.csv',index=False)
