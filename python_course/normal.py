#! /usr/bin/python3
#pip3 install pillow
from PIL import Image,ImageEnhance
import numpy as np

gray_image = Image.open('cropped_ros_crystal_grey.png')
#Image to array 
np_image=np.array(gray_image)
print(np_image.shape)

cropped_np_grey_image_int = np_image[0:632,0:632]
print(cropped_np_grey_image_int.shape)

#Next we make empty 2d numpy array
small_image = np.zeros((79,79)).astype(np.uint8)
print(small_image.shape)


for y in range(len(small_image)):
    for x in range(len(small_image)):
        
        small_image[x,y]=cropped_np_grey_image_int[x*8,y*8]
       
            #print(cropped_np_gray_image_int.shape)
new_image=Image.fromarray(small_image)


#brightness enhancer
enhancer = ImageEnhance.Brightness(new_image)

#get the brightest image 
factor = 1.5
normal = enhancer.enhance(factor)
normal.save('ros_crystal_small_normal.png')

