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
# count rows that match
matched_count = mask.sum()
# return top 5 rows from mask
matched_top5_title = df.loc[mask, 'Title'].head(5).tolist()
matched_top5_year = df.loc[mask, 'Release Year'].head(5).tolist()
matched_top5_rating = df.loc[mask, 'Rating (Out of 10)'].head(5).tolist()
matched_top5_summary = df.loc[mask, 'Summary'].head(5).tolist()
matched_top5 = list(zip([x+1 for x in range(5)], matched_top5_title, matched_top5_year, matched_top5_rating))

def get_results():
    if matched_count:
        print(f"{matched_count} {'movies' if matched_count > 1 else 'movie'} found with {desired_genres}")
        if matched_count > 5:
            print("The top 5 most popular are:")
        print('-'*75)
        for idx, title, year, rating in matched_top5:
            print(f"{idx} | {title} ({int(year)}), [{rating}/10]")
    else:
        print(f"No movie found with {desired_genres}")
    
get_results()

user_end = False
while not user_end:
    print('Choose movie to read its summary:')
    user_input = int(input())
    print('='*75)
    print(f'{matched_top5[user_input-1][1]} ({int(matched_top5[user_input-1][2])}), [{matched_top5[user_input-1][3]}/10]')
    print('-'*75)
    print(textwrap.fill(matched_top5_summary[user_input-1], 75))
    print('-'*75)
    print('Read another summary? Y/N:')
    user_input = input()
    if user_input.lower() == 'n':
        user_end = True