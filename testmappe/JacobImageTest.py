from PIL import Image
#Read the two images
image1 = Image.open('../Warrior.png')
# image1.show()
image2 = Image.open('../Warrior.png')

image3 = Image.open('../Warrior.png')
# image2.show()
#resize, first image
image1 = image1.resize((100, 500))
image2 = image2.resize((400,400))
image3 = image3.resize((400,100))

image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(image2_size[0]+100, image2_size[1]+100), (255, 255,255))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.paste(image3,(100,image2_size[0]))
# new_image.save("images/merged_image.jpg","JPEG")
new_image.show()