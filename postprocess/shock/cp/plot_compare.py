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


mesh0= pd.read_csv("m0.csv", ",", skiprows=0)
mesh2= pd.read_csv("m2.csv", ",", skiprows=0)
# mesh3= pd.read_csv("m3.csv", ",", skiprows=0)
mesh5= pd.read_csv("m5.csv", ",", skiprows=0)

m0new= pd.read_csv("m0new.csv", ",", skiprows=0)





Pc = 1410044
P1 = 1499900
dc = 256.74
Tc = 564.09
# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh0.iloc[:,-3] , mesh0.iloc[:,6]/Pc, 'k', lw=lwh, label="5k")
axes.plot(mesh2.iloc[:,-3] , mesh2.iloc[:,6]/Pc, 'r', lw=lwh, label="12k")
# axes.plot(mesh3.iloc[:,-3] , mesh3.iloc[:,6]/Pc, 'g', lw=lwh, label="18k")
# axes.plot(mesh4.iloc[:,-3] , mesh4.iloc[:,6]/Pc, 'b', lw=lwh, label="30k")
axes.plot(mesh5.iloc[:,-3] , mesh5.iloc[:,6]/Pc, 'b', lw=lwh, label="33k")
axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# sub_axes = plt.axes([0.26, 0.26, 0.25, 0.25]) 

# # sub_axes.plot(m6new.iloc[:,6] , m6new.iloc[:,-3], 'k', lw=lwh, label="$s$")
# sub_axes.plot(m4new.iloc[:,11] , m4new.iloc[:,-3], 'k', lw=lwh, label="$s$")
# sub_axes.set_ylabel('$s[J/K/mol]$',fontsize=10) 
# sub_axes.set_ylim([754.5, 760])

axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_c$',fontsize=12) 
axes.set_title('$P/P_c$ along y$=0.4 mm$',fontsize=14)
axes.legend(loc=1) # 

fig1.savefig("shock_gv_p.pdf")

# fig 2
fig2 = plt.figure( dpi=300)
lwh = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh0.iloc[:,-3] , mesh0.iloc[:,2], 'k', lw=lwh, label="5k")
axes.plot(mesh2.iloc[:,-3] , mesh2.iloc[:,2], 'r', lw=lwh, label="12k")
# axes.plot(mesh3.iloc[:,-3] , mesh3.iloc[:,2], 'g', lw=lwh, label="18k")
# axes.plot(mesh4.iloc[:,-3] , mesh4.iloc[:,2], 'b', lw=lwh, label="30k")
axes.plot(mesh5.iloc[:,-3] , mesh5.iloc[:,2], 'b', lw=lwh, label="33k")

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

# fig 3
fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(mesh0.iloc[:,-3] , mesh0.iloc[:,0]/dc, 'k', lw=lwh, label="5k")
axes.plot(mesh2.iloc[:,-3] , mesh2.iloc[:,0]/dc, 'r', lw=lwh, label="12k")
# axes.plot(mesh3.iloc[:,-3] , mesh3.iloc[:,0]/dc, 'g', lw=lwh, label="18k")
# axes.plot(mesh4.iloc[:,-3] , mesh4.iloc[:,0]/dc, 'b', lw=lwh, label="30k")
axes.plot(mesh5.iloc[:,-3] , mesh5.iloc[:,0]/dc, 'b', lw=lwh, label="33k")


axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$\\rho$/$\\rho_c$',fontsize=12) 
axes.set_title('$\\rho$ / $\\rho_c$ along y$=0.4 mm$',fontsize=14)
axes.legend(loc=1) # 

fig3.savefig("shock_gv_rho.pdf")

# fig 4
# fig4 = plt.figure( dpi=300)
# lwh = 2
# axes = fig4.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(m0new.iloc[:,-5] , m0new.iloc[:,-1], 'k', lw=lwh, label="5k")
# # axes.plot(m2new.iloc[:,-5] , m2new.iloc[:,-1], 'r', lw=lwh, label="12k")
# # axes.plot(m3new.iloc[:,-5] , m3new.iloc[:,-1], 'g', lw=lwh, label="18k")
# # axes.plot(m4new.iloc[:,-5] , m4new.iloc[:,-1], 'b', lw=lwh, label="30k")


# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$\\Gamma$',fontsize=12) 
# axes.set_title('$\\Gamma$ along y$=0.4 mm$',fontsize=14)
# axes.legend(loc=1) # 

# fig4.savefig("shock_gv_Gamma.pdf")


