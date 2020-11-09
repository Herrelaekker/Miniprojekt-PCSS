import tkinter as tk
from Player import player
from Client import Client

class main(object):

    def __init__(self, root):
        self.root = root
        self.pNum = ""
        self.player = player(self.root, self)

    # Laver en client som thread, som kan sende og modtager beskeder til og fra serveren.
    def startClient(self):
        self.client = Client(self.pNum, self)
        self.client.start()

    # Sender beskeden Done til serveren.
    def doneButtonClicked(self):
        totalPower = self.player.getTotalPower()
        print(totalPower)
        self.client.setTeamToNames(self.player.getTeam())
        self.client.sendMessage("Done")

    def getPlayer(self):
        return self.player

# Laver en main Window som kommer til at indeholde alt GUI.
root = tk.Tk()

# Laver et main-objekt, og starter clienten op gennem funktionen startClient().
m = main(root)
m.startClient()

# Kører ind til vinduet er lukket ned
root.mainloop()