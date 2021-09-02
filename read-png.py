# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 11:53:38 2021

@author: Tony Tsou
"""
import cv2

f = open('bg.txt', 'w')
img = cv2.imread('bg.png')
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if j == 0:
            f.write('[[{}, {}, {}],\n'.format(img[i,j,0], img[i,j,1], img[i,j,2]))
        elif j == img.shape[1]-1:
            f.write('[{}, {}, {}]],\n'.format(img[i,j,0], img[i,j,1], img[i,j,2]))
        else:
            f.write('[{}, {}, {}],\n'.format(img[i,j,0], img[i,j,1], img[i,j,2]))
f.close()
