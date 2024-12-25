import pandas as pd
df = pd.read_csv('movies.csv')

def fix_date_format(date):
    try:
        month, day, year = map(int, date.split('/'))
        if year > 50:
            year = 1900 + year
        else:
            year = 2000 + year
        return f"{year:04d}-{month:02d}-{day:02d}"
    except:
        return None 


df['release_date'] = df['release_date'].apply(fix_date_format)
df['release_date'] = pd.to_datetime(df['release_date'])
df_sorted = df.sort_values(by='release_date', ascending=False)
df_sorted.to_csv('task1.csv', index=False)

