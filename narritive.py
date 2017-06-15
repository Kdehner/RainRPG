import user_input
import router
import os
import sys


from Player import PlayerClass


class narritive():

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    choice_counter = 0
    new_player_class = PlayerClass()
    router.pass_instance(player=new_player_class)
    narritive_list = [
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
                [
                    [
                        'Fight Monster',
                        '{combat}'
                    ],
                    [
                        'Get going',
                        'You\'re heading out of town'
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

    def user_choice(self):

        self.cls()
        try:
            print self.narritive_list[self.choice_counter][0][0]
            print self.narritive_list[self.choice_counter][1][0]
            print
        except IndexError:
            print 'No more Choices'
            sys.exit()

        input_result = user_input.user_input()
        print router.take_input(input_result, self.narritive_list, self.choice_counter)
        self.choice_counter+=1

        print 'Press "c" to continue'
        user_input.user_input()
