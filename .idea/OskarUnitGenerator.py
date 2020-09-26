from PIL import Image, ImageDraw, ImageFont
from Unit import unit
from OskarCardGenerator import cardGenerator

class unitGenerator():

    unitList = open('unitList.txt', 'r')

    def __init__(self):
        self.unitList = open('unitList.txt', 'r')

    #Genererer units ved hjælp af et cardGenerator objekt og en unitList (en .txt-fil).
    def genUnits(self, cardGenerator, unitList):

        #Kører igennem unitList'en én linje ad gangen og genererer et kort for hver linje med cardGen
        for x, line in enumerate(unitList, 1):
            fileNumber = x
            split = line.split(", ")
            newUnit = unit(split[0], split[1], Image.open(split[2]), split[3])
            cardGen.createCard(newUnit, x)
