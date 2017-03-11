# coding=UTF-8
# Import files
from Store import storeClass, Item
from Player import PlayerClass
import os
import user_input

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Open Text Files
introtxt = open('Intro.txt', 'r')

# Intro text
for line in introtxt:
    print line,
introtxt.close()

# Define globals
game = True
choice_counter = 0
player_class = PlayerClass()

def user_choice():

    cls()
    narritive_dictionary = [
                [
                    [
                        'Begin your journy',
                        'Horray!'
                    ],
                    [
                        'Wimp out like a lame person',
                        'You suck!!!'
                    ]
                ],
                [
                    [
                        'Equip yourself',
                        '{store}'
                    ],
                    [
                        'Get going',
                        'You\'re heading out of town'
                    ]
                ],
            ]

    print narritive_dictionary[choice_counter][0][0]
    print narritive_dictionary[choice_counter][1][0]
    print

    input_result = user_input.user_input()

    if isinstance(input_result, str):
        print input_result

    if isinstance(input_result, int):
        print narritive_dictionary[choice_counter][input_result][1]

    print 'Press "c" to continue'
    user_input.user_input()



while game:
    user_choice()
    choice_counter += 1







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
