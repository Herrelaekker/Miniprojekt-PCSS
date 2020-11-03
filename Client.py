import socket
import threading
import pickle

class Client(threading.Thread):

    def __init__(self, pNum):
        threading.Thread.__init__(self)
        self.pNum = pNum
        self.msg = ""
        self.team = []

    def run(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 9879
        self.ip_address = socket.gethostbyname(socket.gethostname())
        self.s.connect((self.ip_address, self.port))
        print("The client has been connected")
        # print("The message from server:" + self.s.recv(1024).decode("utf-8"))
        # self.s.send(bytes(self.name, "utf-8"))
        # print("message sent")
        print("The message from server: " + self.s.recv(1024).decode("utf-8"))

        self.SendMessage()


    def setMsg(self, msg):
        self.msg = msg

    def setTeam(self, team):
        self.team = [None]*len(team)
        for x in range(len(team)):
            self.team[x] = team[x].getName()
        #self.team = team

    def getMsg(self):
        return self.msg
     #   if self.msg != "":
     #       self.s.close()

    def SendDoneMessage(self):
        d = {1: "Hej", 2: "Venner"}
        newMsg = pickle.dumps(d)
        self.s.send(bytes("Done", "utf-8"))
        self.s.send(newMsg)

        print("The message from server: " + self.s.recv(1024).decode("utf-8"))
        print("Done")

    def SendMessage(self):
        while True:
            if self.pNum == "":
                self.s.send(bytes("Give me my player number", "utf-8"))
                self.pNum = self.s.recv(256).decode()
                print(self.pNum)
            elif self.msg == "Done":
                newMsg = pickle.dumps(self.team)
                self.s.send(bytes("Done", "utf-8"))
                self.s.send(newMsg)
                print("The message from server: " + self.s.recv(1024).decode("utf-8"))
                print("Done")
                list1 = self.s.recv(10000)
                self.playerTeam1 = pickle.loads(list1)
                print(f"player 1's list: {self.playerTeam1}")
                list2 = self.s.recv(10000)
                self.playerTeam2 = pickle.loads(list2)
                print(f"player 2's list: {self.playerTeam2}")
                print("list received")

                scores = self.s.recv(1024)
                self.finalScores = pickle.loads(scores)
                print(f"player 1's score: {self.finalScores[0]}")
                print(f"player 2's score: {self.finalScores[1]}")

                finalMsg = self.s.recv(1024).decode()
                print(finalMsg)

                self.msg = ""

