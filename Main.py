# coding=UTF-8
# Import files
import time

from narritive import narritive

# Define globals
narritive = narritive()

def game():
    narritive.user_choice()
    time.sleep(3)
while True:
    game()






    # # clear the screen
    # cls()
    # # If there are no more choices
    # if choice_counter >= len(choice1Array):
    #     game = False
    #     print 'Game over'
    #     quit()
    #
    # print 'Oh mighty hero, will you?'
    # print '1)', choice1Array[choice_counter]
    # print '2)', choice2Array[choice_counter]
    # print
    #
    # # User should be able to choose between two choices
    # userChoice = user_input('What will you decide: ')
    #
    #
    # if userChoice == 'q':
    #     quit()
    # else:
    #     # clear the screen
    #     cls()
    #     if userChoice == '1':
    #         if choice1ResponseArray[choice_counter] == '{store}':
    #             new_store = storeClass()
    #             new_store.createStore()
    #             new_item = new_store.get_purchased_item()
    #             p = PlayerClass()
    #             p.log_items()
    #             p.log_person()
    #
    #             userChoice = raw_input('What will you decide: ')
    #         else:
    #             print choice1ResponseArray[choice_counter]
    #             choice_counter += 1
    #     else:
    #         print choice2ResponseArray[choice_counter]
    #         choice_counter += 1
