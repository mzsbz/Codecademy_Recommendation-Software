import pandas as pd
import textwrap

class LoadData:

    def __init__(self, csv, column_filter):
        self.df = pd.read_csv(csv)
        self.column_filter = column_filter

    def print_uniques(self):
        self.df = self.df.dropna(subset=[self.column_filter])
        # convert csv string in Main Genres into list and handle NaN
        self.df[self.column_filter] = self.df[self.column_filter].apply(lambda x: x.split(','))
        # transform list in column into rows then return list of unique items
        uniques = self.df[self.column_filter].explode().unique()
        unique_list = list(uniques)
        print(unique_list)
    
    def filter_data(self, user_input_list):
        # list of genres to match
        self.desired_genres = user_input_list
        # boolean mask for rows with matching mask
        mask = self.df[self.column_filter].apply(lambda x: all(genre in x for genre in self.desired_genres))
        #filter df off mask
        self.filtered_df = self.df[mask]
        # count rows that match
        self.matched_count = mask.sum()

        return self.filtered_df, self.matched_count
    
    def print_filtered(self):
        if self.matched_count:
            print(f"{self.matched_count} {'movies' if self.matched_count > 1 else 'movie'} found with {self.desired_genres}")
            if self.matched_count > 5:
                print("The top 5 most popular are:")
            print('-'*75)

            for idx in range(5):
                print(f"{idx+1} | {self.filtered_df['Title'].iloc[idx]} ({int(self.filtered_df['Release Year'].iloc[idx])}), [{self.filtered_df['Rating (Out of 10)'].iloc[idx]}/10]")
        else:
            print(f"No movie found with {self.desired_genres}")

    def print_summary(self):
        user_end = False
        while not user_end:
            print('Choose movie to read its summary:')
            user_input = int(input())
            movie_idx = user_input - 1
            print('='*75)
            print(f'{self.filtered_df['Title'].iloc[movie_idx]} ({int(self.filtered_df['Release Year'].iloc[movie_idx])}), [{self.filtered_df['Rating (Out of 10)'].iloc[movie_idx]}/10]')
            print('-'*75)
            print(textwrap.fill(self.filtered_df['Summary'].iloc[movie_idx], 75))
            print('-'*75)
            print('Read another summary? Y/N:')
            user_input = input()
            if user_input.lower() == 'n':
                user_end = True