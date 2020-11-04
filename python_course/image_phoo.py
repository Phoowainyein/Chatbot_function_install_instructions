#! /usr/bin/python3
from PIL import Image
import numpy as np

im=Image.open('ROS_Crystal_Logo.png')
#I am printing the size weight and height (output : 639,676)
width, height = im.size
print(im.size)#(639,676)

#printing the image format and png is one of the pillow supported format
print(im.format,im.info)
#this will print RGB or L
print(im.mode)
#transforming an image to numpy array
image_as_array=np.array(im)
#I must remember to print the array
print(image_as_array.shape)
#I can do this as well to know what is c,w,h sepeately
h, w, c = image_as_array.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)

#now we can turn the image
#https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html
turned_image =np.moveaxis(image_as_array,1,0)#we are moving the index position 1(639)to index postion o
print(turned_image.shape)

#saving our turned image and giving the filename
#first ,create a PIL image
""" Then this can be used to convert it to a Pillow image:
im = Image.fromarray(a)
Returns
An image object. """
save_image = Image.fromarray(turned_image)
filename='phoo_image.png'
save_image.save(filename)




