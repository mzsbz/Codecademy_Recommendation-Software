import pandas as pd
import textwrap

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

user_input_list = []
user_end = False
while not user_end:
    print('Choose a Genre to add to search:')
    user_input = input()
    user_input_list.append(user_input)
    print('Add more Genres? Y/N:')
    user_input = input()
    if user_input.lower() == 'n':
        user_end = True

# list of genres to match
desired_genres = user_input_list
# boolean mask for rows with matching mask
mask = df['Main Genres'].apply(lambda x: all(genre in x for genre in desired_genres))
#filter df off mask
filtered_df = df[mask]
# count rows that match
matched_count = mask.sum()

def get_results():
    if matched_count:
        print(f"{matched_count} {'movies' if matched_count > 1 else 'movie'} found with {desired_genres}")
        if matched_count > 5:
            print("The top 5 most popular are:")
        print('-'*75)

        for idx in range(5):
            print(f"{idx+1} | {filtered_df['Title'].iloc[idx]} ({int(filtered_df['Release Year'].iloc[idx])}), [{filtered_df['Rating (Out of 10)'].iloc[idx]}/10]")
    else:
        print(f"No movie found with {desired_genres}")
    
get_results()

user_end = False
while not user_end:
    print('Choose movie to read its summary:')
    user_input = int(input())
    movie_idx = user_input - 1
    print('='*75)
    print(f'{filtered_df['Title'].iloc[movie_idx]} ({int(filtered_df['Release Year'].iloc[movie_idx])}), [{filtered_df['Rating (Out of 10)'].iloc[movie_idx]}/10]')
    print('-'*75)
    print(textwrap.fill(filtered_df['Summary'].iloc[movie_idx], 75))
    print('-'*75)
    print('Read another summary? Y/N:')
    user_input = input()
    if user_input.lower() == 'n':
        user_end = True