from tkinter import *
from PIL import ImageTk,Image
from Unit import unit
from random import randrange
import matplotlib.pyplot as plt

root = Tk()

img = Image.open("./UnitsJacob/Placeholder.png")
img = img.resize((100,100))
phImg = ImageTk.PhotoImage(img)

images = [Image.open("Warrior.png"), Image.open("./UnitsJacob/Ninja.png"), Image.open("./UnitsJacob/Chad.png")]

img2 = img.resize((25,100))
my_img2 = ImageTk.PhotoImage(img2)

unitNum = 13
unitList = [unit(1,1,images[randrange(3)])]*0

for x in range(unitNum):
    unitList.append(unit(1,1,images[randrange(3)]))

teamList = [unit(3,3,images[0])]*0

# Første grid
row1 = 5
col1 = 5
for x in range(row1):
    for y in range(col1):
        newLabel = Label(image=phImg)
        newLabel.grid(row=x, column=y + 1)

# Grid der skiller de 2 grids
col2 = 1
for x in range(row1):
    for y in range(col2):
        newLabel = Label(image=my_img2)
        newLabel.grid(row=x, column=y + col1 + 1)

# Andet Grid
col3 = col1+col2+1
for x in range(row1):
    for y in range(col1):
        newLabel = Label(image=phImg)
        newLabel.grid(row=x, column=y +col3)


def unitToTeam(indexNum):
    print(indexNum)
    teamList.append(unitList[indexNum])
    updateTeam()


def updateTeam():
    for x, u in enumerate(teamList):
        btnImg = getCurrentImage(teamList,x)

        newButton = Button(image=btnImg)
        newButton.image = btnImg
        num = int(x/col1) 
        newButton.grid(row=num, column= x -(num*col1) +col3)


# newIcon = unitList[0].getIcon()
# newIcon = newIcon.resize((100, 100))
# newImg = ImageTk.PhotoImage(newIcon)

newIcon = unitList[0].getIcon()
newImg = ImageTk.PhotoImage(newIcon)


def getCurrentImage(list, val):
    newIcon = list[val].getIcon()
    newIcon = newIcon.resize((100, 100))
    newImg = ImageTk.PhotoImage(newIcon)
    return newImg


def myClick():
    for x, u in enumerate(unitList):

        btnImg = getCurrentImage(unitList,x)

        newButton = Button(image=btnImg, command=lambda x=x: unitToTeam(x))
        newButton.image = btnImg
        num = int(x/col1)
        newButton.grid(row=num, column= x -(num*col1) +1)


plt.show()

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton.grid(row=2,column=0)
# myLabel.pack()

root.mainloop()