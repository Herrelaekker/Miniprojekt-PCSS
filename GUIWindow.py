from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import PIL
from Unit import unit
from Player import *
from random import randrange
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from BubbleSort import BubbleSort

class GUIWindow():
    # root = Tk()
    # root.withdraw()
    mainFrame = None

    img = Image.open("testmappe/UnitsJacob/Placeholder.png")
    img = img.resize((150, 150))
    #  phImg = ImageTk.PhotoImage(img)  # Photoimage er nødvendigt for at bruge det til knapper og labels

    img2 = img.resize((25, 120))
    # phImg2 = ImageTk.PhotoImage(img2)

    sortStr = ["Most Power", "Least Power", "Biggest Cost", "Smallest Cost"]
    curSortNum = len(sortStr) - 1  # Variabel der viser hvilken string vi er ved i sortStr-arrayet.

    row1 = 8  # Rækker af felter der skal laves
    col1 = 5  # Kolonner i første antal felter (Unit Listen)
    row2 = 2
    col2 = 1  # Kolonner i anden række (der skiller units og team)
    col3 = col1 + col2 + 1  # Kolonner i sidste antal felter (team listen)

    # flag = 0

    p = None

    # btn_text = tk.StringVar()

    # Laver en masse billeder som grid
    def printGrid(self):
        self.frame_canvas = tk.Frame(self.mainFrame)
        self.frame_canvas.grid(row=0, column=1, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        self.frame_canvas.grid_propagate(False)

        self.canvas = tk.Canvas(self.frame_canvas)
        self.canvas.grid(row=0, column=0, sticky="news")

        self.vsb = tk.Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.frame_canvas.bind("<Configure>", self._on_frame_configure)

        self.frame_buttons = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor="nw")

      #  self.button_frame = tk.Frame(self.unitListCanvas)
     #   self.button_frame.grid(row=0, column=1, sticky='ns', padx=30)

      #  self.scrollBar = tk.Scrollbar(self.unitListCanvas, orient="vertical", command=self.unitListCanvas.yview)
      #  self.scrollBar.grid(row=0, column=10, sticky='ns')
        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = tk.Label(self.frame_buttons, image=self.phImg)
                newLabel.grid(row=x, column=y + 1,padx=5, pady=5, sticky="news")

        self.frame_canvas.config(width=850, height=900)

        self.canvas.config(scrollregion=self.frame_canvas.bbox("all"))
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        """ # Grid der skiller de 2 grids
        for x in range(self.row1):
            for y in range(self.col2):
                newLabel = tk.Label(self.mainFrame, image=self.phImg2)
                newLabel.grid(row=x, column=y + self.col1 + 1,padx=5, pady=5, sticky='news')"""

        self.teamListFrame = Frame(self.mainFrame)
        self.teamListFrame.grid(row=0, column=2, sticky='ns')
        # Andet Grid
        for x in range(self.row2):
            for y in range(self.col1):
                newLabel = tk.Label(self.teamListFrame, image=self.phImg)
                newLabel.grid(row=x, column=y + self.col3,padx=5, pady=5, sticky='news')

    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def ShowUnitList(self):
        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = tk.Label(self.frame_buttons, image=self.phImg)
                newLabel.grid(row=x, column=y + 1, padx=5, pady=5)
        for x, u in enumerate(self.unitList):
            btnImg = self.getBtnImage(self.unitList, x, (150, 150))

            # cv.imshow('g',btnImg)

            newButton = tk.Button(self.frame_buttons, image=btnImg, command=lambda x=x: self.unitToTeam(x))
            newButton.image = btnImg
            num = int(x / self.col1)
            newButton.grid(row=num, column=x - (num * self.col1) + 1,padx=5, pady=5)
        self.mainFrame.pack()

    def getBtnImage(self, list, val, size):
        newIcon = list[val].getCard()
        newIcon = newIcon.resize(size)
        newImg = ImageTk.PhotoImage(image=newIcon)
        return newImg

    def UnitSwap(self, index):
        tempVal = self.unitList[index]
        self.unitList[index] = self.unitList[index + 1]
        self.unitList[index + 1] = tempVal
        self.flag += 1

    # CurSortNum = "Most Power", "Least Power", "Biggest Cost", "Smallest Cost"
    # BubbleSort
    def SortUnits(self):
        self.unitList = self.bSort.SortUnits(self.curSortNum, self.unitList).copy()
        self.ShowUnitList()

    def sortBtnClicked(self):
        if self.curSortNum != 0:
            self.curSortNum -= 1
        else:
            self.curSortNum = len(self.sortStr) - 1
        print(self.curSortNum)
        self.btn_text.set(self.sortStr[self.curSortNum])
        self.SortUnits()


    # Vi fjerner de irrelevante units, og gemmer dem i tempList
    # Når vi Searcher igen tilføjer vi i starten tempList, så udgangspunktet er i den fulde liste.
    def Search(self):

        for x in range(len(self.tempList)):
            self.unitList.append(self.tempList[x])

        #  print(str(len(self.unitListStart)) + " " + str(len(self.unitList)))
        tempStr = self.searchBar.get()
        self.tempList = []
        print(tempStr)
        for x in range(len(self.unitList)):  # 0-2
            if self.unitList[x].getName().count(tempStr) <= 0:
                self.tempList.append(self.unitList[x])

        for x in range(len(self.tempList)):
            self.unitList.remove(self.tempList[x])

        self.SortUnits()

    def UpdateTeam(self):
        team = self.p.getTeam()
        for x in range(self.row2):
            for y in range(self.col1):
                newLabel = tk.Label(self.teamListFrame, image=self.phImg)
                newLabel.grid(row=x, column=y + self.col3,padx=5, pady=5)

        for x, u in enumerate(team):
            btnImg = self.getBtnImage(team, x, (150, 150))

            newButton = tk.Button(self.teamListFrame, image=btnImg, command=lambda x=x: self.removeTeamUnit(x))
            newButton.image = btnImg
            num = int(x / self.col1)
            newButton.grid(row=num, column=x - (num * self.col1) + self.col3,padx=5, pady=5)

    def removeTeamUnit(self, indexNum):
        moneyAdded = self.p.getTeam()[indexNum].getCost()
        self.p.addMoney(moneyAdded)
        self.money += moneyAdded
        self.money_text.set("Money: " + str(self.money))
        self.p.removeFromTeamList(indexNum)
        self.UpdateTeam()

    def unitToTeam(self, indexNum):
        moneySubtracted = self.unitList[indexNum].getCost()
        if moneySubtracted <= self.money and len(self.p.getTeam()) < 10:
            self.p.addMoney(-moneySubtracted)
            self.money -= moneySubtracted
            self.money_text.set("Money: " + str(self.money))
            self.p.addToTeamList(self.unitList[indexNum])
            self.UpdateTeam()

    def doneBtnClicked(self):
        main = self.p.getMain()
        main.doneButtonClicked()

        fontStyle = tkFont.Font(family="Lucida Grande", size=48)
        self.waitingLabel = tk.Label(self.otherWindow, text="Waiting for other player...", font=fontStyle)
        self.waitingLabel.grid(row=1, column=2)

        self.otherWindow.deiconify()

        """team = self.p.getTeam()
        newArray = []
        for x in range(2):
            newArray.append(team)
        print(newArray)
        score1 = 376
        score2 = 543
        self.SetBattleWindow(newArray, score1, score2)"""


    def SetBattleWindow(self, playerTeams, playerScore1, playerScore2):
        self.waitingLabel.destroy()

        for y in range(2):
            for x in range(len(playerTeams[y])):
                labelImg = self.getBtnImage(playerTeams[y], x, (150, 150))
                num = int(x / self.col1)
                newLabel = tk.Label(self.otherWindow, image=labelImg)
                newLabel.image = labelImg
                # newLabel.grid(row=num, column=x - (num * self.col1) + 1)

                num = int(x / self.col1)
                # newLabel.place(x=(x*50-5*50*num),y=(num*50))
                if y == 1 and num == 0:
                    newLabel.grid(row=2 + num + y * 2, column=x - (num * self.col1) + 2, padx=5, pady=20)
                else:
                    newLabel.grid(row=2 + num + y*2, column=x - (num * self.col1) + 2,padx=5, pady=5)
                # canvas.create_image(x*50, num*50,anchor=NW,image=img)

        fontStyle = tkFont.Font(family="Lucida Grande", size=24)

        Player1Label = tk.Label(self.otherWindow, text="Player 1", font=fontStyle)
        Player1Label.grid(row=2, column=1)
        Player2Label = tk.Label(self.otherWindow, text="Player 2", font=fontStyle)
        Player2Label.grid(row=4, column=1)

        pScore1Lbl = tk.Label(self.otherWindow, text="Power: " + str(playerScore1), font=fontStyle)
        pScore1Lbl.grid(row=2, column=8)
        pScore2Lbl = tk.Label(self.otherWindow, text="Power: " + str(playerScore2), font=fontStyle)
        pScore2Lbl.grid(row=4, column=8)

     #   self.otherWindow.deiconify()


    def __init__(self, unitList, master, p):
        self.done = False
        self.p = p
        self.money = p.getMoney()
        self.root = master
        self.mainFrame = tk.Frame(self.root)
        self.otherWindow = tk.Toplevel(self.root)
        self.otherWindow.withdraw()

        self.phImg = ImageTk.PhotoImage(self.img)
        self.phImg2 = ImageTk.PhotoImage(self.img2)
        self.btn_text = tk.StringVar()
       # self.canvas = tk.Canvas(self.mainFrame, bg="yellow")
        #self.canvas.create_window((0, 0), window=self.button_frame, anchor='nw')

        self.printGrid()
        self.unitList = unitList.copy()
        self.tempList = []
        self.bSort = BubbleSort(unitList.copy())
        self.SortUnits()
        self.ShowUnitList()

        # Tekst
        sortLabel = tk.Label(self.mainFrame, text="Sort By:")
        sortLabel.grid(row=6, column=3)

        self.btn_text = tk.StringVar()  # en variabel der kan ændres, gør så teksten på knappen kan opdateres.
        self.btn_text.set(self.sortStr[self.curSortNum])  # Tekst knappen viser i starten.

        sortBtn = tk.Button(self.mainFrame, textvariable=self.btn_text, command=self.sortBtnClicked)
        sortBtn.grid(row=7, column=3)

        self.money_text = tk.StringVar()
        self.money_text.set("Money: " + str(self.money))

        moneyLabel = tk.Label(self.mainFrame, textvariable=self.money_text)
        moneyLabel.grid(row=6, column=2)

        doneBtn = tk.Button(self.mainFrame, text="Done!", command=self.doneBtnClicked, font=24)
        doneBtn.grid(row=4, column=9)

        self.searchBar = tk.Entry(self.mainFrame)
        self.searchBar.grid(row=8, column=3)

        self.searchBtn = tk.Button(self.mainFrame, text='Search', command=self.Search)
        self.searchBtn.grid(row=8, column=4)
        self.mainFrame.pack()


