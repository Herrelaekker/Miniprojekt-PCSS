from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from Unit import unit
from random import randrange
import matplotlib.pyplot as plt

root = Tk()

img = Image.open("UnitsJacob/Placeholder.png")
img = img.resize((100,100))
phImg = ImageTk.PhotoImage(img) # Photoimage er nødvnedigt for at bruge det til knapper og labels

images = [Image.open("Warrior.png"), Image.open("UnitsJacob/Ninja.png"), Image.open("UnitsJacob/Chad.png")]

img2 = img.resize((25,100))
my_img2 = ImageTk.PhotoImage(img2)

unitList = [unit(1,1,images[0],"")]*0 #Liste over units på venstre side
teamList = [unit(3,3,images[0],"")]*0 #Liste over units på højre side

unitList = [unit(2,1,images[0],""),unit(1,5,images[1],""),unit(10,2,images[2],""),]

row1 = 5 #Rækker af felter der skal laves
col1 = 5 #Kolonner i første antal felter (Unit Listen)
col2 = 1 #Kolonner i anden række (der skiller units og team)
col3 = col1 + col2 + 1 #Kolonner i sidste antal felter (team listen)

sortStr = ["Most Power","Least Power","Biggest Cost", "Smallest Cost"]
curSortNum = len(sortStr) -1 # Variabel der viser hvilken string vi er ved i sortStr-arrayet.

# Laver en masse billeder som grid
def printGrid():
    # Første grid
    for x in range(row1):
        for y in range(col1):
            newLabel = Label(image=phImg)
            newLabel.grid(row=x, column=y + 1)

    # Grid der skiller de 2 grids
    for x in range(row1):
        for y in range(col2):
            newLabel = Label(image=my_img2)
            newLabel.grid(row=x, column=y + col1 + 1)

    # Andet Grid
    for x in range(row1):
        for y in range(col1):
            newLabel = Label(image=phImg)
            newLabel.grid(row=x, column=y + col3)



# Tilføjer den unit man har trykket på til teamlisten.
def unitToTeam(indexNum):
    print(indexNum)
    teamList.append(unitList[indexNum])
    updateTeam()

# Opdaterer først hvert label med placeholderbilleder
# Så adder den knapper så det passer med hvor mange units der er i teamlisten.
def updateTeam():
    for x in range(row1):
        for y in range(col1):
            newLabel = Label(image=phImg)
            newLabel.grid(row=x, column=y + col3)

    for x, u in enumerate(teamList):
        btnImg = getBtnImage(teamList,x)

        newButton = Button(image=btnImg, command=lambda x=x: removeTeamUnit(x))
        newButton.image = btnImg
        num = int(x/col1) 
        newButton.grid(row=num, column= x -(num*col1) +col3)


# Fjerner den unit man har trykket på fra teamlisten.
def removeTeamUnit(indexNum):
    teamList.remove(teamList[indexNum])
    updateTeam()


# Tager billedeikonet fra en unit, resizer og laver den om til et format der kan bruges til knapper.
def getBtnImage(list, val):
    newIcon = list[val].getIcon()
    newIcon = newIcon.resize((100, 100))
    newImg = ImageTk.PhotoImage(newIcon)
    return newImg


# Viser alle alle unit-knapper fra unitlisten og sætter dem i grid
def showUnitList():
    # Første grid
    for x in range(row1):
        for y in range(col1):
            newLabel = Label(image=phImg)
            newLabel.grid(row=x, column=y + 1)
    for x, u in enumerate(unitList):

        btnImg = getBtnImage(unitList,x)

        newButton = Button(image=btnImg, command=lambda x=x: unitToTeam(x))
        newButton.image = btnImg
        num = int(x/col1)
        newButton.grid(row=num, column= x -(num*col1) +1)


# Sker når man clicker på sortknappen, ændre soreteringsmåden fundet i sortStr-arrayet
# Og sætter knappen string til at være det
def sortBtnClicked():
    global curSortNum
    global sortStr
    if curSortNum != 0:
        curSortNum -= 1
    else:
        curSortNum = len(sortStr)-1
    btn_text.set(sortStr[curSortNum])
    sortUnits(unitList)


# Laver (unit eller team)listen om til en sorteret udgave af sig selv ved at kalde funktionen GetUnit().
# I tilfælde af at man sorterer efter laveste er "HighestUnit" det laveste.
def sortUnits(list):
    global unitList
    global teamList
    tempList = list
    sortedList = [None]*0
    for x in range(len(list)):
        HighestUnit = tempList[0]
        HighestUnit = GetUnit(HighestUnit, list)

        sortedList.append(HighestUnit)
        tempList.remove(HighestUnit)

    unitList = sortedList
    showUnitList()


# GetUnit returnerer det "højeste unit"
# I tilfælde af at man leder efter det laveste unit får man det.
def GetUnit(HighestUnit,list):
    if (curSortNum == 0):
        for u in list:
            if u.getCost() > HighestUnit.getAttackPower():
                HighestUnit = u
    elif (curSortNum == 1):
        for u in list:
            if u.getCost() < HighestUnit.getAttackPower():
                HighestUnit = u
    elif (curSortNum == 2):
        for u in list:
            if u.getCost() > HighestUnit.getCost():
                HighestUnit = u
    elif (curSortNum == 3):
        for u in list:
            if u.getCost() < HighestUnit.getCost():
                HighestUnit = u
    else:
        print("ERROR")

    return HighestUnit

# Viser først grid, og bagefter units og teamet.
printGrid()
showUnitList()
updateTeam()

# Tekst
sortLabel = Label(text="Sort By:")
sortLabel.grid(row=6, column=3)


btn_text = tk.StringVar() # en variabel der kan ændres, gør så teksten på knappen kan opdateres.
btn_text.set(sortStr[curSortNum]) #Tekst knappen viser i starten.

sortBtn = Button(textvariable=btn_text, command=sortBtnClicked)
sortBtn.grid(row=7,column=3)
# sortBtnClicked(curSortNum)

root.mainloop()