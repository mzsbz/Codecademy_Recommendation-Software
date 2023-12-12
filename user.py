import textwrap

class User:
    def __init__(self):
        self.user_input_list = []

    def get_genres(self):
        self.user_input_list = []
        user_end = False
        while not user_end:
            print('Choose a Genre to add to search:')
            user_input = input()
            self.user_input_list.append(user_input)
            print('Add more Genres? Y/N:')
            user_input = input()
            if user_input.lower() == 'n':
                user_end = True
    
    def print_filtered(self, data):
        matched_count, string_filtered = data.return_filtered(self.user_input_list)

        if matched_count:
            string_matched = f"{matched_count} {'movies' if matched_count > 1 else 'movie'} found with {self.user_input_list}"
            print(string_matched)
            if matched_count > 5:
                print("The top 5 most popular are:")
            print('-'*75)
            print(string_filtered)
        else:
            print(f"No movie found with {self.user_input_list}")
    
    def print_summary(self, data):
        user_end = False
        while not user_end:
            print('Choose movie to read its summary:')
            user_input = int(input())

            string_summary_head, string_summary_body = data.return_summary(user_input)

            print(string_summary_head)
            print(string_summary_body)
            
            print('-'*75 + '\n' + 'Read another summary? (Y/N):')
            user_input = input()
            if user_input.lower() == 'n':
                user_end = True

    def print_similar(self, data):
        user_input = input('Find Similar? (Y/N) \n')