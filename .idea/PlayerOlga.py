import cv2 as cv
from Unit import unit
import os
import tkinter as tk
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


    team = [unit(1,2,img,""), unit(2,1,img,""), unit(3,3,img,""), unit(2,1,img,"")]

    def __init__(self):
        print(":D ")

        f = 'cards'

        for x, file in enumerate(os.listdir(f)):
            print(file)
            f_img = f + "/" + file
            tempImg = Image.open(f_img)
            tempImg = tempImg.resize((100,100))

            self.unitList[x].SetCard(tempImg)


        window = GUIWindow(self.unitList)


    def calcPower(self):
        self.totalPower = 0
        for x in range(len(self.team)):
            self.totalPower += self.team[x].getAttackPower()
            print(self.totalPower)

    def getTotalPower(self):
        self.calcPower()
        return self.totalPower

root = tk.Tk()
root.withdraw()

img=cv.imread("Warrior.png")
team=[unit(2,1,img,""),unit(3,2,img,"")]

p1 = player()
# p1.calcPower()
# print(p1.getTotalPower())

root.mainloop()