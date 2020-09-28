from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import PIL
from Unit import unit
from random import randrange
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class GUIWindow():

    root = tk.Toplevel()
    root.withdraw()

    img = Image.open("./UnitsJacob/Placeholder.png")
    img = img.resize((100, 100))
    phImg = ImageTk.PhotoImage(img)  # Photoimage er nødvendigt for at bruge det til knapper og labels

    img2 = img.resize((25, 100))
    phImg2 = ImageTk.PhotoImage(img2)

    unitList = [unit(1, 1, "", "")] * 0  # Liste over units på venstre side
    teamList = [unit(3, 3, "", "")] * 0  # Liste over units på højre side

    sortStr = ["Most Power", "Least Power", "Biggest Cost", "Smallest Cost"]
    curSortNum = len(sortStr) - 1  # Variabel der viser hvilken string vi er ved i sortStr-arrayet.

    row1 = 5  # Rækker af felter der skal laves
    col1 = 5  # Kolonner i første antal felter (Unit Listen)
    col2 = 1  # Kolonner i anden række (der skiller units og team)
    col3 = col1 + col2 + 1  # Kolonner i sidste antal felter (team listen)

    def SetUnitList(self, unitList):
        self.unitList = unitList
        self.SortUnits(unitList)

    # Laver en masse billeder som grid
    def printGrid(self):
        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = Label(image=self.phImg)
                newLabel.grid(row=x, column=y + 1)

        # Grid der skiller de 2 grids
        for x in range(self.row1):
            for y in range(self.col2):
                newLabel = Label(image=self.phImg2)
                newLabel.grid(row=x, column=y + self.col1 + 1)

        # Andet Grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = Label(image=self.phImg)
                newLabel.grid(row=x, column=y + self.col3)

    def ShowUnitList(self):
        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = Label(image=self.phImg)
                newLabel.grid(row=x, column=y + 1)
        for x, u in enumerate(self.unitList):
            btnImg = self.getBtnImage(self.unitList, x)

            newButton = Button(image=btnImg, command=lambda x=x: unitToTeam(x))
            newButton.image = btnImg
            num = int(x / self.col1)
            newButton.grid(row=num, column=x - (num * self.col1) + 1)

    def getBtnImage(self, list, val):
        newIcon = list[val].getIcon()
        cv.resize(newIcon,(100,100))
        newImg = ImageTk.PhotoImage(image=PIL.Image.fromarray(newIcon))
        #return newImg

    def SortUnits(self, list):
        tempList = list
        sortedList = [None] * 0
        for x in range(len(list)):
            HighestUnit = tempList[0]
            HighestUnit = self.GetUnit(HighestUnit, list)

            sortedList.append(HighestUnit)
            tempList.remove(HighestUnit)

        self.unitList = sortedList
        self.ShowUnitList()

    def GetUnit(self, HighestUnit, list):
        if (self.curSortNum == 0):
            for u in list:
                if u.getCost() > HighestUnit.getAttackPower():
                    HighestUnit = u
        elif (self.curSortNum == 1):
            for u in list:
                if u.getCost() < HighestUnit.getAttackPower():
                    HighestUnit = u
        elif (self.curSortNum == 2):
            for u in list:
                if u.getCost() > HighestUnit.getCost():
                    HighestUnit = u
        elif (self.curSortNum == 3):
            for u in list:
                if u.getCost() < HighestUnit.getCost():
                    HighestUnit = u
        else:
            print("ERROR")

        return HighestUnit

    def __init__(self):
        self.printGrid()


root = tk.Tk()
root.withdraw()
window = GUIWindow()
l = [unit(1,1,cv.imread("Warrior.png"),"")]
window.SetUnitList(l)
root.mainloop()