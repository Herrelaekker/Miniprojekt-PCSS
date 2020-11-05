import tkinter as tk
from Player import player
from ClientNew import Client
from Unit import unit
import threading

class main(object):
    # root.withdraw()
    def __init__(self, root):
        self.root = root
        self.pNum = ""
        self.player = player(self.root, self)

    def startClient(self):
        self.client = Client(self.pNum, self)
        self.client.start()

    def doneButtonClicked(self):
        self.client.setTeam(self.player.getTeam())
        self.client.sendMessage("Done")

    #newButton = tk.Button(root, text="I'm Done", width=25, command=lambda x="Done": sendMessage(x))
    #newButton.pack()

    #top1 = tk.Toplevel(root)

    #threadDone = threading.Thread(target=checkIfDone)
    #threadDone.start()

root = tk.Tk()
m = main(root)
m.startClient()
root.mainloop()