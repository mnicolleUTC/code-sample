#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 11:31:14 2022
https://stackoverflow.com/questions/2369492/generate-a-heatmap-in-matplotlib-using-a-scatter-data-set
@author: nicollemathieu
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.ndimage.filters import gaussian_filter
import numpy as np

def myplot(x, y, s, bins=1000):
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins)
    heatmap = gaussian_filter(heatmap, sigma=s)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent

if __name__ == '__main__':
    file = '/Users/nicollemathieu/Desktop/file_xy99.csv'
    df = pd.read_csv(file)    
    df["Y"] = -df["Y"] #Retournement du graphique selon y pour correspondre à la réalité 
    x = df["X"]
    y = df["Y"]
    #df_cd8 = df[df["Phenotype"]=="CD8"]
    #df_cdc1 = df[df["Phenotype"]=="cDC1"]
    #plt.plot( 'X', 'Y', "", data=df_cd8, linestyle='', marker='o', color = 'b',markersize = 0.6)
    #plt.plot( 'X', 'Y', "", data=df_cdc1, linestyle='', marker='o', color = 'r',markersize = 1)
    fig,ax = plt.subplots()
    img, extent = myplot(x, y, 8)
    ax.imshow(img, extent=extent, origin='lower', cmap=cm.jet)
    plt.savefig('/Users/nicollemathieu/Desktop/plot_heatmap8.jpeg')
    plt.show()
