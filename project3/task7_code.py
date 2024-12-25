import pandas as pd 
df = pd.read_csv("movies.csv")
from collections import Counter

genre_counts = Counter()
df['genres'].dropna().apply(lambda x: genre_counts.update(x.split('|')))

for genre, count in genre_counts.items():
    print(f"{genre}: {count}")

pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).to_csv('task7.csv', index=False)

