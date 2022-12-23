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
axes.plot(m1.iloc[:,5]*1000 , m1.iloc[:,3], 'k', lw=lwh, label="n=6k")
axes.plot(m2.iloc[:,5]*1000 , m2.iloc[:,3], 'r', lw=lwh, label="n=12k")
axes.plot(m3.iloc[:,5]*1000 , m3.iloc[:,3], 'g', lw=lwh, label="n=22k")



# axes2.plot(m3.iloc[:,5]*1000 , m3.iloc[:,9]/m3.iloc[0,9], 'k--', lw=lwh/2, label="$\\overline{s}$")
# axes2.plot(m3.iloc[:,5]*1000 , m3.iloc[:,10]/m3.iloc[0,10], 'r--', lw=lwh/2, label="$\\overline{h^t}$")

axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('Distribution of $P/P_t$ along centerline',fontsize=14)

axes.legend(loc=3) # 
# axes2.legend(loc=1) # 
# axes.set_xlim(0,120)
# axes2.set_ylim(0,2)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_de_ce_gv_p.pdf")


# figure 2
fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(m1.iloc[:,5]*1000 , m1.iloc[:,9]/m1.iloc[0,9], 'k', lw=lwh, label="n=6k")
axes.plot(m2.iloc[:,5]*1000 , m2.iloc[:,9]/m2.iloc[0,9], 'k--', lw=lwh, label="n=12k")
axes.plot(m3.iloc[:,5]*1000 , m3.iloc[:,9]/m3.iloc[0,9], 'ko', lw=lwh, label="n=22k")

axes2 = axes.twinx()
axes2.plot(m1.iloc[:,5]*1000 , m1.iloc[:,10]/m1.iloc[0,10], 'r', lw=lwh, label="n=6k")
axes2.plot(m2.iloc[:,5]*1000 , m2.iloc[:,10]/m2.iloc[0,10], 'r--', lw=lwh, label="n=12k")
axes2.plot(m3.iloc[:,5]*1000 , m3.iloc[:,10]/m3.iloc[0,10], 'ro', lw=lwh, label="n=22k")

axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$\\overline{s}$',fontsize=12) 
axes2.set_ylabel('$\\overline{h^t}$',fontsize=12) 
axes.set_title('Distribution of $\\overline{s}$ and $\\overline{h^t}$ along centerline',fontsize=14)
axes2.yaxis.label.set_color('red')
axes.legend(loc=2) # 
# axes2.legend(loc=1) # 
# axes.set_xlim(0,120)
axes.set_ylim(0.9,1.1)
axes2.set_ylim(0,3)
axes2.legend(loc=1) # 2 means left top
fig2.savefig("nozzle_de_ce_gv_hs.pdf")



