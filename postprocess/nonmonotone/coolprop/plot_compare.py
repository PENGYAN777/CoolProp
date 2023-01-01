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
import os
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')

mesh1= pd.read_csv("m1.csv", ",", skiprows=0)
mesh2= pd.read_csv("m2.csv", ",", skiprows=0)
mesh3= pd.read_csv("m3.csv", ",", skiprows=0)
mesh4= pd.read_csv("m4.csv", ",", skiprows=0)







# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh1.iloc[:,9] , mesh1.iloc[:,1], 'k', lw=lwh, label="2k")
axes.plot(mesh2.iloc[:,9] , mesh2.iloc[:,1], 'r', lw=lwh, label="4k")
axes.plot(mesh3.iloc[:,9] , mesh3.iloc[:,1], 'g', lw=lwh, label="8k")
axes.plot(mesh4.iloc[:,9] , mesh4.iloc[:,1], 'b', lw=lwh, label="18k")


axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
# axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_ylabel('Mach number',fontsize=12) 

axes.set_title('Mach number along centerline',fontsize=14)

axes.legend(loc=2) # 
# axes.set_xlim(0,7)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nonmonotone_gv.pdf")

