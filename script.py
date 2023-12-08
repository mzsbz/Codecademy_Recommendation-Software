import pandas as pd

df = pd.read_csv('dataset/IMDbMovies-Clean.csv')
# convert csv string in Main Genres into list and handle NaN
df['Main Genres'] = df['Main Genres'].apply(lambda x: x.split(',') if pd.notna(x) else [])
# transform list in column into rows then return list of unique items
unique_genres = df['Main Genres'].explode().unique()

print(unique_genres)

# list of genres to match
desired_genres = ['Drama', 'Horror', 'Music']
# boolean mask for rows with matching mask
mask = df['Main Genres'].apply(lambda x: all(genre in x for genre in desired_genres))
# return top 5 titles from mask as a list
matched_titles = df.loc[mask, 'Title'].head(5).tolist()

for title in matched_titles:
    print(title)