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
        
        return self.user_input_list