import tkinter.font as tkFont
from BubbleSort import BubbleSort
from PIL import ImageTk,Image
import tkinter as tk

class GUIWindow():
    img = Image.open("testmappe/UnitsJacob/Placeholder.png")
    img = img.resize((150,150))

    icons = [None]*4
    #Loader icons ned så icons[0] er bedst, icons[3] er værst
    for x in range(4):
        icons[x] = Image.open('icons\icon' + str(4-x) + '.png')

    teamIcons = [None] * 10
    teamRarity = [0,1,1,2,2,2,3,3,3,3] # Hvilke rarities felterne er.
    teamRoles = [1,2,3,4] # Hvor mange roller der er tilbage for hver rarity.
    spaceOccupied = [False]*10 # Felter der er en gamer i, er occupied.

    sortStr = ["Highest Power", "Lowest Power", "Highest Cost", "Lowest Cost", "Highest Rank", "Lowest Rank"]
    curSortNum = 0  # Variabel der viser hvilken string vi er ved i sortStr-arrayet.

    row1 = 8  # Rækker af felter der skal laves
    col1 = 5  # Kolonner i første antal felter (Unit Listen)
    row2 = 2
    col2 = 1  # Kolonner i anden række (der skiller units og team)
    col3 = col1 + col2 + 1  # Kolonner i sidste antal felter (team listen)

    def __init__(self, unitList, master, p):
        self.p = p
        self.money = p.getMoney()
        self.root = master
        self.mainFrame = tk.Frame(self.root)

        # Laver Done-vinduet, som ikke vises til at starte med (først når man har trykket på done)
        self.otherWindow = tk.Toplevel(self.root)
        self.otherWindow.withdraw()

        self.fontStyle = tkFont.Font(family="Lucida Grande", size=24)

        # Laver to Frames som styrer hvad der er på højre og venstre side af skærmen.
        self.leftFrame = tk.Frame(self.root, width=850, height=900)
        self.leftFrame.grid(row=0, column=1)
        self.rightFrame = tk.Frame(self.root, width=850, height=900)
        self.rightFrame.grid(row=0, column=2, sticky="nw")

        # Laver phImg om til et PhotoImage, så det kan bruges til knapper og labels.
        self.phImg = ImageTk.PhotoImage(self.img)

        # Laver alle icons om til PhotImage i den rigtige størrelse.
        for x in range(4):
            tempIcon = self.icons[x].resize((150, 150))
            self.icons[x] = ImageTk.PhotoImage(tempIcon)

        # Putter hvert ikon ind på pladserne, an på hvilket ikon der skal være der (valgt ud fra teamRarity)
        # Det vil sige ikon[0] er på 0's plads, ikon[1] er på 1's og 2's plads.
        for x in range(len(self.teamIcons)):
            self.teamIcons[x] = self.icons[self.teamRarity[x]]

        self.printGrid()

        self.unitList = unitList.copy()
        self.tempList = [] # Bruges til at gemme alle de værider der fjernes ved en søgning.
        self.bSort = BubbleSort()
        self.SortUnits()
        self.ShowUnitList()

        # money_text er en string-variabel, som opdateres hver gang money bliver ændret på.
        self.money_text = tk.StringVar()
        self.money_text.set("Money: " + str(self.money))

        self.moneyFont = tkFont.Font(family="Lucida Grande", size=32)

        moneyLabel = tk.Label(self.rightFrame, textvariable=self.money_text, font=self.moneyFont)
        moneyLabel.grid(row=1, column=0, sticky="nw", padx=20, pady=15)

        # Knap som kalder funktionen doneBtnCLicked, når man trykker på den.
        doneBtn = tk.Button(self.rightFrame, text="Done!", command=self.doneBtnClicked, font=self.moneyFont)
        doneBtn.grid(row=2, column=0, padx=50, pady=100)

        self.sortFont = tkFont.Font(family="Lucida Grande", size=16)

        self.sortLabel = tk.Label(self.leftFrame, text="Sort by:", font=self.sortFont)
        self.sortLabel.grid(row=1, column=1, sticky="news", pady=10)

        #Laver en Fram hvor alle sorteringselementer bliver lagt ind i.
        self.sortFrame = tk.Frame(self.leftFrame)
        self.sortFrame.grid(row=2, column=1, sticky="nw")

        self.sortBtns = [None] * len(self.sortStr)

        self.UpdateSortButtons()

        # Adder søgebaren og en søgeknap (der kalder Search-funktionen når man trykker på den) til sortLabel.
        self.searchBar = tk.Entry(self.sortFrame)
        self.searchBar.grid(row=0, column=7, padx=15)
        self.searchBtn = tk.Button(self.sortFrame, text='Search', command=self.Search)
        self.searchBtn.grid(row=0, column=8)

    # Laver en masse billeder som grid
    def printGrid(self):
        #Laver Frame til vores canvas
        self.frame_canvas = tk.Frame(self.leftFrame)
        self.frame_canvas.grid(row=0, column=1, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        self.frame_canvas.grid_propagate(False)

        # Sætter canvas ind på første grid i Framen.
        self.canvas = tk.Canvas(self.frame_canvas)
        self.canvas.grid(row=0, column=0, sticky="news")

        # Adder en scrollbar til højre for canvas'en, og binder den til at kunne scrolle vertikalt.
        self.vsb = tk.Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.frame_canvas.bind("<Configure>", self._on_frame_configure)

        # Laver en frame på canvas'en, hvor alle unitsene (knapper) kommer til at være på.
        self.frame_buttons = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor="nw")

        # Første grid
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = tk.Label(self.frame_buttons, image=self.phImg) # Adder placeholderbillede
                newLabel.grid(row=x, column=y + 1,padx=5, pady=5, sticky="news")

        # Sætter dimensionerne på canvasen. (For at se resten skal man scrolle)
        self.frame_canvas.config(width=850, height=800)

        #Laver teamListFrame
        self.teamListFrame = tk.Frame(self.rightFrame)
        self.teamListFrame.grid(row=0, column=0, sticky='ns')

        # Andet Grid - sætter hvert ikon ind på den tilsvarende plads (bestemt ud fra teamIcons-arrayet)
        for x in range(self.row2):
            for y in range(self.col1):
                icon =self.teamIcons[x*5+y]
                newLabel = tk.Label(self.teamListFrame, image=icon)
                newLabel.image=icon
                newLabel.grid(row=x, column=y + self.col3,padx=5, pady=5, sticky='news')

    # Sørger for at scrollbaren kan scrolle på alt i canvasen.
    def _on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #
    def ShowUnitList(self):
        # Første grid
        # Laver placeholder billede for hvert felt i venstre tabel.
        for x in range(self.row1):
            for y in range(self.col1):
                newLabel = tk.Label(self.frame_buttons, image=self.phImg)
                newLabel.grid(row=x, column=y + 1, padx=5, pady=5)

        # Laver knapper med billeder af hvert unit. Knapperne kalder funktionen unitToTeam når de bliver trykket på.
        # Her giver de deres indexnummer. Eks. den første i listen giver tallet 0.
        for x, u in enumerate(self.unitList):
            btnImg = self.getBtnImage(self.unitList, x, (150, 150))

            newButton = tk.Button(self.frame_buttons, image=btnImg, command=lambda x=x: self.unitToTeam(x), relief=tk.FLAT)
            newButton.image = btnImg
            num = int(x / self.col1)
            newButton.grid(row=num, column=x - (num * self.col1) + 1,padx=5, pady=5)
        # self.mainFrame.pack()

    # Tager billedet fra listen, resizer det, og omdanner det til et PhotoImage.
    def getBtnImage(self, list, val, size):
        newIcon = list[val].getCard()
        newIcon = newIcon.resize(size)
        newImg = ImageTk.PhotoImage(image=newIcon)
        return newImg

    # BubbleSort - Kalder SortUnits funtionen i BubbleSort-objektet.
    def SortUnits(self):
        self.unitList = self.bSort.SortUnits(self.curSortNum, self.unitList).copy()
        self.ShowUnitList()

    # Hvis kanppen der bliver trykket på ikke er den der sidst er blevet valgt...
    #   Så sæt knappen til at være den der bliver trykket på.
    def sortBtnClicked(self, index):
        if self.curSortNum != index:
            self.curSortNum = index
            print(self.curSortNum)
            self.UpdateSortButtons()
            self.SortUnits()


    # Vi fjerner de irrelevante units, og gemmer dem i tempList
    # Når vi Searcher igen tilføjer vi i starten tempList, så udgangspunktet er i den fulde liste.
    def Search(self):

        for x in range(len(self.tempList)):
            self.unitList.append(self.tempList[x])

        tempStr = self.searchBar.get()
        self.tempList = []
        print(tempStr)
        # Tilføjer alle fra unitlisten som ikke matcher søgningen, til tempList.
        for x in range(len(self.unitList)):  # 0-2
            if self.unitList[x].getName().count(tempStr) <= 0:
                self.tempList.append(self.unitList[x])

        #Fjerner alle fra unitlisten som ikke matcher søgningen.
        for x in range(len(self.tempList)):
            self.unitList.remove(self.tempList[x])

        self.SortUnits()


    def UpdateTeam(self):
        team = self.p.getTeam()
        # Adder først labels - sætter hvert ikon ind på den tilsvarende plads (bestemt ud fra teamIcons-arrayet)
        for x in range(self.row2):
            for y in range(self.col1):
                icon =self.teamIcons[x*5+y]
                newLabel = tk.Label(self.teamListFrame, image=icon)
                newLabel.grid(row=x, column=y + self.col3,padx=5, pady=5)

        # Resetter hvilke felter der er occupied.
        self.spaceOccupied = [False]*10

        # går igennem for hver spiller på holdet...
        for x, u in enumerate(team):
            # Får fat i rollen på nuværende spiller:
            roleIndex = team[x].getRole()

            # Går igennem hvert felt i teamRarity
            # teamRarity = [0,1,1,2,2,2,3,3,3,3]
            for y in range(len(self.teamRarity)):
                # Hvis spillerens rolle matcher, og feltet ikke er occupied...
                if self.teamRarity[y] == roleIndex and self.spaceOccupied[y] is False:
                    # Så bliver feltet occupied.
                    self.spaceOccupied[y] = True

                    # Og så addes der en knap med billede der matcher til feltet.
                    btnImg = self.getBtnImage(team, x, (150, 150))
                    newButton = tk.Button(self.teamListFrame, image=btnImg, command=lambda x=x: self.removeTeamUnit(x), relief=tk.FLAT)
                    newButton.image = btnImg
                    num = int(y / self.col1)
                    newButton.grid(row=num, column=y - (num * self.col1) + self.col3, padx=5, pady=5)

                    # Til sidst breakes der, så den går videre til næste spiller på holdet.
                    break


    def removeTeamUnit(self, indexNum):
        # Får fat i den valgte spillers cost og role.
        moneyAdded = self.p.getTeam()[indexNum].getCost()
        roleIndex = self.p.getTeam()[indexNum].getRole()

        # Adder pengene tilbage.
        self.p.addMoney(moneyAdded)
        self.money += moneyAdded

        # Sørger for at der er en ekstra plads på feltet spilleren før var på
        # Eks. teamRoles går fra [1,2,3,3] -> [1,2,3,4], hvis det er en spiller med roleindexet 3.
        self.teamRoles[roleIndex] += 1
        print(self.teamRoles)
        # Sætter teksten på Stringvariablen til den nuværende mængde penge.
        self.money_text.set("Money: " + str(self.money))

        self.p.removeFromTeamList(indexNum)
        self.UpdateTeam()

    def unitToTeam(self, indexNum):
        # Får fat i den valgte spillers cost og role.
        moneySubtracted = self.unitList[indexNum].getCost()
        roleIndex = self.unitList[indexNum].getRole()

        # Hvis man ikke har penge nok, eller er ikke er flere pladser for spillerens rolle tilbage...
        if moneySubtracted <= self.money and self.teamRoles[roleIndex] > 0:
            # Fjerner pengene.
            self.p.addMoney(-moneySubtracted)
            self.money -= moneySubtracted

            # Fjerner en fra spillerens rolles plads
            # Eks. teamRoles går fra [1,2,3,4] -> [1,2,3,3], hvis det er en spiller med roleindexet 3.
            self.teamRoles[roleIndex] -= 1
            print(self.teamRoles)
            # Sætter teksten på Stringvariablen til den nuværende mængde penge.
            self.money_text.set("Money: " + str(self.money))

            self.p.addToTeamList(self.unitList[indexNum])
            self.UpdateTeam()

    # Bliver kaldt når brugeren trykker på done.
    def doneBtnClicked(self):

        # Kalder funktionen doneButtonClicked() i mainScriptet.
        main = self.p.getMain()
        main.doneButtonClicked()

        # Skriver ventetekst som dukker op i et andet vindue.
        fontStyle = tkFont.Font(family="Lucida Grande", size=48)
        self.waitingLabel = tk.Label(self.otherWindow, text="Waiting for other player...", font=fontStyle)
        self.waitingLabel.grid(row=1, column=2)

        # Gør så at det før lukkede vindue, nu åbner igen..
        self.otherWindow.deiconify()

    # Bliver kaldt når begge spillere har trykket done.
    def SetBattleWindow(self, playerTeams, playerScore1, playerScore2):
        # Fjerner venteteksten.
        self.waitingLabel.destroy()

        # For hver spiller...
        for y in range(2):

            for x in range(len(playerTeams[y])):
                # Laver et label for hvert unit på spillerens hold
                labelImg = self.getBtnImage(playerTeams[y], x, (150, 150))
                num = int(x / self.col1)
                newLabel = tk.Label(self.otherWindow, image=labelImg)
                newLabel.image = labelImg

                num = int(x / self.col1)

                # Sætter labelet ind på plads.
                newLabel.grid(row=2 + num + y*2, column=x - (num * self.col1) + 2,padx=5, pady=5)

        # Skriver spillerne som string
        Player1Label = tk.Label(self.otherWindow, text="Player 1", font=self.fontStyle)
        Player1Label.grid(row=2, column=1)
        Player2Label = tk.Label(self.otherWindow, text="Player 2", font=self.fontStyle)
        Player2Label.grid(row=4, column=1)

        # Skriver hver spilelrs totale Power
        pScore1Lbl = tk.Label(self.otherWindow, text="Power: " + str(playerScore1), font=self.fontStyle)
        pScore1Lbl.grid(row=2, column=8)
        pScore2Lbl = tk.Label(self.otherWindow, text="Power: " + str(playerScore2), font=self.fontStyle)
        pScore2Lbl.grid(row=4, column=8)


    def UpdateSortButtons(self):
        # self.sortStr = ["Highest Power", "Lowest Power", "Highest Cost", "Lowest Cost", "Highest Rank", "Lowest Rank"]

        # Laver hver knap...
        for x in range(len(self.sortStr)):
            # Hvis det er den nuværende valgt knap, så laver man knappen sunket ned. (Det ligner at knappen er valgt)
            if x == self.curSortNum:
                self.sortBtns[x] = tk.Button(self.sortFrame, text=self.sortStr[x], command=lambda x=x: self.sortBtnClicked(x), relief=tk.SUNKEN)
            # Ellers laver man bare en normal knap
            else:
                self.sortBtns[x] = tk.Button(self.sortFrame, text=self.sortStr[x], command=lambda x=x: self.sortBtnClicked(x))

            self.sortBtns[x].grid(row=0, column=1 + x, padx=15)
