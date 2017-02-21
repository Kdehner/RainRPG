class Item(object):
    """__init__() functions as the class constructor"""
    def __init__(self, itemName=None, itemType=None, cost=None):
        self.itemName = itemName
        self.itemType = itemType
        self.cost = cost

class storeClass:

    itemCellWidth = 10;
    typeCellWidth = 10;
    costCellWidth = 10;

    itemList = []
    itemList.append(Item("Sword", "offence", 10000000000))
    itemList.append(Item("Shieldaaaaaaaaa", "defence", 200))
    itemList.append(Item("Potion", "consumableeeeeeeeeeee", 300))

    for item in itemList:
        if len(item.itemName) > itemCellWidth:
            itemCellWidth = len(item.itemName)

        if len(item.itemType) > typeCellWidth:
            typeCellWidth = len(item.itemType)

        if len(str(item.cost)) > costCellWidth:
            costCellWidth = len(str(item.cost))

    def createStore(self):
        totleWidth = self.itemCellWidth + self.typeCellWidth + self.costCellWidth + 8

        welcome = "Welcome to the shop!"
        welcomeMargin = ((totleWidth - len(welcome))/2)

        print '+' + '-' * totleWidth + '+'
        print '|' + ' ' * totleWidth + '|'
        print '|' + ' ' *  welcomeMargin + welcome + ' ' *  welcomeMargin + '|'
        print '|' + ' ' * totleWidth + '|'
        print '+' + '-' * totleWidth + '+'

        tTitle = 'Title' + ' ' * (self.itemCellWidth - len('Title'))
        tType = 'Type' + ' ' * (self.typeCellWidth - len('Type'))
        tCost = 'Cost' + ' ' * (self.costCellWidth - len('Cost'))

        print '| ' + tTitle + ' | ' + tType + ' | ' + tCost + ' |'

        print '+' + '-' * totleWidth + '+'

        for item in self.itemList:
            iName = item.itemName + ' ' * (self.itemCellWidth - len(item.itemName))
            iType = item.itemType + ' ' * (self.typeCellWidth - len(item.itemType))
            iCost = str(item.cost) + ' ' * (self.costCellWidth - len(str(item.cost)))

            print '| ' + iName + ' | ' + iType + ' | ' + iCost + ' |'

        print '+' + '-' * totleWidth + '+'
        print
        userChoice = raw_input('What do you want?: ')
