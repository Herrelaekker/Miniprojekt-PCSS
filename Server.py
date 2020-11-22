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
playerTeams = []

cardGen = cardGenerator()
unitGen = unitGenerator()
unitGen.genUnits(cardGen, open('unitList.txt', 'r'))
unitList = unitGen.getUnits()

# Create a Socket (connection between two computers)
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


# Binding and listening for connections
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
threads =[None,None]
def accepting_connections():

    while True:
        try:
            conn, address = s.accept()

            print("Connection has been established :" + address[0])

            playersConnected = len(all_connections)

            for index in range(2):
                if playersConnected == index:
                    print("listening on " + str(playersConnected))
                    threads[index] = threading.Thread(target=lambda y=playersConnected, x=conn: listen(x,y))
                    #threads.append(thread)
                    threads[index].daemon = True
                    threads[index].start()

            all_connections.append(conn)
            all_address.append(address)

        except:
            print("Error accepting connections")



def listen(conn, playerID):
    while True:
        data = conn.recv(1024).decode()
        if data == "Done":
            list = conn.recv(100000)
            playerTeams.append(pickle.loads(list))
            print(pickle.loads(list))
            usedConnections.append(conn)
            playersReady[playerID] = True
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
        conn.send(team0)
        conn.send(team1)
        time.sleep(2)
        conn.send(totalPower)

        del all_connections[:]
        del all_address[:]
        del playerTeams[:]

        for x in range(len(playersReady)):
            playersReady[x] = False

    except:
        print("Error (Probably happened when trying to connect to closed Client.)")


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


create_socket()
bind_socket()
accepting_connections()