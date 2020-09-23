import cv2 as cv

attackPower = 238
cost = 10
icon = cv.imread("Warrior.png")


def getAttackPower():
    return attackPower


def getCost():
    return cost


def getIcon():
    return icon


print(getAttackPower())
print(getCost())

cv.imshow("Icon", getIcon())
cv.waitKey(0)
