def take_input(user_input, narritive_list, choice_counter):

    if user_input == '{choice1}':
        return options(narritive_list[choice_counter][0][1])
    elif user_input == '{choice2}':
        return options(narritive_list[choice_counter][1][1])
    else:
        return user_input

def options(narritive_list_link):

    if narritive_list_link == '{store}':
        return 'store'
    else:
        return narritive_list_link
