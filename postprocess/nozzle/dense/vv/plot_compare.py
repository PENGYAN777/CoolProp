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


coolprop_euler = pd.read_csv("../coolprop_euler/mesh3.csv", ",", skiprows=0)
coolprop_rans = pd.read_csv("../coolprop_rans/coolprop_rans.csv", ",", skiprows=0)
pr_euler = pd.read_csv("../pr_euler/pr.csv", ",", skiprows=0)
pr_rans = pd.read_csv("../pr_rans/pr_rans.csv", ",", skiprows=0)
fp_euler = pd.read_csv("../fp_euler/fp_euler.csv", ",", skiprows=0)
fp_rans = pd.read_csv("../fp_rans/fp_rans.csv", ",", skiprows=0)
nimoc_euler = pd.read_csv("../NIMOC/NIMOC_lower_boundary.csv", ",", skiprows=0)
ex = pd.read_csv("ex_p.csv", "  ", skiprows=0)

nn = 4

# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(coolprop_euler.iloc[:,5]*1000 , coolprop_euler.iloc[:,3], 'k', lw=lwh, label="SU2 CoolProp Euler")
axes.plot(coolprop_rans.iloc[:,4]*1000 , coolprop_rans.iloc[:,2], 'k--', lw=lwh, label="SU2 CoolProp RANS")
axes.plot(pr_euler.iloc[:,4]*1000 , pr_euler.iloc[:,2], 'r', lw=lwh, label="SU2 PR Euler")
axes.plot(pr_rans.iloc[:,4]*1000 , pr_rans.iloc[:,2], 'r--', lw=lwh, label="SU2 PR RANS")
axes.plot(fp_euler.iloc[:,11]*1000 , fp_euler.iloc[:,8], 'b', lw=lwh, label="SU2 FluidProp Euler")
axes.plot(fp_rans.iloc[:,19]*1000 , fp_rans.iloc[:,15], 'b--', lw=lwh, label="SU2 FluidProp RANS")
axes.plot(nimoc_euler.iloc[:,1]*1000+86.4 , nimoc_euler.iloc[:,9]/9.04e5, 'g', lw=lwh, label="NIMOC Coolrop Euler")

axes.errorbar(ex.iloc[:,0]*1000, ex.iloc[:,1]/9.04e5, ex.iloc[:,2]/9.04e5, fmt=' ', marker='o',mfc='black', 
              ms=4, mec='black', mew=1, label="Experiment")

for i in range(nn):
    x = abs(pr_euler.iloc[:,4]-ex.iloc[i,0])
    j = x.idxmin()
    dmax[i] = max(pr_euler.iloc[j,2],pr_rans.iloc[j,2],coolprop_euler.iloc[j,3]
                    ,coolprop_rans.iloc[j,2],fp_euler.iloc[j,8],fp_rans.iloc[j,15],
                    ex.iloc[i,1]/9.04e5)
    dmin[i] = min(pr_euler.iloc[j,2],pr_rans.iloc[j,2],coolprop_euler.iloc[j,3]
                    ,coolprop_rans.iloc[j,2],fp_euler.iloc[j,8],fp_rans.iloc[j,15],
                    ex.iloc[i,1]/9.04e5)

ax2.plot(ex.iloc[0:4,0]*1000, (dmax-dmin)/dmax*100 , 'k*', lw=lwh)    
ax2.set_ylabel('$\Delta_{P/P_t}$(%)',fontsize=12) 
ax2.set_ylim(0,6)
axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 

axes.set_title('Distribution of $P/P_t$ along centerline',fontsize=14)

axes.legend(loc=6) # 
axes.set_xlim(0,120)
# axes.set_ylim(0,2)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_de_vv.pdf")


