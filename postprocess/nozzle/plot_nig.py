#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:01:08 2022

@author: yan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:35:29 2022

@author: yan

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


ig = pd.read_csv("ig_nig.csv", ",", skiprows=0)
pr = pd.read_csv("pr_nig.csv", ",", skiprows=0)
cp = pd.read_csv("coolprop_euler.csv", ",", skiprows=0)




# plot (M,Z)
fig1 = plt.figure( dpi=300)
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ig.iloc[:,5]*1000 , ig.iloc[:,2]/9e5, 'k', lw=2, label="PIG")
axes.plot(pr.iloc[:,5]*1000 , pr.iloc[:,2]/9e5, 'r', lw=2, label="PR")
axes.plot(cp.iloc[:,5]*1000 , cp.iloc[:,2]/9e5, 'b', lw=2, label="CoolProp")
# axes2=axes.twinx()
# axes2.plot(cp.iloc[:,5]*1000 , (cp.iloc[:,2]-pr.iloc[:,2])/cp.iloc[:,2]*100, 'k--', lw=2)

axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
#axes2.set_ylabel("$\\Delta P/P_t \\%$",fontsize=12) 
axes.set_title('Pressure along centerline',fontsize=14)

axes.legend(loc=1) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_p_nicfd.pdf")

# fig 2
fig1 = plt.figure( dpi=300)
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ig.iloc[:,5]*1000 , ig.iloc[:,0], 'k', lw=2, label="PIG")
axes.plot(pr.iloc[:,5]*1000 , pr.iloc[:,0], 'r', lw=2, label="PR")
axes.plot(cp.iloc[:,5]*1000 , cp.iloc[:,0], 'b', lw=2, label="CoolProp")

axes2=axes.twinx()
axes2.plot(cp.iloc[:,5]*1000 , (cp.iloc[:,0]-pr.iloc[:,0])/cp.iloc[:,0]*100, 'k--', lw=2)

axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$\\rho(kg/m^3$)',fontsize=12) 
axes2.set_ylabel("$\\Delta \\rho \\%$",fontsize=12) 
axes.set_title('Denisty along centerline',fontsize=14)

axes.legend(loc=1) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_rho_nicfd.pdf")

