import cv2 as cv
from Unit import unit
class player(object):
    """
        player
    """

    totalPower = 0
    money = 10

    img = cv.imread("Warrior.png")

    cardGen = cardGenerator()
    unitGen = unitGenerator()
    unitGen.genUnits(cardGen,open('unitList.txt', 'r'))
    unitList = unitGen.getUnits()

    cards = [None]*0

    team = [unit(1,2,img,""), unit(2,1,img,""), unit(3,3,img,""), unit(2,1,img,"")]

    def __init__(self, team):
        print(":D ")
        self.team = team

        f = 'cards'

        for file in os.listdir(f):
            f_img = f + "/" + file
            tempImg = Image.open(f_img)
            self.cards.append(tempImg)
            

    def calcPower(self):
        self.totalPower = 0
        for x in range(len(self.team)):
            self.totalPower += self.team[x].getAttackPower()
            print(self.totalPower)

    def getTotalPower(self):
        self.calcPower()
        return self.totalPower


img=cv.imread("Warrior.png")
team=[unit(2,1,img,""),unit(3,2,img,"")]

p1 = player(team)
# p1.calcPower()
# print(p1.getTotalPower())
