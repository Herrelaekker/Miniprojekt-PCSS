import os
from tkinter import *
from GUIWindow import GUIWindow
from PIL import Image
from UnitGenerator import unitGenerator
from CardGenerator import cardGenerator

class player(object):
    """
        player
    """

    totalPower = 0
    money = 1000

    cardGen = cardGenerator()
    unitGen = unitGenerator()
    unitGen.genUnits(cardGen,open('unitList.txt', 'r'))
    unitList = unitGen.getUnits()
   # playerClient = Client()

   #  window2 = None

    team = []

    def __init__(self, master, main):
        # Sætter hvert unit's card til at være det tilsvarende fra mappen "cards".
        f = 'cards'
        for x, file in enumerate(os.listdir(f)):
            # print(file)
            f_img = f + "/" + file
            tempImg = Image.open(f_img)

            self.unitList[x].SetCard(tempImg)

        print("cards added")
        self.main = main
        self.window = GUIWindow(self.unitList, master, self)

    def getMain(self):
        return self.main

    def getTeam(self):
        return self.team

    def getMoney(self):
        return self.money

    def addMoney(self, val):
        self.money += val

    def addToTeamList(self, u):
        self.team.append(u)

    def removeFromTeamList(self,indexNum):
        self.team.remove(self.team[indexNum])

    def getGUIWindow(self):
        return self.window

    def getUnitList(self):
        return self.unitList