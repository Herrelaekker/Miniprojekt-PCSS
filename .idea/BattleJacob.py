import cv2 as cv
from Unit import unit
import tkinter as tk
from PlayerOlga import player

img = cv.imread("Warrior.png")



def calcBattle():

    p1Score = p1.getTotalPower()
    p2Score = p2.getTotalPower()

    if (p1Score > p2Score):
        print("P1 Wins!")
    else:
        print("P2 Wins!")

    print("\n P1 Score = " + str(p1Score) + "\n P2 Score = " + str(p2Score))

def new_window():
    newWindow = tk.Toplevel(root)
    app = player(newWindow)

root = tk.Tk()

top1 = tk.Toplevel(root)
p1 = player(top1)
top2 =tk.Toplevel(root)
p2 = player(top2)

btn = tk.Button(width=25,height=10,text='Compare', command=calcBattle)
btn.pack()

root.mainloop()