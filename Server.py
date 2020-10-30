import time
import socket
import threading
#import Client

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 9879
hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())

s.bind((ip_address, port))
print(f"socket bound to {port}")

s.listen(5)
print("socket is listening...")

activeClients = []
usernames = {"P1", "P2"}
playersActive = 0
playersReady = [False, False]

def func(num):
    playersReady[num-1] = True
    print(str(playersReady[0]) + str(playersReady[1]))

def NewClientSocketHandler(client, addr):
    client.send(bytes("P"+str(playersActive), "utf-8"))
    print("P" + str(playersActive) + " has connected")
    playerNum = playersActive
    while True:
        msg = client.recv(256).decode()
      #  print(msg)
        if msg == "done":
            print("player" + str(playerNum) + " done")
            func(playerNum)

while True:
    conn, addr = s.accept()
    print(f"Got connection from {addr}")
    #c.send(bytes("Thank you for connecting", "utf-8"))

    thread = threading.Thread(target=NewClientSocketHandler, args=(conn, addr))
    playersActive += 1
    thread.start()
