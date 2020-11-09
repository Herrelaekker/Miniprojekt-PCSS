import socket
import threading
import pickle

class Client(threading.Thread):

    def __init__(self, pNum, main):
        threading.Thread.__init__(self)
        self.pNum = pNum
        self.msg = ""
        self.team = []
        self.main = main
        self.msgNum = 0
        self.playerTeams = []
        self.playerScores = [0, 0]

    def run(self):
        # Sætter en socket op til at connecte.
        self.s = socket.socket()
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 9999

        # Connecter med hosten (som er Serveren)
        self.s.connect((self.host, self.port))
        print("The client has been connected")

        # Kalder funktionen listen() som en thread
        thread = threading.Thread(target=self.listen)
        thread.daemon = True
        thread.start()

    # Konverterer Team-listen, til en liste kun med navnene på unitsene.
    def setTeamToNames(self, team):
        self.team = [None]*len(team)
        for x in range(len(team)):
            self.team[x] = team[x].getName()

    # Konverterer navne-listen, til en liste med unitsene de svarer til.
    def setNamesToTeam(self):
        self.unitList = self.main.getPlayer().getUnitList()
        for x in range(2):
            for y in range(len(self.playerTeams[x])):
                for z in range(len(self.unitList)):
                    if self.playerTeams[x][y] == self.unitList[z].getName():
                        self.playerTeams[x][y] = self.unitList[z]
                        break
        print(self.playerTeams)

    # Lytter hele tiden til serveren og venter på beskeder.
    # Hvis den har fået en besked sender den den til ReceiveMessage-funktionen.
    def listen(self):
        while True:
            msg = self.s.recv(10000)
            list = pickle.loads(msg)
            print(list)
            self.msgNum += 1
            self.ReceiveMessage(list)

    #
    def ReceiveMessage(self, msg):
        # Hvis det er første og anden besked, så er det de to teams, som så bliver gemt.
        if self.msgNum == 1 or self.msgNum == 2:
            self.playerTeams.append(msg)
        # Hvis det er tredje besked, så er de samlede to scores fra hvert hold, som også bliver gemt.
        elif self.msgNum == 3:
            self.playerScores[0] = msg[0]
            self.playerScores[1] = msg[1]

            p = self.main.getPlayer()
            window = p.getGUIWindow()
            self.setNamesToTeam()

            # Den kalder funktionen SetBattleWindow() i GUIWindowet der er tilknyttet til playeren.
            window.SetBattleWindow(self.playerTeams, self.playerScores[0], self.playerScores[1])

    # Funktion der bliver kaldt når man trykker på done.
    # Sender den valgte besked til serveren.
    # Hvis ikke den kan sende, skriver den en error besked.
    def sendMessage(self, msg):
        try:
            newMsg = pickle.dumps(self.team)
            self.s.send(bytes(msg, "utf-8"))
            self.s.send(newMsg)
        except:
            print("Error sending commands")
