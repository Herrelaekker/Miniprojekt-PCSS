import cv2 as cv
from Unit import unit

#Instantiation af unit object
q = unit(20, 200, cv.imread('icons\kinatest.png'))

#Fastlægger icon og template
icon = q.icon
template = cv.imread('icons\monkeTemplate.png')

#Kombinerer template med icon
card = icon+template

#Opretter nyt billede
newCard = cv.imwrite('cards\card00.png', card)

#Det virker ikke
#textCard = cv.putText(newCard, 'stfu?', (200,200), 1, 200, 0)

#Debugging
cv.imshow('combined', template+icon)
cv.imshow('gaming', q.getIcon())

#Det gør det ikke
#cv.imshow('virker det?', textCard)
print(q.getCost())
cv.waitKey(0)
