#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:20:51 2022

@author: yan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

wall = pd.read_csv("nozzle.csv", " ", skiprows=0)
inlet = pd.read_csv("inlet.csv", ",", skiprows=0)
outlet = pd.read_csv("outlet.csv", ",", skiprows=0)
sym = pd.read_csv("sym.csv", ",", skiprows=0)

fig1 = plt.figure( dpi=300)
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(wall.iloc[:,1]*1000  , wall.iloc[:,2]*1000 , 'k', lw=2, label="wall")
axes.plot(inlet.iloc[:,0]*1000  , inlet.iloc[:,1]*1000 , 'r', lw=2, label="inlet")
axes.plot(outlet.iloc[:,0]*1000  , outlet.iloc[:,1]*1000 , 'g', lw=2, label="outlet")
axes.plot(sym.iloc[:,0]*1000  , sym.iloc[:,1]*1000 , 'b', lw=2, label="symmetry")
axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$Y[mm]$',fontsize=12) 
axes.set_aspect('equal', 'box')
axes.set_title('Geometry of nozzle M1.5',fontsize=14)

axes.legend(loc=1 , prop={'size': 6}) # 
# axes.set_xlim(0,0.12)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("geo.pdf")
