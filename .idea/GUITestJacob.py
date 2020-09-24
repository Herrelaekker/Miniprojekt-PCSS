from tkinter import *
from PIL import ImageTk,Image
from Unit import unit

root = Tk()

img = Image.open("Warrior.png")
img = img.resize((50,50))
my_img = ImageTk.PhotoImage(img)
my_label = Label(image=my_img)

img2 = img.resize((15,15))
my_img2 = ImageTk.PhotoImage(img2)

unitNum = 13
unitList = [unit(1,1,img)]*unitNum

teamList = [unit(3,3,img)]*0

# Første grid
row1 = 5
col1 = 5
for x in range(row1):
    for y in range(col1):
        newLabel = Label(image=my_img)
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
        newLabel = Label(image=my_img)
        newLabel.grid(row=x, column=y +col3)


def unitToTeam(indexNum):
    print(indexNum)
    teamList.append(unitList[indexNum])
    updateTeam()


def updateTeam():
    for x, u in enumerate(teamList):
        num = int(x/col1)
        newButton = Button(image=my_img)
        newButton.grid(row=num, column= x -(num*col1) +col3)


def myClick():
    for x, u in enumerate(unitList):
        num = int(x/col1)
        newButton = Button(image=my_img, command=lambda x=x: unitToTeam(x))
        newButton.grid(row=num, column= x -(num*col1) +1)


myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton.grid(row=2,column=0)
# myLabel.pack()

root.mainloop()