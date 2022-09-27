from PIL import Image
import os



#folder = input('Enter Folder Path : ')

folder = r"D:\004-Programing\flutter\happy_mart\lib\utils\color_palette"

# Input Checker
while folder[0] in '({["\']})':
    folder = folder[1:]

while folder[-1] in'({["\']})':
    folder = folder[:-1]
    

# Color Extractor

try:
    file_list = os.listdir(folder)
    for i in range(len(file_list)):
        file_list[i] = f'{folder}\{file_list[i]}'
except:
    file_list = [folder]


 
for file in file_list:
    if file.endswith('.jpeg') or file.endswith('.png'):
        print(file)
        
        img = Image.open(file)
        colorList = img.getcolors()
            
        threshold = 0
        for color in colorList:
            threshold += color[0]
        
        threshold = threshold/len(colorList)
        
        index = 1
        print ('import \'package:flutter/material.dart\'; \nclass AppColor{')
        for color in colorList:
            if color[0] >= threshold:                
                final_color = str((color[1][3], color[1][0],color[1][1],color[1][2]))
                print(f'  static final Color color_{index} = const Color.fromARGB({final_color};') 
                index += 1
        print('}')
# 'D:\004-Programing\flutter\happy_mart\lib\utils\color_palette'


'''
Pillow returns (r, g, b, a)
r is red channel
g is green channel
b is blue channel
a is opacity 

Flutter takes (a, r, g, b)
'''
