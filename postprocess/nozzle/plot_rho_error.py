#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:33:08 2022

@author: yan
"""

"""
if you do not have CoolProp on your PC, run the following commented code
"""
# import sys
# import subprocess

# # download CoolProp
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'CoolProp'])

import matplotlib
import numpy as np
import CoolProp as CP
import matplotlib.pyplot as plt
import scipy.interpolate
import pandas as pd


T = 542
P = np.linspace(5e5,1.4e6,2000)
P = pd.Series(P)
error = np.zeros(P.size)
for i in P.index:
    rho_coolprop =  CP.CoolProp.PropsSI('Dmass','T',T,'P',P[i],"HEOS::MDM")
    rho_pr =  CP.CoolProp.PropsSI('Dmass','T',T,'P',P[i],"PR::MDM") 
    error[i] = ( rho_coolprop - rho_pr)/ rho_coolprop *100


# fig 1
fig1 = plt.figure( dpi=300)
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(P , error, 'k', lw=2)

axes.set_xlabel('$P[Pa]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$\\Delta \\rho \%$',fontsize=12) 

axes.set_title('Difference of density vs Pressure',fontsize=14)

# axes.legend(loc=6) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("difference_density.pdf")
