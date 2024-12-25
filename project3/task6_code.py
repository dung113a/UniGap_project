import pandas as pd 
from collections import Counter


### director
df=pd.read_csv("movies.csv")
# Đếm số lượng phim của mỗi đạo diễn
director_counts = df['director'].value_counts()

# Tìm đạo diễn có nhiều phim nhất
top_director = director_counts.idxmax()
top_director_count = director_counts.max()

print(f"The director with the most films: {top_director} ({top_director_count} films)")

### actor
actor_counts = Counter()
df['cast'].dropna().apply(lambda x: actor_counts.update(x.split('|')))

# Tìm diễn viên có nhiều phim nhất
top_actor, top_actor_count = actor_counts.most_common(1)[0]

print(f"The actor with the most films: {top_actor} ({top_actor_count} films)")


