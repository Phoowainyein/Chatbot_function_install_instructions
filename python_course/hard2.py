#! /usr/bin/python3
import numpy as np
from PIL import Image

im = Image.open('ros_crystal_small_easy.png')
#im_grey = im.convert('LA') # convert to grayscale
width, height = im.size
image_array = np.array(im)
total = 0
for i in range(image_array.shape[0]):
    for j in range(image_array.shape[1]):
        total += image_array[(i,j)]
a = width * height

mean = (total) / a
print("mean value is : ",mean)
rounded_mean =round(mean)
print(rounded_mean)

mean2 = np.mean(im)

if mean == mean2:
    print("it's correct ")

