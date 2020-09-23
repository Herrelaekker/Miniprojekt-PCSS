import cv2 as cv
class unit(object):
    """
        unit
    """

    attackPower = 238
    cost = 10
    icon = cv.imread("Warrior.png")

    def __init__(self, cost, attackPower, icon):
        self.attackPower = attackPower
        self.cost = cost
        self.__icon = icon


    def getAttackPower(self):
        return self.attackPower


    def getCost(self):
        return self.cost


    def getIcon(self):
        return self.icon
