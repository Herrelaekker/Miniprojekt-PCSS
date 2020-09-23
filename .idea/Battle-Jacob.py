import cv2 as cv
from Unit import unit

img = cv.imread("Warrior.png")

p1Score = 34
p2Score = 3

# p1Units = [unit(1,1,img), unit(2,1,img), unit(3,3,img), unit(2,1,img), unit(3,3,img)]
# p2Units = [unit(1,2,img), unit(2,1,img), unit(3,3,img), unit(2,1,img)]

def calcBattle():
    if (p1Score > p2Score):
        print("P1 Wins!")
    else:
        print("P2 Wins!")

    print("\n P1 Score = " + str(p1Score) + "\n P2 Score = " + str(p2Score))

calcBattle()