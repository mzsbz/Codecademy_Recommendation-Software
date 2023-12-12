# Codecademy_Recommendation-Software

Dataset: [IMDb Movies (231129 - 231201) by popularity](https://www.kaggle.com/datasets/elvinrustam/imdb-movies-dataset/)

## UX Flow
1. (From User) User chooses genres
2. (From Data through User) User receives top 5 movies matching chosen genres by popularity
3. (From User) User enters summary loop
    1. (From Data through User) User choose and views movie summary
    2. (From User) User chooses movie
4. (From User) User prompted to view similar movies
    1. (If YES) User enters recommender loop
        1. (From Recommender through User) User views similar movies
        2. (From Data through User) User choose and views movie summary
        3. (From User) User chooses movie
        4. (From User) User prompted to view similar movies
            1. (If YES) User enters recommender loop
            2. (If NO) End Program
    2. (If NO) End Program

To-do:
- Refactor filters, inputs and print
- Create movie graph to recommend 3 other movies similar to selected movie