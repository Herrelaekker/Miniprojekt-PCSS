import cv2 as cv
from Unit import unit
import tkinter as tk
from Player import player
from PIL import Image
from UnitGenerator import unitGenerator
from CardGenerator import cardGenerator
class Battle(object):

    def __init__(self):
        self.cardGen = cardGenerator()
        self.unitGen = unitGenerator()
        self.unitGen.genUnits(self.cardGen, open('unitList.txt', 'r'))
        self.unitList = self.unitGen.getUnits()

    def calcBattle(self, playersTeams):
        self.getPlayerTeam(playersTeams)
        finalScore = [0,0]
        finalScore2 = 0

        for x in range(2):
            for y in range(len(self.playersTeams[x])):
                if x == 0:
                    finalScore[0] += self.playersTeams[x][y].getAttackPower()
                if x== 1:
                    finalScore[1] += self.playersTeams[x][y].getAttackPower()

        return finalScore


    def getPlayerTeam(self, playersTeams):
        self.playersTeams = playersTeams
        for x in range(2):
            for y in range(len(playersTeams[x])):
                for z in range(len(self.unitList)):
                    if playersTeams[x][y] == self.unitList[z].getName():
                        self.playersTeams[x][y] = self.unitList[z]
                        break