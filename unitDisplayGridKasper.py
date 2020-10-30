import os
import numpy as np
import matplotlib.pyplot as plt

directory = "./ExamplePictures/"
images = os.listdir(directory)

fig = plt.figure(figsize=(5, 5))
columns = 3
rows = np.ceil(len(images))

for x, i in enumerate(images):
    path =  os.path.join("./ExamplePictures/",i)
    img = plt.imread(path)
    fig.add_subplot(rows, columns, x+1)
    plt.axis('off')
    plt.imshow(img)

plt.show()
