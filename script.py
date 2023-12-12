from data import LoadData
from user import User

data = LoadData('dataset/IMDbMovies-Clean.csv', 'Main Genres')
user = User()

data.print_uniques()

user_input_list = user.get_genres()

data.filter_data(user_input_list)

# temporarily print unique genres
# replace with autocomplete
data.print_filtered()

user.print_summary(data)
user.print_similar(data)