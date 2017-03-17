from Store import storeClass

def take_input(user_input, narritive_list, choice_counter, player):

    if user_input == '{choice1}':
        return options(narritive_list[choice_counter][0][1], player)
    elif user_input == '{choice2}':
        return options(narritive_list[choice_counter][1][1], play)
    else:
        return user_input

def options(narritive_list_link, player):

    if narritive_list_link == '{store}':
        store = storeClass(player)
        store.createStore()

        return ''

    else:
        return narritive_list_link
