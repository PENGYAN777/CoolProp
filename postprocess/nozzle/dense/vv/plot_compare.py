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


coolprop = pd.read_csv("../coolprop/mesh3.csv", ",", skiprows=0)
pr = pd.read_csv("../pr/pr.csv", ",", skiprows=0)
ex = pd.read_csv("ex_p.csv", "  ", skiprows=0)




# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(coolprop.iloc[:,5]*1000 , coolprop.iloc[:,3], 'k', lw=lwh, label="SU2 CoolProp")
axes.plot(pr.iloc[:,4]*1000 , pr.iloc[:,2], 'r', lw=lwh, label="SU2 PR")

plt.errorbar(ex.iloc[:,0]*1000, ex.iloc[:,1]/9.04e5, ex.iloc[:,2]/9.04e5, fmt=' ', marker='o',mfc='black', 
              ms=4, mec='black', mew=1, label="Experiment")



axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 

axes.set_title('Distribution of $P/P_t$ along centerline',fontsize=14)

axes.legend(loc=3) # 
axes.set_xlim(0,120)
# axes.set_ylim(0,2)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_de_vv.pdf")

