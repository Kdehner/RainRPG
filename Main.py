
# while True:
#     print 'You are the one and only hero!'
#     print 'Destined to save the great land of Rain!'
#     print 'Please grace us with your name hero!'
#     print
#     name = raw_input('Enter your name: ')
#     print 'Hello ', name, 'welcome to your destiny!'
#     quit()







# Starting game logic here to prevent collisions

# Intro text
print 'You are the one and only hero!'
print 'Destined to save the great land of Rain!'
print 'Please grace us with your name hero!'
print

# Get user name
name = raw_input('Enter your name: ')
print 'Hello ', name, 'welcome to your destiny!'

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
        if userChoice == '1':
            print choice1ResponseArray[choiceCounter]
            choiceCounter += 1
        else:
            print choice2ResponseArray[choiceCounter]
            choiceCounter += 1
