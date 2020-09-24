from tkinter import *
from PIL import ImageTk,Image

root = Tk()

img = Image.open("Warrior.png")
img = img.resize((50,50))
my_img = ImageTk.PhotoImage(img)
my_label = Label(image=my_img)

def myClick():
    for x in range(5):
        for y in range(5):
            newButton = Button(image=my_img)
            newButton.grid(row=x, column=y+1)


# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=0)

myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="red")
myButton.grid(row=2,column=0)
# myLabel.pack()

root.mainloop()