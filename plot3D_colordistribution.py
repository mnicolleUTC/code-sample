#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:10:46 2022
@author: nicollemathieu
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import matplotlib as mpl


if __name__ == '__main__':
    file = "/Users/nicollemathieu/Desktop/temp2.jpg"
    arr = np.array(io.imread(file))
    #mpl.rcParams['agg.path.chunksize'] = arr.shape[0]*arr.shape[1]+10
    #Si erreur cela est du au alpha channel
    red = arr[:,:,0].flatten()
    green = arr[:,:,1].flatten()
    blue = arr[:,:,2].flatten()
    colors = arr.reshape(arr.shape[0]*arr.shape[1],3)/255
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.scatter(red,green,blue,c = colors)
