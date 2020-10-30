import socket

class Client(object):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 9879
    ip_address = socket.gethostbyname(socket.gethostname())
    s.connect((ip_address, port))
    print("The client has been connected")

    name = s.recv(1024).decode("utf-8")

    print("The message from server:" + name)

    nameCheck = False

    def __init__(self):
        print("Instantiated")

    def func(self):
        msg = "done"
        self.s.send(bytes(msg, "utf-8"))


