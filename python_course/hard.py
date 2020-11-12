#! /usr/bin/python3
import numpy as np
from PIL import Image


"""hard: same as easy, but now look every 8x8 pixels and save average of those 
pixels to small_image array, and use ros_crystal_small_hard.png
return this image and code to moodle"""

open_img=Image.open('ros_crystal_small_easy.png')
image_array = np.array(open_img)
#new_image = image_array.copy()
n = 0
average_sum = 0
for i in range(0, len(image_array)):
    for j in range(0, len(image_array[i])):
        for k in range(-2, 3):
            for l in range(-2, 3):
                if (len(image_array) > (i + k) >= 0) and (len(image_array[i]) > (j + l) >= 0):
                    average_sum += image_array[i+k][j+l]
                    n += 1

    image_array[i][j] = (int(round(average_sum/n)))
    average_sum = 0
    n = 0

hard_img= Image.fromarray(np.array(image_array))
filename ='ros_crystal_small_hard.png'
hard_img.save(filename)
    