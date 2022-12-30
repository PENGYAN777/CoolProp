#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 14:59:54 2022

@author: user
"""
import CoolProp as CP
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import os
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')

nimoc= pd.read_csv("../vv/NIMOC_lower_boundary.csv", ",", skiprows=0)

P = nimoc.iloc[:,9]
T = nimoc.iloc[:,8]
x = nimoc.iloc[:,1]
rho = np.zeros(P.size)
c = np.zeros(P.size)
h = np.zeros(P.size)
s = np.zeros(P.size)
u = np.zeros(P.size)
M = np.zeros(P.size)
fluidname = "MM"

ht = CP.CoolProp.PropsSI('Hmass','T',538.15,'P',2.95e6,fluidname) 
for i in range(P.size):
       rho[i]= CP.CoolProp.PropsSI('Dmass','T',T[i],'P',P[i],fluidname) 
       c[i]= CP.CoolProp.PropsSI('A','T',T[i],'P',P[i],fluidname) 
       h[i]= CP.CoolProp.PropsSI('Hmass','T',T[i],'P',P[i],fluidname) 
       s[i]= CP.CoolProp.PropsSI('Smass','T',T[i],'P',P[i],fluidname) 
       u[i] = math.sqrt((ht-h[i])*2)
       M[i]= u[i]/c[i]
       
       
       

fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) 
axes.plot(x, s, 'k', lw=lwh, label="CoolProp")

# axes2 = axes.twinx()
# axes2.plot(x, nimoc.iloc[:,5], 'r', lw=lwh, label="NIMOC")


axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('s',fontsize=12) 
# axes2.set_ylabel('c', fontsize=12) 
# axes2.yaxis.label.set_color('red')
axes.legend(loc=2) # 
axes.set_ylim([800, 900])
# axes2.legend(loc=4) # 

axes.set_title('Speed of sound along centerline',fontsize=14)
fig1.savefig("s.pdf")
