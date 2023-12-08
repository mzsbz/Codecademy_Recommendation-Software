import pandas as pd

df = pd.read_csv('dataset/IMDbMovies-Clean.csv')

# drop nan values from Main Genres
df = df.dropna(subset=['Main Genres'])
# convert csv string in Main Genres into list and handle NaN
df['Main Genres'] = df['Main Genres'].apply(lambda x: x.split(','))
# transform list in column into rows then return list of unique items
unique_genres = df['Main Genres'].explode().unique()
unique_genres_list = list(unique_genres)
print(unique_genres_list)
print('-'*50)

# list of genres to match
desired_genres = ['Action']
# boolean mask for rows with matching mask
mask = df['Main Genres'].apply(lambda x: all(genre in x for genre in desired_genres))
# count rows that match
matched_count = mask.sum()
# return top 5 rows from mask
matched_top5_title = df.loc[mask, 'Title'].head(5).tolist()
matched_top5_year = df.loc[mask, 'Release Year'].head(5).tolist()
matched_top5_rating = df.loc[mask, 'Rating (Out of 10)'].head(5).tolist()
matched_top5 = list(zip(matched_top5_title, matched_top5_year, matched_top5_rating))

if matched_count:
    print(f"{matched_count} {'movies' if matched_count > 1 else 'movie'} found with {desired_genres}")
    if matched_count > 5:
        print("The top 5 most popular are:")
    print('-'*50)
    for title, year, rating in matched_top5:
        print(f"{title} ({int(year)}), [{rating}/10]")
else:
    print(f"No movie found with {desired_genres}")
    