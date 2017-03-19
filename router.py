from Store import storeClass
from combat import Combat

instances = {}

def take_input(user_input, narritive_list, choice_counter):

    if user_input == '{choice1}':
        return options(narritive_list[choice_counter][0][1])
    elif user_input == '{choice2}':
        return options(narritive_list[choice_counter][1][1])
    else:
        return user_input

def options(narritive_list_link):

    if narritive_list_link == '{store}':
        store = storeClass()
        store.createStore()

        return ''
    elif narritive_list_link == '{combat}':
        combat = Combat()
        combat.combat()

        return ''


    else:
        return narritive_list_link

def get_instance(instance):

    if instance in instances.keys():
        return instances[instance]
    else:
        return None


def pass_instance(**kwargs):

    for key, value in kwargs.items():
        instances[key] = value
