from PIL import Image, ImageDraw, ImageFont
from Unit import unit

class cardGenerator (unit):
    statsBar = Image.open('icons\statsBar.png')
    nameBar = Image.open('icons\mameBar.png')
    icon = Image.open('icons\character.png')
    attackPower = 10
    name = 'default name'

    def __init__(self):
        self.statsBar = Image.open('icons\statsBar.png')
        self.nameBar = Image.open('icons\mameBar.png')
        self.icon = Image.open('icons\character.png')
        self.attackPower = 10
    def createCard(self, unit):
        self.icon = unit.getIcon()
        self.attackPower = unit.getAttackPower()
        self.name = unit.getName()

        image1 = self.statsBar.resize((100, 500))
        image2 = self.icon.resize((400, 400))
        image3 = self.nameBar.resize((400, 100))

        image1 = image1.resize((100, 500))
        image2 = image2.resize((400, 400))
        image3 = image3.resize((400, 100))

        image1_size = image1.size
        image2_size = image2.size
        new_image = Image.new('RGB', (image2_size[0] + 100, image2_size[1] + 100), (255, 255, 255))
        new_image.paste(image1, (0, 0))
        new_image.paste(image2, (image1_size[0], 0))
        new_image.paste(image3, (100, image2_size[0]))
        new_image.save("cards\merged_image.png","PNG")
        #new_image.show()

        # get an image
        base = Image.open("cards\merged_image.png").convert("RGBA")

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("fonts\BebasNeue-Regular.ttf", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((30, 110), str(unit.getAttackPower()), font=fnt, fill=(0, 0, 0, 255))
        # draw text, full opacity
        d.text((30, 420), str(unit.getCost()), font=fnt, fill=(0, 0, 0, 255))

        d.text((300, 420), unit.getName(), font=fnt, fill=(0, 0, 0, 255))

        out = Image.alpha_composite(base, txt)

        out.show()





    def debug(self):
        print(self.attackPower)

testUnit = unit(20, 200, Image.open('icons\character.png'), 'Epic Gamer')

cardGen = cardGenerator()
cardGen.createCard(testUnit)
