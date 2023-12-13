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
        print('-'*75)
    
    def return_filtered(self, user_input_list):
        # list of genres to match and boolean mask for rows with matching mask
        self.desired_genres = user_input_list
        mask = self.df[self.column_filter].apply(lambda x: all(genre in x for genre in self.desired_genres))

        #filter df off mask and count rows that match
        self.filtered_df = self.df[mask]
        self.matched_count = mask.sum()

        string_filtered = ''
        for idx in range(5):
            string_result = f"{idx+1} | {self.filtered_df['Title'].iloc[idx]} ({int(self.filtered_df['Release Year'].iloc[idx])}), [{self.filtered_df['Rating (Out of 10)'].iloc[idx]}/10] \n"
            string_filtered += string_result

        return self.matched_count, string_filtered, self.filtered_df

    def return_summary(self, user_input):
        movie_idx = user_input - 1

        string_summary_head = '='*75 + '\n' + f'{self.filtered_df['Title'].iloc[movie_idx]} ({int(self.filtered_df['Release Year'].iloc[movie_idx])}), [{self.filtered_df['Rating (Out of 10)'].iloc[movie_idx]}/10] | {self.filtered_df['Main Genres'].iloc[movie_idx]}'

        string_summary_body = '-'*75 + '\n' + textwrap.fill(self.filtered_df['Summary'].iloc[movie_idx], 75)

        return string_summary_head, string_summary_body
    
    def return_pruned(self, user_input):

        chosen_genres = self.filtered_df['Main Genres'].iloc[user_input -1]
        mask = self.filtered_df[self.column_filter].apply(lambda x: all(genre in x for genre in chosen_genres))

        #filter df off mask and count rows that match
        self.pruned_df = self.filtered_df[mask]

        selected_columns = ['Title', 'Release Year', 'Motion Picture Rating', 'Runtime (Minutes)', 'Rating (Out of 10)', 'Main Genres']
        pruned_df_list = self.pruned_df[selected_columns].values.tolist()

        return pruned_df_list