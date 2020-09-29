import cv2 as cv
from Unit import unit
import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
from JacobGUIWindow import GUIWindow
from PIL import Image
from OskarUnitGenerator import unitGenerator
from OskarCardGenerator import cardGenerator
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

    window = None
    window2 = None

    team = [unit(1,2,img,""), unit(2,1,img,""), unit(3,3,img,""), unit(2,1,img,"")]

    def __init__(self, master):
        print(":D ")

        f = 'cards'

        for x, file in enumerate(os.listdir(f)):
            print(file)
            f_img = f + "/" + file
            tempImg = Image.open(f_img)

            self.unitList[x].SetCard(tempImg)


        self.window = GUIWindow(self.unitList, master)
        #newWindow = tk.Toplevel(master)
        #self.window2 = GUIWindow(self.unitList, newWindow)

    def calcPower(self):
        self.totalPower = 0
        self.team = self.window.getTeamList()
        for x in range(len(self.team)):
            self.totalPower += self.team[x].getAttackPower()
            print(self.totalPower)

    def getTotalPower(self):
        self.calcPower()
        return self.totalPower

#root.withdraw()

#img=cv.imread("Warrior.png")
#team=[unit(2,1,img,""),unit(3,2,img,"")]


# p1.calcPower()
# print(p1.getTotalPower())
