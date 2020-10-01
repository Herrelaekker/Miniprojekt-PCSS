import cv2 as cv
from Unit import unit
import tkinter as tk
from PlayerOlga import player

img = cv.imread("Warrior.png")



def calcBattle():

    p1Score = p1.getTotalPower()
    p2Score = p2.getTotalPower()

    if (p1Score > p2Score):
        print(p1.getName() + " Wins!")
    else:
        print(p2.getName() + " Wins!")

    print("\n" + p1.getName() + " Score = " + str(p1Score) + "\n" + p2.getName() + " Score = " + str(p2Score))

def new_window():
    newWindow = tk.Toplevel(root)
    app = player(newWindow)

def printTeams():
    p1.printTeam()
    p2.printTeam()

root = tk.Tk()
root.withdraw()

top1 = tk.Toplevel(root)
p1 = player(top1,"p1")
top2 = tk.Toplevel(root)
p2 = player(top2,"p2")

top3 = tk.Toplevel(root)
frame = tk.Frame(top3)

btn = tk.Button(frame,width=25,height=10,text='Compare', command=calcBattle)
btn.pack()

btn2 = tk.Button(frame,width=25,height=5,text='printTeams', command=printTeams)
btn2.pack()

root.mainloop()