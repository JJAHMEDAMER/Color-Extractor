from PIL import Image
import os

folder = "D:\\004-Programing\\flutter\\happy_mart\\lib\\utils\\1080w"


print(folder)

for file in os.listdir(folder):
    if file.endswith('.jpeg') or file.endswith('.png'):
        print(file)
        
        img = Image.open(folder + '\\' + file)
        colorList = img.getcolors()
            
        threshold = 0
        for color in colorList:
            threshold += color[0]
        
        threshold = threshold/len(colorList)
        
        
        print ('import \'package:flutter/material.dart\'; \nclass AppColor{')
        for color in colorList:
            if color[0] > threshold:                
                final_color = (color[1][3], color[1][0],color[1][1],color[1][2])
                print('  static final Color COLOR_NAME = const Color.fromARGB' + str(final_color) +';') 
        print('}')


'''
Pillow returns (r, g, b, a)
r is red channel
g is green channel
b is blue channel
a is opacity 

Flutter takes (a, r, g, b)
'''
