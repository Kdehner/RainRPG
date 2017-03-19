class Item(object):
    #__init__() functions as the class constructor
    def __init__(self, item_name=None, item_type=None, cost=None):
        self.item_name = item_name
        self.item_type = item_type
        self.cost = cost

class storeClass:
    import router

    def __init__(self):
        self.player = self.router.get_instance('player')

    purchased_item = None

    # Set up length vars
    item_cell_width = 10;
    type_cell_width = 10;
    cost_cell_width = 10;

    # Create item list
    item_list = []
    item_list.append(Item("Sword", "offence", 100))
    item_list.append(Item("Shield", "defence", 200))
    item_list.append(Item("Potion", "consumable", 300))
    item_list.append(Item("Lance", "offence", 100))
    item_list.append(Item("Super Awesome Sharp Thing", "offence", 2000))
    item_list.append(Item("The Unbreakable Wall", "offence", 300000))

    # Calculate lengths
    for item in item_list:
        if len(item.item_name) > item_cell_width:
            item_cell_width = len(item.item_name)

        if len(item.item_type) > type_cell_width:
            type_cell_width = len(item.item_type)

        if len(str(item.cost)) > cost_cell_width:
            cost_cell_width = len(str(item.cost))

    def set_purchased_item(self, item):
        self.purchased_item = item

    def get_purchased_item(self):
        return self.purchased_item

    def createStore(self):

        total_width = self.item_cell_width + self.type_cell_width + self.cost_cell_width + 8

        welcome_message = "Welcome to the Shop!"
        total_gold = "Player Gold: " + str(self.player.gold)
        welcome_margin = ((total_width - len(welcome_message))/2)
        odd_round = 0 if total_width % 2 == 0 else 1

        # Print store welcome banner
        print '+' + '-' * total_width + '+'
        print '|' + ' ' * total_width + '|'
        print '|' + (' ' *  welcome_margin) + welcome_message + (' ' *  (welcome_margin + odd_round)) + '|'
        print '|' + ' ' * total_width + '|'
        print '+' + '-' * total_width + '+'
        print '| ' + total_gold + ' ' * (total_width - len(total_gold) - 1) + '|'
        print '+' + '-' * total_width + '+'

        # Print column headers
        tTitle = 'Title' + ' ' * (self.item_cell_width - len('Title'))
        tType = 'Type' + ' ' * (self.type_cell_width - len('Type'))
        tCost = 'Cost' + ' ' * (self.cost_cell_width - len('Cost'))

        print '| ' + tTitle + ' | ' + tType + ' | ' + tCost + ' |'

        print '+' + '-' * total_width + '+'

        # Print item list
        for item in self.item_list:
            iName = item.item_name + ' ' * (self.item_cell_width - len(item.item_name))
            iType = item.item_type + ' ' * (self.type_cell_width - len(item.item_type))
            iCost = str(item.cost) + ' ' * (self.cost_cell_width - len(str(item.cost)))

            print '| ' + iName + ' | ' + iType + ' | ' + iCost + ' |'

        print '+' + '-' * total_width + '+'
        print

        user_choice = raw_input('Make a selection: ')
        self.set_purchased_item(self.item_list[0])
        self.player.obtain_item(self.purchased_item)
