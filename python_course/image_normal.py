#! /usr/bin/python3
#pip3 install pillow
from PIL import Image
import numpy as np

def grayscale(colors):
    red, green, blue = colors
    #We could do just .333 for every color, but from wikipedia
    #tells us that mixing colors like this make picture a little 
    #bit better.
    return 0.07 * red + 0.72 * green + 0.21 * blue
    

# If you have problem to use writing_file.py, 
# you can manually download picture, and save it
# to right folder.
#
#Next open image file, file needs to be in same folder
image_frame = Image.open('ROS_Crystal_Logo.png')
#next make nympy array from picture
np_image = np.array(image_frame)

#we convert image to grey scale.
#Before we have 3d array with 3 color arrays 
#after this we have 2d array in grey scale
np_image_in_grayscale = np.apply_along_axis(grayscale, 2, np_image)

#Next we convert nympy array to type uint8
#That means that every pixel in array has 8 bit value, that
#can be anything from 0-255
#In case of image usually 0 is black and 255 is white.
np_gray_image_int = np_image_in_grayscale.astype(np.uint8)

#change np array back to image
gray_image = Image.fromarray(np_gray_image_int)

filename = "ros_crystal_grey.png"
#Save image to file
gray_image.save(filename)

#.shape prints shape of n dimensional numpy array
print(np_gray_image_int.shape)
# lets crop picture a little
#we make it a squre of 632, we can divide that by 8

cropped_np_gray_image_int = np_gray_image_int[0:632,0:632]
print(cropped_np_gray_image_int.shape)


gray_image_cropped = Image.fromarray(cropped_np_gray_image_int)
filename = "ros_crystal_grey_cropped.png"

gray_image_cropped.save(filename)

print(cropped_np_gray_image_int.shape[0])
# now we know that image has resolution 632 x 632

#Next we make empty 2d numpy array
small_image = np.zeros((79,79)).astype(np.uint8)
print(small_image.shape)
print(len(cropped_np_gray_image_int))
for y in range(79):
    for x in range(79):
        
        small_image[x][y]=cropped_np_gray_image_int[x*8][y*8]
       
            #print(cropped_np_gray_image_int.shape)
new_image=Image.fromarray(small_image)
filename='phoo_easy1.png'
new_image.save(filename)


            

"""
easy: make for loops to take one pixel from every 8x8 pixels from
cropped_np_gray_image_int and save it right place in small_image array,
make picture from array, and save file as ros_crystal_small_easy.png
return this image and code to moodle

normal: Same that easy, but now look every 8x8 pixels and save brightest
to small_image_array, and use ros_crystal_small_normal.png
return this image and code to moodle

hard: same as easy, but now look every 8x8 pixels and save average of those 
pixels to small_image array, and use ros_crystal_small_hard.png
return this image and code to moodle"""