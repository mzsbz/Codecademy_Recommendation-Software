import pandas as pd

class LoadData:

    def __init__(self, csv, column_filter):
        self.df = pd.read_csv(csv)
        self.column_filter = column_filter

    def get_uniques(self):
        self.df = self.df.dropna(subset=[self.column_filter])
        # convert csv string in Main Genres into list and handle NaN
        self.df[self.column_filter] = self.df[self.column_filter].apply(lambda x: x.split(','))
        # transform list in column into rows then return list of unique items
        uniques = self.df[self.column_filter].explode().unique()
        unique_list = list(uniques)
        return unique_list
    
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