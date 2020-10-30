from PIL import Image, ImageDraw, ImageFont
from Unit import unit
from CardGenerator import cardGenerator

class unitGenerator():

    unitList = open('unitList.txt', 'r')
    units = [unit(1,1,'',"")]*0

    def __init__(self):
        self.unitList = open('unitList.txt', 'r')

    def getUnits(self):
        return self.units

    #Genererer units ved hjælp af et cardGenerator objekt og en unitList (en .txt-fil).
    def genUnits(self, cardGenerator, unitList):

        #Kører igennem unitList'en én linje ad gangen og genererer et kort for hver linje med cardGen
        for x, line in enumerate(unitList, 1):
            fileNumber = x
            split = line.split(", ")
            newUnit = unit(split[0], split[1], Image.open(split[2]), split[3])
            self.units.append(newUnit)
            cardGenerator.createCard(newUnit, x)
