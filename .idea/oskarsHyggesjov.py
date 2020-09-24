import cv2 as cv
import numpy as np
from Unit import unit
textImg = np.zeros((500,500,3), np.uint8)
textImg[:,200:500:] = (255,255,255)
font = cv.FONT_HERSHEY_SIMPLEX
#Instantiation af unit object
q = unit(20, 200, cv.imread('icons\kinatestNEW.png'))

#Fastlægger icon og template
icon = q.icon
template = cv.imread('icons\wemplateNEWEST.png')

#Kombinerer template med icon

card = template+icon



#Opretter nyt billede
newCard = cv.imwrite('cards\card00.png.png', card)

#Det virker ikke
#textCard = cv.putText(newCard, 'stfu?', (200,200), 1, 200, 0)
cv.putText(textImg,'Hack Projects',(0,50), font, 1,(0,0,0),3)
#Debugging
cv.imshow('combined', card)
cv.imshow('gaming', q.getIcon())
cv.imshow('text', template)
#Det gør det ikke
#cv.imshow('virker det?', textCard)
print(q.getCost())
cv.waitKey(0)
