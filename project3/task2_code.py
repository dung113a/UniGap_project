import pandas as pd 
df=pd.read_csv("movies.csv")

df_point = df[df["vote_average"]>7.5].sort_values(by='vote_average'
	,ascending=True
) 

df_point.to_csv('task2.csv',index=False)
