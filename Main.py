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
choiceCounter = 0

p = PlayerClass()

choice1Array = ['Begin your journy',
                'Equip yourself']

choice2Array = ['Wimp out like a lame person',
                'Get going']

choice1ResponseArray = ['Horray!' ,
                        '{store}']

choice2ResponseArray = ['You suck!!!',
                        'You\'re heading out of town']
def user_choice():

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
                    ['Begin your journy2','Wimp out like a lame person2'],
                    ['Horray!','You suck!!!2']
                ],
            ]

    print narritive_dictionary[choiceCounter][0][0]
    print narritive_dictionary[choiceCounter][1][0]
    print

    input_result = user_input.user_input()

    if isinstance(input_result, str):
        print input_result

    if isinstance(input_result, int):
        print narritive_dictionary[choiceCounter][input_result][1]



while game:
    user_choice()
    choiceCounter += 1







    # # clear the screen
    # cls()
    # # If there are no more choices
    # if choiceCounter >= len(choice1Array):
    #     game = False
    #     print 'Game over'
    #     quit()
    #
    # print 'Oh mighty hero, will you?'
    # print '1)', choice1Array[choiceCounter]
    # print '2)', choice2Array[choiceCounter]
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
    #         if choice1ResponseArray[choiceCounter] == '{store}':
    #             new_store = storeClass()
    #             new_store.createStore()
    #             new_item = new_store.get_purchased_item()
    #             p = PlayerClass()
    #             p.log_items()
    #             p.log_person()
    #
    #             userChoice = raw_input('What will you decide: ')
    #         else:
    #             print choice1ResponseArray[choiceCounter]
    #             choiceCounter += 1
    #     else:
    #         print choice2ResponseArray[choiceCounter]
    #         choiceCounter += 1
