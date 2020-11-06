import cv2 as cv
class unit(object):
    """
        unit
    """

    attackPower = 238
    cost = 10
    icon = cv.imread("testmappe/Warrior.png")
    name = 'default name'
    role = 0
    card = None

    def __init__(self, cost, attackPower, icon, name, role):
        self.cost = cost
        self.attackPower = attackPower
        self.icon = icon
        self.name = name
        self.role = role


    def getAttackPower(self):
        return int(self.attackPower)


    def getCost(self):
        return int(self.cost)


    def getIcon(self):
        return self.icon

    def getName(self):
        return self.name

    def getCard(self):
        return self.card

    def SetCard(self, card):
        self.card = card

    def getRole(self):
        return int(self.role)