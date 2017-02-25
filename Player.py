class PlayerClass:

    health = 100
    gold = 100
    attack = 1
    defense = 1
    items = []

    #armor = [('', 'Head'), ('', 'Sholders'), ('', 'Chest'), ('', 'Hands') ('', 'Legs'), ('', 'Feet')]
    #weapon = [('', 'Main Hand'), ('', 'OffHand')]

    def obtain_item(self, item):
        cost = item.cost
        if cost <= self.gold:
            self.items.append(item)
            self.gold - cost
            print item.itemName, "was purchased!"
        else:
            print "You do not have enough gold to purchase this item"
