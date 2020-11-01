import tkinter as tk
from Player import player
from Client import Client
from Unit import unit
import threading

root = tk.Tk()
#root.withdraw()

pNum = ""
client = Client(pNum)
client.start()

def sendDoneMessage(list):
    rMsg = ""
    client.setTeam(list)
    client.setMsg("Done")


def checkIfDone():
    curDone = False
    while curDone is False:
        curDone = player.getCurDone()
        if curDone is not False:
            teamList = player.getTeam()
            sendDoneMessage(teamList)
            break


#newButton = tk.Button(root, text="I'm Done", width=25, command=lambda x="Done": sendMessage(x))
#newButton.pack()

#top1 = tk.Toplevel(root)
player = player(root)

threadDone = threading.Thread(target=checkIfDone)
threadDone.start()

root.mainloop()
