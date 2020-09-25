import cv2 as cv
class unit(object):
    """
        unit
    """

    attackPower = 238
    cost = 10
    icon = cv.imread("Warrior.png")
    name = 'default name'

    def __init__(self, cost, attackPower, icon, name):
        self.cost = cost
        self.attackPower = attackPower
        self.icon = icon
        self.name = name


    def getAttackPower(self):
        return self.attackPower


    def getCost(self):
        return self.cost


    def getIcon(self):
        return self.icon

    def getName(self):
        return self.name