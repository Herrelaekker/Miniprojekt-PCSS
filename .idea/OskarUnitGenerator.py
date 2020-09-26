from PIL import Image, ImageDraw, ImageFont
from Unit import unit
from OskarCardGenerator import cardGenerator

class unitGenerator():

    unitList = open('unitList.txt', 'r')

    def __init__(self):
        self.unitList = open('unitList.txt', 'r')

    def genUnits(self, cardGenerator, unitList):


        for x, line in enumerate(unitList, 1):
            fileNumber = x
            split = line.split(", ")
            newUnit = unit(split[0], split[1], Image.open(split[2]), split[3])
            cardGen.createCard(newUnit, x)

            print (line)
            print(split[2])

    

newUnitList = open('unitList.txt', 'r')
testUnitGen = unitGenerator()
cardGen = cardGenerator()



testUnitGen.genUnits(cardGen, newUnitList)