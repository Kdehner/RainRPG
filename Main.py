
# while True:
#     print 'You are the one and only hero!'
#     print 'Destined to save the great land of Rain!'
#     print 'Please grace us with your name hero!'
#     print
#     name = raw_input('Enter your name: ')
#     print 'Hello ', name, 'welcome to your destiny!'
#     quit()







# Starting game logic here to prevent collisions

# Import files
from Store import storeClass, Item
from Input import UserInputClass
import os

user_input = UserInputClass().user_input

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Open Text Files
introtxt = open('Intro.txt', 'r')

# Intro text
for line in introtxt:
    print line,
introtxt.close()

# Get user name
name = user_input('Enter your name: ')
print 'Hello {} welcome to your destiny!'.format(name)

# Define globals
game = True

choiceCounter = 0
choice1Array = ['Begin your journy',
                'Equip yourself']

choice2Array = ['Wimp out like a lame person',
                'Get going']

choice1ResponseArray = ['Horray!' ,
                        '{store}']

choice2ResponseArray = ['You suck!!!',
                        'You\'re heading out of town']

while game:
    # clear the screen
    cls()
    # If there are no more choices
    if choiceCounter >= len(choice1Array):
        game = False
        print 'Game over'
        quit()

    print 'Oh mighty hero, will you?'
    print '1)', choice1Array[choiceCounter]
    print '2)', choice2Array[choiceCounter]
    print

    # User should be able to choose between two choices
    userChoice = raw_input('What will you decide: ')


    if userChoice == 'quit':
        quit()
    else:
        # clear the screen
        cls()
        if userChoice == '1':
            if choice1ResponseArray[choiceCounter] == '{store}':
                new_store = storeClass()
                new_store.createStore()
                new_item = new_store.get_purchased_item()
                print new_item.itemType
                userChoice = raw_input('What will you decide: ')

            else:
                print choice1ResponseArray[choiceCounter]
                choiceCounter += 1
        else:
            print choice2ResponseArray[choiceCounter]
            choiceCounter += 1
