from Store import Item

class PlayerClass:

    health = 100
    gold = 10
    attack = 1
    defense = 1
    items = []

    #armor = [('', 'Head'), ('', 'Sholders'), ('', 'Chest'), ('', 'Hands') ('', 'Legs'), ('', 'Feet')]
    #weapon = [('', 'Main Hand'), ('', 'OffHand')]

    def obtain_item(self, item):
        cost = item.cost
        if cost >= self.gold:
            self.items.append(item)
            self.gold - cost
        else:
            print "You do not have enough gold to purchase this item"
