from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import PIL
from Unit import unit
from PlayerOlga import *
from random import randrange
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class GUIWindow():

    #root = Tk()
    #root.withdraw()
    mainFrame = None

    img = Image.open("./UnitsJacob/Placeholder.png")
    img = img.resize((100, 100))
  #  phImg = ImageTk.PhotoImage(img)  # Photoimage er nødvendigt for at bruge det til knapper og labels

    img2 = img.resize((25, 100))
   # phImg2 = ImageTk.PhotoImage(img2)

    unitList = [unit(1, 1, "", "")] * 0  # Liste over units på venstre side
   # teamList = [unit(3, 3, "", "")] * 0  # Liste over units på højre side

    sortStr = ["Most Power", "Least Power", "Biggest Cost", "Smallest Cost"]
    curSortNum = len(sortStr) - 1  # Variabel der viser hvilken string vi er ved i sortStr-arrayet.

    row1 = 5  # Rækker af felter der skal laves
    col1 = 5  # Kolonner i første antal felter (Unit Listen)
    row2 = 2
    col2 = 1  # Kolonner i anden række (der skiller units og team)
    col3 = col1 + col2 + 1  # Kolonner i sidste antal felter (team listen)

    p = None
    #btn_text = tk.StringVar()

    # Laver en masse billeder som grid
    def printGrid(self):
        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = tk.Label(self.mainFrame,image=self.phImg)
                newLabel.grid(row=x, column=y + 1)

        # Grid der skiller de 2 grids
        for x in range(self.row1):
            for y in range(self.col2):
                newLabel = tk.Label(self.mainFrame,image=self.phImg2)
                newLabel.grid(row=x, column=y + self.col1 + 1)

        # Andet Grid
        for x in range(self.row2):
            for y in range(self.col1):
                newLabel = tk.Label(self.mainFrame,image=self.phImg)
                newLabel.grid(row=x, column=y + self.col3)

    def ShowUnitList(self):
        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = tk.Label(self.mainFrame,image=self.phImg)
                newLabel.grid(row=x, column=y + 1)
        for x, u in enumerate(self.unitList):
            btnImg = self.getBtnImage(self.unitList,x)

            # cv.imshow('g',btnImg)

            newButton = tk.Button(self.mainFrame,image=btnImg, command=lambda x=x: self.unitToTeam(x))
            newButton.image = btnImg
            num = int(x / self.col1)
            newButton.grid(row=num, column=x - (num * self.col1) + 1)
        self.mainFrame.pack()

    def getBtnImage(self,list, val):
        newIcon = list[val].getCard()
        newIcon = newIcon.resize((100,100))
        newImg = ImageTk.PhotoImage(image=newIcon)
        return newImg

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

    def sortBtnClicked(self):
        if self.curSortNum != 0:
            self.curSortNum -= 1
        else:
            self.curSortNum = len(self.sortStr) - 1
        print(self.curSortNum)
        self.btn_text.set(self.sortStr[self.curSortNum])
        self.SortUnits(self.unitList)

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

    def UpdateTeam(self):
        team = self.p.getTeam()
        for x in range(self.row2):
            for y in range(self.col1):
                newLabel = tk.Label(self.mainFrame,image=self.phImg)
                newLabel.grid(row=x, column=y + self.col3)

        for x, u in enumerate(team):
            btnImg = self.getBtnImage(team,x)

            newButton = tk.Button(self.mainFrame,image=btnImg, command=lambda x=x: self.removeTeamUnit(x))
            newButton.image = btnImg
            num = int(x / self.col1)
            newButton.grid(row=num, column=x - (num * self.col1) + self.col3)

    def removeTeamUnit(self,indexNum):
        self.p.removeFromTeamList(indexNum)
        self.UpdateTeam()

    def unitToTeam(self, indexNum):
        self.p.addToTeamList(self.unitList[indexNum])
        self.UpdateTeam()

    def __init__(self, unitList, master, p):
        self.p = p
        print(self.p.getName())
        self.root = master
        self.mainFrame = tk.Frame(self.root)

        self.phImg = ImageTk.PhotoImage(self.img)
        self.phImg2 = ImageTk.PhotoImage(self.img2)
        self.btn_text = tk.StringVar()

        self.printGrid()
        self.unitList = unitList
        self.ShowUnitList()

        # Tekst
        sortLabel = tk.Label(self.mainFrame,text="Sort By:")
        sortLabel.grid(row=6, column=3)

        self.btn_text = tk.StringVar()  # en variabel der kan ændres, gør så teksten på knappen kan opdateres.
        self.btn_text.set(self.sortStr[self.curSortNum])  # Tekst knappen viser i starten.

        sortBtn = tk.Button(self.mainFrame,textvariable=self.btn_text, command=self.sortBtnClicked)
        sortBtn.grid(row=7, column=3)
        self.mainFrame.pack()

    def getTeamList(self):
        return self.teamList