import socket
import threading
import time
import pickle
from CardGenerator import cardGenerator
from UnitGenerator import unitGenerator

all_connections = []
all_address = []

playersReady = [False, False]
usedConnections = []
playersConnected = 0
playerTeams = []

cardGen = cardGenerator()
unitGen = unitGenerator()
unitGen.genUnits(cardGen, open('unitList.txt', 'r'))
unitList = unitGen.getUnits()

# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Handling connection from multiple clients and saving to a list
# Closing previous connections when server.py file is restarted
numOfClients = 0
threads =[]
def accepting_connections():

    while True:
        try:
            conn, address = s.accept()
       #     s.setblocking(1)  # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

            print(playersConnected)
            if playersConnected == 0:
                thread = threading.Thread(target=lambda y=playersConnected, x=conn: listen(x,y))
                threads.append(thread)
                thread.daemon = True
                thread.start()
            elif playersConnected == 1:
                thread1 = threading.Thread(target=lambda y=playersConnected, x=conn: listen(x,y))
                threads.append(thread1)
                thread1.daemon = True
                thread1.start()

            playersConnected = len(all_connections)

        except:
            print("Error accepting connections")



def listen(conn, num):
    while True:
        data = conn.recv(1024).decode()
        if data == "Done":
            list = conn.recv(100000)
            playerTeams.append(pickle.loads(list))
            print(pickle.loads(list))
           # playersReady += 1
            usedConnections.append(conn)
            playersReady[num] = True
            break
    while True:
        if playersReady[0] and playersReady[1]:
            print("player " + str(conn) + "stopped listening")
            AllPlayersDone(conn)
            break

def AllPlayersDone(conn):
    try:
        print(playersReady)
        print(playerTeams)
        playerPower = calcBattle(playerTeams)

        team = setTeam(playerTeams)
        team0 = pickle.dumps(team[0])
        team1 = pickle.dumps(team[1])
        totalPower = pickle.dumps(playerPower)
        totalPower2 = pickle.dumps(playerPower[1])
        print(totalPower)
        conn.send(team0)
        conn.send(team1)
        time.sleep(2)
        conn.send(totalPower)
        print(playerPower)
    except:
        print("Error")


def calcBattle(playersTeams):
        newPT = getPlayerTeam(playersTeams)
        finalScore = [0, 0]

        for x in range(2):
            for y in range(len(newPT[x])):
                if x == 0:
                    finalScore[0] += newPT[x][y].getAttackPower()
                if x == 1:
                    finalScore[1] += newPT[x][y].getAttackPower()

        return finalScore


def setTeam(team):
    for x in range(2):
        for y in range(len(team[x])):
            team[x][y] = team[x][y].getName()
    return team


def getPlayerTeam(playersTeams):
    newPT = playersTeams.copy()
    for x in range(2):
        for y in range(len(newPT[x])):
            for z in range(len(unitList)):
                if newPT[x][y] == unitList[z].getName():
                    newPT[x][y] = unitList[z]
                    break
    return newPT

# Do next job that is in the queue (handle connections, send commands)
def work():
    while True:
        create_socket()
        bind_socket()
        accepting_connections()


work()