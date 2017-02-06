#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:11:05 2017

@author: abed
"""
import os
import PIL
from PIL import Image
import datetime
import shutil

now = datetime.datetime.now()
image_name = '1.jpg'
img = Image.open(image_name)

Dir = 'Images/'
if not os.path.isdir(Dir):
    os.makedirs(Dir)
newDir = Dir + str(now)



def iconResizer(size):
    wpercent = (size / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img1 = img.resize((size, hsize), PIL.Image.ANTIALIAS)
    if not os.path.isdir(newDir):
        os.makedirs(newDir)
    img1.save(newDir + '/' + str(size) + '.png')
    
def squareCrop():
    width, height = img.size   # Get dimensions
    if width < height:
        maxSide = width
    else:
        maxSide = height
    size = (maxSide, maxSide)
    img.thumbnail(size, Image.ANTIALIAS)
    background = Image.new('RGBA', size, (255, 255, 255, 0))
    background.paste(
    img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
    )
    background.save("1.jpg")
    


    
# This must be not equal at the end !=
if img.size[0] != img.size[1]:
    print "Sorry, image should be squared. Please put a square image and try again"
else:
    iconResizer(20)
    iconResizer(40)
    iconResizer(60)
    iconResizer(58)
    iconResizer(87)
    iconResizer(80)
    iconResizer(120)
    iconResizer(180)
    iconResizer(29)
    iconResizer(76)
    iconResizer(152)
    iconResizer(167)
    
    src = "C:\\steve_test\\Test_xp\\added"
    dst = "C:\\steve_test\\Test_xp\\moved"
    shutil.move(image_name, newDir + '/' + "Original_Image_" + image_name)
    







 

    