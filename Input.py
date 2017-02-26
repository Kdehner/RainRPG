class UserInputClass:

    def user_help(self):
        print 'This is player help'

    def user_input(self, input):
        user_input = raw_input(input).lower()


        if user_input == 'help'.lower():
            self.user_help()


        return user_input
