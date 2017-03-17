import user_input
import router
import os
from Player import PlayerClass

class narritive():

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    choice_counter = 0
    new_player_class = PlayerClass()
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
        print self.narritive_list[self.choice_counter][0][0]
        print self.narritive_list[self.choice_counter][1][0]
        print

        input_result = user_input.user_input(self.new_player_class)
        print router.take_input(input_result, self.narritive_list, self.choice_counter, self.new_player_class)
        self.choice_counter+=1

        print 'Press "c" to continue'
        user_input.user_input(self.new_player_class)
