# coding=UTF-8
class PlayerClass:

    health = 20
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
        print 'Health' + '♥︎' * self.health

    def log_gold(self):
        print 'Gold' + self.gold

    def log_stats(self):
        print 'Attack: ' + self.attack
        print 'Defence: ' + self.defence

    def log_person(self):
        log_person_width = 20

        log_attack = 'Attack: ' + str(self.attack)
        log_defence = 'Defence: ' + str(self.defence)
        log_gold = 'Gold: ' + str(self.gold)
        log_health = 'Health: ' + '>' * self.health

        log_list = []
        log_list.append(log_attack)
        log_list.append(log_defence)
        log_list.append(log_gold)
        log_list.append(log_health)

        for log in log_list:
            if len(log) > log_person_width:
                log_person_width = len(log)


        log_title = 'Player Stats'

        print '+-' + '-' * log_person_width + '-+'
        print '| ' + log_title + ' ' * (log_person_width - len(log_title)) + ' |'
        print '| ' + ' ' * log_person_width + ' |'

        for log in log_list:
            print '| ' + log + ' ' * (log_person_width - len(log)) + ' |'

        print '+-' + '-' * log_person_width + '-+'

    def log_items(self):

        # Set up length vars
        itemCellWidth = 10;
        typeCellWidth = 10;

        # Calculate lengths
        for item in self.items:
            if len(item.itemName) > itemCellWidth:
                itemCellWidth = len(item.itemName)

            if len(item.itemType) > typeCellWidth:
                typeCellWidth = len(item.itemType)

        tTitle = 'Title' + ' ' * (itemCellWidth - len('Title'))
        tType = 'Type' + ' ' * (typeCellWidth - len('Type'))

        titles = '| ' + tTitle + ' | ' + tType + ' |'

        print '+' + '-' * len(titles) + '+'
        print titles

        # Print item list
        for item in self.items:
            iName = item.itemName + ' ' * (itemCellWidth - len(item.itemName))
            iType = item.itemType + ' ' * (typeCellWidth - len(item.itemType))

            print '| ' + iName + ' | ' + iType + ' |'

        print '+' + '-' * len(titles) + '+'
