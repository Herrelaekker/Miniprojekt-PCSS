import socket
import sys
import threading
import time
import pickle
from Battle import Battle
from queue import Queue
from CardGenerator import cardGenerator
from UnitGenerator import unitGenerator

NUMBER_OF_THREADS = 2 ## Ikke clients
JOB_NUMBER = [1, 2] ## Ikke CLients
queue = Queue()
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
        global host
        global port
        global s
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
    global playersConnected
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

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


# 2nd thread functions - 1) See all the clients 2) Select a client 3) Send commands to the connected client
# Interactive prompt for sending commands
# turtle> list
# 0 Friend-A Port
# 1 Friend-B Port
# 2 Friend-C Port
# turtle> select 1
# 192.168.0.112> dir


def start_turtle(id):
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("Command not recognized")


"""while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)

        else:
            print("Command not recognized")"""


# Display all current active connections with client

def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients----" + "\n" + results)


# Selecting the target
def get_target(target):
    try:
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn
        # 192.168.0.4> dir

    except:
        print("Selection not valid")
        return None


# Send commands to client/victim or a friend
def send_target_commands(conn, msg):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending commands")
            break


# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


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
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle(x)

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()



"""                self.s.send(bytes("Give me my player number", "utf-8"))
                self.pNum = self.s.recv(256).decode()
                print(self.pNum)
            elif self.msg == "Done":
                newMsg = pickle.dumps(self.team)
                self.s.send(bytes("Done", "utf-8"))
                self.s.send(newMsg)
                print("The message from server: " + self.s.recv(1024).decode("utf-8"))
                print("Done")
                list1 = self.s.recv(10000)"""
create_workers()
create_jobs()