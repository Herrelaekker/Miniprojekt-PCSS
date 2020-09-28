from PIL import Image, ImageDraw, ImageFont
from Unit import unit

class cardGenerator (unit):
    statsBar = Image.open('icons\statsBar.png')
    nameBar = Image.open('icons\mameBar.png')
    icon = Image.open('icons\character.png')
    attackPower = 10
    name = 'default name'

    #Ved ikke hvor meget af det her, der var nødvendigt. Hvis man ved, om  det kan fjernes er man meget velkommen til det
    def __init__(self):
        self.statsBar = Image.open('icons\statsBar.png')
        self.nameBar = Image.open('icons\mameBar.png')
        self.icon = Image.open('icons\character.png')
        self.attackPower = 10

    #Genererer et kort baseret på et unit objekt og et "file number". File number bruges til at navngive filen>
    #>og er mest til brug af unitGenerator-classen, så der er orden i filerne.
    def createCard(self, unit, fileNumber):
        self.icon = unit.getIcon()
        self.attackPower = unit.getAttackPower()
        self.name = unit.getName()
        fileName = 'characterCard'+str(fileNumber)+'.png'

        #Resizer alle billederne til de korrekte størrelser. Burde ikke være nødvendigt, men er en failsafe>
        #>for at sikre, at output-billederne forbliver 500x500
        image1 = self.statsBar.resize((100, 500))
        image2 = self.icon.resize((400, 400))
        image3 = self.nameBar.resize((400, 100))

        image1 = image1.resize((100, 500))
        image2 = image2.resize((400, 400))
        image3 = image3.resize((400, 100))

        #Sammensætter billederne til ét ved at appende dem langs hinanden og gemmer det.
        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB', (image2_size[0] + 100, image2_size[1] + 100), (255, 255, 255))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (100, image2_size[0]))
        new_image.save("cards\merged_image.png","PNG")
        #new_image.show()

        #Henter billedet der skal skrives på
        base = Image.open("cards\merged_image.png").convert("RGBA")

        #Laver et blankt text image med 0% opacity
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        #Finder en font
        fnt = ImageFont.truetype("fonts\BebasNeue-Regular.ttf", 40)
        #Gør klar til at ændre i txt
        d = ImageDraw.Draw(txt)

        #Draw'er attackpower tekst på billedet
        d.text((30, 110), str(unit.getAttackPower()), font=fnt, fill=(0, 0, 0, 255))

        #Draw'er cost tekst på billedet
        d.text((30, 420), str(unit.getCost()), font=fnt, fill=(0, 0, 0, 255))

        d.text((300, 420), unit.getName(), font=fnt, fill=(0, 0, 0, 255))

        #Gemmer outputtet som en png
        out = Image.alpha_composite(base, txt)
        out.save('cards/'+fileName, 'PNG')
        fileName = 'characterCard' + str(fileNumber) + '.png'
        # out.show()





    def debug(self):
        print(self.attackPower)

