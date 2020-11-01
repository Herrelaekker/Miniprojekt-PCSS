import tkinter as tk
from Player import player
from Client import Client
import threading

root = tk.Tk()
root.withdraw()

pNum = ""
client = Client(pNum)
client.start()

while pNum == "":
    pNum = client.getName()


def sendMessage(msg):
    rMsg = ""
    client = Client(pNum)
    client.start()
    client.setMsg(msg)
    while rMsg == "":
        rMsg = client.getName()


def checkIfDone():
    curDone = False
    while curDone is False:
        curDone = player.getCurDone()
        if curDone is not False:
            sendMessage("Done")


newButton = tk.Button(root, text="I'm Done", width=25, command=lambda x="Done": sendMessage(x))
newButton.pack()

top1 = tk.Toplevel(root)
player = player(top1)

threadDone = threading.Thread(target=checkIfDone)
threadDone.start()

root.mainloop()
