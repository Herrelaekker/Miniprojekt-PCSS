import time
import socket
import threading
from socket import error as SocketError
import errno
#import Client

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 9879
hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())
print("ip adress ="+socket.gethostbyname(socket.gethostname()))

s.bind((ip_address, port))
print(f"socket bound to {port}")

s.listen(5)
print("socket is listening...")

activeClients = []
usernames = {"P1", "P2"}
playersActive = 0
playersReady = [False, False]
allPlayersReady = False

playersActive = 0

def func(num):
    if playersReady[num-1] != True:
        playersReady[num-1] = True
        print(str(playersReady[0]) + str(playersReady[1]))


def addActivePlayer(num):
    global playersActive
    playersActive += num


def NewClientSocketHandler(client, addr):
    #print("P" + str(playersActive) + f" has connected from {addr}")
   # try:
    while True:
        try:
            msg = client.recv(256).decode()
            if msg == "Give me my player number":
                addActivePlayer(1)
                print(f"[Connection from player {playersActive} established]")
                pNum = client.send(bytes(str(playersActive), "utf-8"))
            if msg == "Done":
                pNum = client.recv(256).decode()
                print(f"[Connection from player {pNum} established]")
                print("player" + pNum + " done")
                print(int(pNum))
                func(int(pNum))
        except:
            break
    print(f"Player {pNum}, has gracefully disconnected!")
    addActivePlayer(-1)
    print("active players left: " + str(playersActive))

    client.close()



while True:
    conn, addr = s.accept()
    # print(f"Got connection from {addr}")
    # c.send(bytes("Thank you for connecting", "utf-8"))

  #  if playersActive < 2:
    conn.send(bytes("Thank you for connecting", "utf-8"))
    thread = threading.Thread(target=NewClientSocketHandler, args=(conn, addr))
    thread.start()
  #  else:
   #     conn.send(bytes("Failed to connect.", "utf-8"))
