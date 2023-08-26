import imageio
import os

images = []
files = sorted(os.listdir("images"))
for file in files:
    img_path = "images/" + file
    image = imageio.imread(img_path)
    images.append(image)
imageio.mimsave("output.gif", images, duration=0.04)