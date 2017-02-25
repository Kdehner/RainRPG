class PlayerClass:

    health = 98
    gold = 100
    attack = 1
    defence = 1
    items = []

    #armor = [('', 'Head'), ('', 'Sholders'), ('', 'Chest'), ('', 'Hands') ('', 'Legs'), ('', 'Feet')]
    #weapon = [('', 'Main Hand'), ('', 'OffHand')]

    #When purchasing an item check player gold vs. cost of item and add appropriate buffs.
    def obtain_item(self, item):
        item_name = item.itemName
        item_type = item.itemType
        item_cost = item.cost
        item_purchased = False

        if item_cost <= self.gold:
            self.items.append(item)
            self.gold -= item_cost
            print item.itemName, "was purchased!"
            item_purchased = True
        else:
            print "You do not have enough gold to purchase this item"

        #If item is offence add attack point
        if item_purchased is True and item_type is 'offence':
            self.attack += 1
            print self.attack

        #If item is defence add defence point
        elif item_purchased is True and item_type is 'defence':
            self.defence += 1

    def log_health(self):
        print 'Health'
        print '❤️' * self.health
