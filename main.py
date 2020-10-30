import tkinter as tk
from Player import player
from Client import Client

root = tk.Tk()
#root.withdraw()

def func():
    client.func()

client = Client()
newButton = tk.Button(root,text='Im Done', width= 25, command=func)
newButton.pack()

top1 = tk.Toplevel(root)
player = player(top1, "p1")

root.mainloop()
