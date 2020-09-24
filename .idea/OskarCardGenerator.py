from PIL import Image
from Unit import unit

class cardGenerator (unit):
    statsBar = Image.open('icons\statsBar.png')
    nameBar = Image.open('icons\mameBar.png')
    icon = Image.open('icons\character.png')
    attackPower = 10

    def __init__(self):
        self.statsBar = Image.open('icons\statsBar.png')
        self.nameBar = Image.open('icons\mameBar.png')
        self.icon = Image.open('icons\character.png')
        self.attackPower = 10
    def createCard(self, unit):
        self.icon = unit.getIcon()
        self.attackPower = unit.getAttackPower()
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
        # new_image.save("images/merged_image.jpg","JPEG")
        new_image.show()

    def debug(self):
        print(self.attackPower)

