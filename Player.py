class playerClass:

    def __init__(self, itemName, itemType):
        self.itemName = itemName
        self.itemType = itemType


    health = 100
    gold = 10
    attack = 1
    defense = 1
    items = []

    armor = [('', 'Head'), ('', 'Sholders'), ('', 'Chest'), ('', 'Hands') ('', 'Legs'), ('', 'Feet')]
    weapon = [('', 'Main Hand'), ('', 'OffHand')]
