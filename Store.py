class Item(object):
    """__init__() functions as the class constructor"""
    def __init__(self, itemName=None, itemType=None, cost=None):
        self.itemName = itemName
        self.itemType = itemType
        self.cost = cost

class storeClass:
    def createStore(self):
        print '+------------------------------------+'
        print '|        Welcome to the store!       |'
        print '+------------------------------------+'
        print
        itemList = []
        itemList.append(Item("Sword", "offence", 100))
        itemList.append(Item("Shield", "defence", 200))
        itemList.append(Item("Potion", "consumable", 300))

        for item in itemList:
            print "%s  %s  %s" % (item.itemName, item.itemType, item.cost)
        userChoice = raw_input('What do you want?: ')
