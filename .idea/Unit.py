import cv2 as cv

attackPower = 0
cost = 0
icon = cv.imread("intro_ball.gif")


def getAttackPower():
    return attackPower


def getCost():
    return cost


def getIcon():
    return icon
