class Item(object):
    #__init__() functions as the class constructor
    def __init__(self, itemName=None, itemType=None, cost=None):
        self.itemName = itemName
        self.itemType = itemType
        self.cost = cost

class storeClass:
    from Player import PlayerClass
    purchased_item = None

    # Set up length vars
    itemCellWidth = 10;
    typeCellWidth = 10;
    costCellWidth = 10;

    # Create item list
    itemList = []
    itemList.append(Item("Sword", "offence", 100))
    itemList.append(Item("Shield", "defence", 200))
    itemList.append(Item("Potion", "consumable", 300))
    itemList.append(Item("Lance", "offence", 100))
    itemList.append(Item("Super Awesome Sharp Thing", "offence", 2000))
    itemList.append(Item("The Unbreakable Wall", "offence", 300000))

    # Calculate lengths
    for item in itemList:
        if len(item.itemName) > itemCellWidth:
            itemCellWidth = len(item.itemName)

        if len(item.itemType) > typeCellWidth:
            typeCellWidth = len(item.itemType)

        if len(str(item.cost)) > costCellWidth:
            costCellWidth = len(str(item.cost))

    def set_purchased_item(self, item):
        self.purchased_item = item

    def get_purchased_item(self):
        return self.purchased_item

    def createStore(self):

        totalWidth = self.itemCellWidth + self.typeCellWidth + self.costCellWidth + 8

        welcomeMessage = "Welcome to the Shop!"
        total_gold = "Player Gold: " + str(self.PlayerClass().gold)
        welcomeMargin = ((totalWidth - len(welcomeMessage))/2)
        oddRound = 0 if totalWidth % 2 == 0 else 1

        # Print store welcome banner
        print '+' + '-' * totalWidth + '+'
        print '|' + ' ' * totalWidth + '|'
        print '|' + (' ' *  welcomeMargin) + welcomeMessage + (' ' *  (welcomeMargin + oddRound)) + '|'
        print '|' + ' ' * totalWidth + '|'
        print '+' + '-' * totalWidth + '+'
        print '| ' + total_gold + ' ' * (totalWidth - len(total_gold) - 1) + '|'
        print '+' + '-' * totalWidth + '+'

        # Print column headers
        tTitle = 'Title' + ' ' * (self.itemCellWidth - len('Title'))
        tType = 'Type' + ' ' * (self.typeCellWidth - len('Type'))
        tCost = 'Cost' + ' ' * (self.costCellWidth - len('Cost'))

        print '| ' + tTitle + ' | ' + tType + ' | ' + tCost + ' |'

        print '+' + '-' * totalWidth + '+'

        # Print item list
        for item in self.itemList:
            iName = item.itemName + ' ' * (self.itemCellWidth - len(item.itemName))
            iType = item.itemType + ' ' * (self.typeCellWidth - len(item.itemType))
            iCost = str(item.cost) + ' ' * (self.costCellWidth - len(str(item.cost)))

            print '| ' + iName + ' | ' + iType + ' | ' + iCost + ' |'

        print '+' + '-' * totalWidth + '+'
        print

        userChoice = raw_input('Make a selection: ')
        self.set_purchased_item(self.itemList[0])
        self.PlayerClass().obtain_item(self.purchased_item)
