
def user_help():
    return 'This is player help'

def user_input():
    import narritive
    user_input = raw_input('> ').lower()

    if user_input == 'help':
        return user_help()
    elif user_input == 'health':
        return 'health'
    elif user_input == 'quit' or user_input == 'q' or user_input == 'exit':
        quit()
    elif user_input == '1':
        return 0
    elif user_input == '2':
        return 1
    else:
        return 'Invalid Input!'
