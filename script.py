from data import LoadData
from recommender import Recommender
from user import User

data = LoadData('dataset/IMDbMovies-Clean.csv', 'Main Genres')
recommender = Recommender()
user = User()

# temporarily print unique genres
# replace with autocomplete
data.print_uniques()

user.get_genres()
user.print_filtered(data)
user.print_summary(data)
user.print_similar(recommender)