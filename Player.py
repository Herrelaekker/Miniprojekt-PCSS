import cv2 as cv
from Unit import unit
import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
from GUIWindow import GUIWindow
from PIL import Image
from UnitGenerator import unitGenerator
from CardGenerator import cardGenerator
class player(object):
    """
        player
    """

    totalPower = 0
    money = 10

    cardGen = cardGenerator()
    unitGen = unitGenerator()
    unitGen.genUnits(cardGen,open('unitList.txt', 'r'))
    unitList = unitGen.getUnits()

    window = None
   #  window2 = None

    team = [None]*0

    name = ""

    def __init__(self, master, name):
        print(":D ")

        f = 'cards'

        for x, file in enumerate(os.listdir(f)):
            print(file)
            f_img = f + "/" + file
            tempImg = Image.open(f_img)

            self.unitList[x].SetCard(tempImg)
        self.name = name
        #print(self.name)

        self.window = GUIWindow(self.unitList, master, self)
        #newWindow = tk.Toplevel(master)
        #self.window2 = GUIWindow(self.unitList, newWindow)

    def printTeam(self):
        print("added to" + self.name)
        for x in range(len(self.team)):
            print(self.team[x].getName())

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def addToTeamList(self, u):
        self.team.append(u)
       # self.printTeam()

    def removeFromTeamList(self,indexNum):
        self.team.remove(self.team[indexNum])

    def calcPower(self):
        self.totalPower = 0
        #self.team = self.window.getTeamList()
        for x in range(len(self.team)):
            self.totalPower += self.team[x].getAttackPower()
            print(self.team[x].getAttackPower())

    def getTotalPower(self):
        self.calcPower()
        return self.totalPower

#root.withdraw()

#img=cv.imread("Warrior.png")
#team=[unit(2,1,img,""),unit(3,2,img,"")]


# p1.calcPower()
# print(p1.getTotalPower())
