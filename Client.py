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
        self.team = team

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
                d = {1: "Hej", 2: "Venner"}
                newMsg = pickle.dumps(d)
                self.s.send(bytes("Done", "utf-8"))
                self.s.send(newMsg)
                print("The message from server: " + self.s.recv(1024).decode("utf-8"))
                print("Done")
                self.msg = ""
             #   print(self.s.recv(1024).decode())

