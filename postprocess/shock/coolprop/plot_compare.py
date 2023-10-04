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


mesh3= pd.read_csv("m0.csv", ",", skiprows=0)
mesh4= pd.read_csv("m2.csv", ",", skiprows=0)
mesh5= pd.read_csv("m3.csv", ",", skiprows=0)
mesh6= pd.read_csv("m4.csv", ",", skiprows=0)
m4new = pd.read_csv("m4new.csv", ",", skiprows=0)





# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh3.iloc[:,-3] , mesh3.iloc[:,6]/1499900, 'k', lw=lwh, label="5k")
axes.plot(mesh4.iloc[:,-3] , mesh4.iloc[:,6]/1499900, 'r', lw=lwh, label="12k")
axes.plot(mesh5.iloc[:,-3] , mesh5.iloc[:,6]/1499900, 'g', lw=lwh, label="18k")
axes.plot(mesh6.iloc[:,-3] , mesh6.iloc[:,6]/1499900, 'b', lw=lwh, label="30k")

# sub_axes = plt.axes([0.26, 0.26, 0.25, 0.25]) 

# # sub_axes.plot(m6new.iloc[:,6] , m6new.iloc[:,-3], 'k', lw=lwh, label="$s$")
# sub_axes.plot(m4new.iloc[:,11] , m4new.iloc[:,-3], 'k', lw=lwh, label="$s$")
# sub_axes.set_ylabel('$s[J/K/mol]$',fontsize=10) 
# sub_axes.set_ylim([754.5, 760])

axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along y$=0.4 mm$',fontsize=14)
axes.legend(loc=1) # 

fig1.savefig("shock_gv_p.pdf")

# fig 2
fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh3.iloc[:,-3] , mesh3.iloc[:,2], 'k', lw=lwh, label="5k")
axes.plot(mesh4.iloc[:,-3] , mesh4.iloc[:,2], 'r', lw=lwh, label="12k")
axes.plot(mesh5.iloc[:,-3] , mesh5.iloc[:,2], 'g', lw=lwh, label="18k")
axes.plot(mesh6.iloc[:,-3] , mesh6.iloc[:,2], 'b', lw=lwh, label="30k")

# sub_axes = plt.axes([0.26, 0.26, 0.25, 0.25]) 

# # sub_axes.plot(m6new.iloc[:,6] , m6new.iloc[:,-3], 'k', lw=lwh, label="$s$")
# sub_axes.plot(m4new.iloc[:,11] , m4new.iloc[:,-3], 'k', lw=lwh, label="$s$")
# sub_axes.set_ylabel('$s[J/K/mol]$',fontsize=10) 
# sub_axes.set_ylim([754.5, 760])

axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('Mach',fontsize=12) 
axes.set_title('Mach number along y$=0.4 mm$',fontsize=14)
axes.legend(loc=1) # 

fig2.savefig("shock_gv_m.pdf")

