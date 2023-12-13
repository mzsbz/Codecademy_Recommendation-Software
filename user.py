import textwrap

class User:
    def __init__(self):
        self.user_input_list = []

    def get_genres(self):
        self.user_input_list = []
        user_end = False
        while not user_end:
            user_input = input('Choose a Genre to add to search: ')
            self.user_input_list.append(user_input)
            user_input = input('Add more Genres? Y/N: ')
            if user_input.lower() == 'n':
                user_end = True
    
    def print_filtered(self, data):
        matched_count, string_filtered, filtered_df = data.return_filtered(self.user_input_list)

        if matched_count:
            string_matched = f"{matched_count} {'movies' if matched_count > 1 else 'movie'} found with {self.user_input_list}"
            print(string_matched)
            if matched_count > 5:
                print("The top 5 most popular are:")
            print('-'*75)
            print(string_filtered)
        else:
            print(f"No movie found with {self.user_input_list}")
    
    def print_details(self, data):
        user_end = False
        count = 0
        while not user_end:
            if count > 0:
                self.print_filtered(data)

            self.choice_filtered = int(input('(1 - 5) Read Details: '))

            string_summary_head, string_summary_body = data.return_details(self.choice_filtered)

            print(string_summary_head)
            print(string_summary_body)
            
            user_input = input('-'*75 + '\n' + 'Read another summary? (Y) | Choose movie (N): ')
            count += 1

            if user_input.lower() == 'n':
                user_end = True

        print(f'\nSelected Movie:')
        print(string_summary_head)

        self.pruned_data_list = data.return_pruned(self.choice_filtered)

    def print_similar(self, recommender):
        user_input = input('-'*75 + '\n' + 'Find Similar? (Y) | Exit (N): ')
        if user_input.lower() == 'n':
            exit()
        elif user_input.lower() == 'y':
            recommender.import_data(self.pruned_data_list)
            recommender.calculate_similarity()
            sorted_list = recommender.heapsort()
            
            # print("reverse list")
            sorted_list.reverse()
            # print(sorted_list)
            print("\nSimilar movies to consider:")
            print('='*75)
            for idx in range(1, 4):
                print(f'{idx} | {sorted_list[idx][0]} ({int(sorted_list[idx][1])}), [{sorted_list[idx][4]}/10]')
