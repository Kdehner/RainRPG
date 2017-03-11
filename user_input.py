def user_help():
    print 'This is player help'

def user_input():
    user_input = raw_input('> ').lower()

    if user_input == 'help':
        user_help()
    elif user_input == 'health':
        print 'health'
    elif user_input == 'quit' or user_input == 'q' or user_input == 'exit':
        quit()
    elif user_input == '1':
        print 'you chose 1'
    elif user_input == '2':
        print 'you chose 2'
    else:
        print 'Invalid Input!'
