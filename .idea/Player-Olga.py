import cv2 as cv
from Unit import unit
class player(object):
    """
        unit
    """

    totalPower = 0
    money = 10

    img = cv.imread("Warrior.png")

    team = [unit(1,2,img), unit(2,1,img), unit(3,3,img), unit(2,1,img)]

    def __init__(self, team):
        self.team = team


    def calcPower(self):
        self.totalPower = 0
        for x in range(len(self.team)):
            self.totalPower += self.team[x].getAttackPower()
            print(self.totalPower)

    def getTotalPower(self):
        return self.totalPower


img=cv.imread("Warrior.png")
team=[unit(2,1,img),unit(3,2,img)]

p1 = player(team)
p1.calcPower()
print(p1.getTotalPower())
