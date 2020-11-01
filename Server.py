import time
import socket
import threading
import pickle
from socket import error as SocketError
import errno
#import Client

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 9879
hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())
print("ip address = "+socket.gethostbyname(socket.gethostname()))

s.bind((ip_address, port))
print(f"socket bound to {port}")

s.listen(5)
print("socket is listening...")

activeClients = []
playersActive = 0
playersReady = [False, False]
playersOccupied = [False, False]
allPlayersReady = False
playerTeams = []

playersActive = 0

def playerDone(num):
    if playersReady[num-1] != True:
        playersReady[num-1] = True
        print(str(playersReady[0]) + str(playersReady[1]))


def addActivePlayer(num):
    global playersActive
    playersActive += num


def AllPlayersDone():
    if playersReady[0] is True & playersReady[1] is True:
        return True
    else:
        return False


def choosePlayerNumber():
    global players
    chosenpNum = 0
    print("def choosePlayerNumber():")
    for x in range(2):
        if playersOccupied[x] is False:
            print(x)
            playersOccupied[x] = True
            chosenpNum = x+1
            break

    return chosenpNum


def NewClientSocketHandler(client, addr):
    #print("P" + str(playersActive) + f" has connected from {addr}")
   # try
    pNum = 0
    while True:
        try:
            msg = client.recv(256).decode()
            print("Connected...")
            print("Message from client: " + msg)
            if msg == "Give me my player number":
                addActivePlayer(1)
                print("active players: " + str(playersActive))
                pNum = choosePlayerNumber()
                print("Chosen number = " + str(pNum))
                if pNum != 0:
                    print(f"[Connection from player {pNum} established]")
                    client.send(bytes(str(pNum), "utf-8"))
                    msg = ""
                else:
                    print("Too many players :(")
                    break
            if msg == "Done":
                print("Player" + str(pNum) + " done")
                teamMsg = client.recv(256)
                print("team Message Received")
                list = pickle.loads(teamMsg)
                print("<list loaded>")
                print(f"Player {pNum}'s list: {list}")
                playerTeams[pNum] = list

                client.send(bytes("Thanks for the list!", "utf-8"))
                playerDone(int(pNum))
            if AllPlayersDone():
                print("All Players Done")
        except:
            break
    print(f"Player {pNum}, has disconnected!")
    addActivePlayer(-1)
    if playersReady[pNum-1] is False:
        playersOccupied[pNum-1] = False
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
