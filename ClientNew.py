import socket
import os
import subprocess
import threading
import pickle

class Client(threading.Thread):

    def __init__(self, pNum,main):
        threading.Thread.__init__(self)
        self.pNum = pNum
        self.msg = ""
        self.team = []
        self.main = main

    def run(self):
        self.s = socket.socket()
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 9999

        self.s.connect((self.host, self.port))
        print("The client has been connected")

        thread = threading.Thread(target=self.listen)
        thread.daemon = True
        thread.start()

    def setTeam(self, team):
        self.team = [None]*len(team)
        for x in range(len(team)):
            self.team[x] = team[x].getName()

    def listen(self):
        while True:
            print(":)")
            # global playersReady
            # if playersReady[num] is False:
            self.msg0 = self.s.recv(10000)
            self.msg1 = self.s.recv(10000)
            self.list0 = pickle.loads(self.msg0)
            self.list1 = pickle.loads(self.msg1)
            print(self.list0)
            print(self.list1)

    def sendMessage(self, msg):
        try:
            self.s.send(bytes(msg, "utf-8"))
            newMsg = pickle.dumps(self.team)
            self.s.send(newMsg)
        except:
            print("Error sending commands")
