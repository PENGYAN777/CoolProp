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


m1 = pd.read_csv("mesh1.csv", ",", skiprows=0)
m2 = pd.read_csv("mesh2.csv", ",", skiprows=0)
m3 = pd.read_csv("mesh3.csv", ",", skiprows=0)





# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(m1.iloc[:,4]*1000 , m1.iloc[:,2], 'k', lw=lwh, label="n=6k")
axes.plot(m2.iloc[:,4]*1000 , m2.iloc[:,2], 'r', lw=lwh, label="n=12k")
axes.plot(m3.iloc[:,4]*1000 , m3.iloc[:,2], 'g', lw=lwh, label="n=22k")


axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 

axes.set_title('Static-to-total pressure ratio along centerline',fontsize=14)

axes.legend(loc=6) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_di_ce_gv_p.pdf")

# fig 2
fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(m1.iloc[:,4]*1000 , m1.iloc[:,0], 'k', lw=lwh, label="n=6k")
axes.plot(m2.iloc[:,4]*1000 , m2.iloc[:,0], 'r', lw=lwh, label="n=12k")
axes.plot(m3.iloc[:,4]*1000 , m3.iloc[:,0], 'g', lw=lwh, label="n=22k")


axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('Mach',fontsize=12) 

axes.set_title('Mach number along centerline',fontsize=14)

axes.legend(loc=6) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig2.savefig("nozzle_di_ce_gv_m.pdf")

