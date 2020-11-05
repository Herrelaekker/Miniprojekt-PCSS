import socket
import os
import subprocess
import threading
import pickle

class Client(threading.Thread):

    def __init__(self, pNum, main):
        threading.Thread.__init__(self)
        self.pNum = pNum
        self.msg = ""
        self.team = []
        self.main = main
        self.msgNum = 0
        self.playerTeams = []
        self.playerScores = [0, 0]

    def run(self):
        self.s = socket.socket()
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 9999

        self.s.connect((self.host, self.port))
        print("The client has been connected")

        thread = threading.Thread(target=self.listen)
        thread.daemon = True
        thread.start()

    def setTeamToNames(self, team):
        self.team = [None]*len(team)
        for x in range(len(team)):
            self.team[x] = team[x].getName()

    def setNamesToTeam(self):
        self.unitList = self.main.getPlayer().getUnitList()
        for x in range(2):
            for y in range(len(self.playerTeams[x])):
                for z in range(len(self.unitList)):
                    if self.playerTeams[x][y] == self.unitList[z].getName():
                        self.playerTeams[x][y] = self.unitList[z]
                        break
        print(self.playerTeams)

    def listen(self):
        while True:
            msg = self.s.recv(10000)
            list = pickle.loads(msg)
            print(list)
            self.msgNum += 1
            self.ReceiveMessage(list)

            """
            print("listening...")
            # global playersReady
            # if playersReady[num] is False:
            msg0 = self.s.recv(10000)
            msg1 = self.s.recv(10000)
            msgPower = self.s.recv(10000)
            self.list0 = pickle.loads(msg0)
            self.list1 = pickle.loads(msg1)
            self.totalPower = pickle.loads(msgPower)
            print(self.list0)
            print(self.list1)
            print(self.totalPower)
            print("Player 1:" + str(self.totalPower[0]))
            print("Player 2:" + str(self.totalPower[1]))"""

    def ReceiveMessage(self, msg):
        if self.msgNum == 1 or self.msgNum == 2:
            self.playerTeams.append(msg)
        elif self.msgNum == 3:
            self.playerScores[0] = msg[0]
            self.playerScores[1] = msg[1]

            p = self.main.getPlayer()
            window = p.getGUIWindow()
            self.setNamesToTeam()
            window.SetBattleWindow(self.playerTeams, self.playerScores)





    def sendMessage(self, msg, power):
        try:
            newMsg = pickle.dumps(self.team)
            self.s.send(bytes(msg, "utf-8"))
            self.s.send(newMsg)
        except:
            print("Error sending commands")
