from monster import Monster

class Combat():
    import router

    def __init__(self):
        self.player = self.router.get_instance('player')
        self.monster = Monster()

    def combat(self):
        while True:

            if self.player.health < 0:
                print('You Died!')
                quit()

            elif self.monster.health < 0:
                print('You have defeated the monster!')
                self.player.gold += 500
                break

            else:
                self.player.health -= (self.monster.attack - self.player.defence)
                self.monster.health -= self.player.attack
