# -*- coding: utf-8 -*-
import numpy as np
import os
from PIL import Image
import math
import cv2
def rgb2hsl(inputColor):
    ''' Converts RGB colorspace to HSL (Hue/Saturation/Value) colorspace.
        Formula from http://www.easyrgb.com/math.php?MATH=M18#text18

        Input:
            (r,g,b) (integers 0...255) : RGB values

        Ouput:
            (h,s,l) (floats 0...1): corresponding HSL values


    '''
    r = inputColor[0]
    g = inputColor[1]
    b = inputColor[2]
    if not (0 <= r <= 255): print("r (red) parameter must be between 0 and 255.")
    if not (0 <= g <= 255): print("g (green) parameter must be between 0 and 255.")
    if not (0 <= b <= 255): print("r (blue) parameter must be between 0 and 255.")

    var_R = r / 255.0
    var_G = g / 255.0
    var_B = b / 255.0

    var_Min = min(var_R, var_G, var_B)  # Min. value of RGB
    var_Max = max(var_R, var_G, var_B)  # Max. value of RGB
    del_Max = var_Max - var_Min  # Delta RGB value

    l = (var_Max + var_Min) / 2.0
    h = 0.0
    s = 0.0
    if del_Max != 0.0:
        if l < 0.5:
            s = del_Max / (var_Max + var_Min)
        else:
            s = del_Max / (2.0 - var_Max - var_Min)
        del_R = (((var_Max - var_R) / 6.0) + (del_Max / 2.0)) / del_Max
        del_G = (((var_Max - var_G) / 6.0) + (del_Max / 2.0)) / del_Max
        del_B = (((var_Max - var_B) / 6.0) + (del_Max / 2.0)) / del_Max
        if var_R == var_Max:
            h = del_B - del_G
        elif var_G == var_Max:
            h = (1.0 / 3.0) + del_R - del_B
        elif var_B == var_Max:
            h = (2.0 / 3.0) + del_G - del_R
        while h < 0.0: h += 1.0
        while h > 1.0: h -= 1.0

        h = round(h * 360)
        s = round(s * 360)
        l = round(l * 360)

    return (h, s, l)

for filename in os.listdir(r"E://街景图片2"):
        #print(filename) #just for test
        #img is used to store the image data
       #img = cv2.imread("E://街景图片" + "//" + filename)
        im = Image.open("E://街景图片2" + "//" + filename)
        pix = im.load()

        width = im.size[0]
        height = im.size[1]

        green=0
        other=0
        for x in range(width):
            for y in range(height):
                temp = []
                r, g, b = pix[x, y]
                #print(pix[x,y])
                temp.append(r)
                temp.append(g)
                temp.append(b)

                h,s,l=rgb2hsl( temp)
                if ((70<h<160)and(10<s<100)and(10<l<90)):
                    green=green+1
                else:
                    other=other+1

                print(h,s,l)
        print(green, other)
        efficience=green/(green+other)
        print("\n")
        print("lushilu:",efficience)