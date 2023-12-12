from data import LoadData
import textwrap

data = LoadData('dataset/IMDbMovies-Clean.csv', 'Main Genres')
print(data.get_uniques())

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

filtered_df, matched_count = data.filter_data(user_input_list)
data.print_filtered()

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