import cv2 as cv
from Unit import unit

img = cv.imread("Warrior.png")


man = unit(1,1,img)
print(man)
