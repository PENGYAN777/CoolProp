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

pr= pd.read_csv("../pr/prsh.csv", ",", skiprows=0)
cp= pd.read_csv("../coolprop/m4sh.csv", ",", skiprows=0)
nimoc= pd.read_csv("NIMOC_lower_boundary.csv", ",", skiprows=0)

nn = len(pr.iloc[:,9])
# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(pr.iloc[:,9] , pr.iloc[:,1], 'k', lw=lwh, label="SU2 PR")
axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,6], 'r', lw=lwh, label="NIMOC CoolProp")
axes.plot(cp.iloc[:,9] , cp.iloc[:,1], 'g', lw=lwh, label="SU2 CoolProp")
for i in range(nn):
    dmax[i] = max(pr.iloc[i,1],cp.iloc[i,1])
    dmin[i] = min(pr.iloc[i,1],cp.iloc[i,1])
    
ax2.plot(pr.iloc[:,9], (dmax-dmin)/dmax*100 , 'k*', lw=lwh/10)    
ax2.set_ylabel('$\Delta_M$(%)',fontsize=12) 
ax2.set_ylim(0,15)
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('Mach number',fontsize=12) 
axes.set_title('Mach number along centerline',fontsize=14)

axes.legend(loc=0,fontsize=8) 
# axes.set_xlim(-12,7)
# axes.set_ylim(0.2,1)
fig1.savefig("nonmonotone_M.pdf")

# fig2 = plt.figure( dpi=300)
# lwh = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(pr.iloc[:,9] , np.sqrt((pr.iloc[:,2]/pr.iloc[:,0])**2 + (pr.iloc[:,3]/pr.iloc[:,0])**2), 'k', lw=lwh, label="SU2 PR")
# axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,5]*nimoc.iloc[:,6], 'r', lw=lwh, label="NIMOC CoolProp")
# axes.plot(cp.iloc[:,9] , np.sqrt((cp.iloc[:,2]/cp.iloc[:,0])**2 + (cp.iloc[:,3]/cp.iloc[:,0])**2), 'g', lw=lwh, label="SU2 CoolProp")
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('Velocity[m/s]',fontsize=12) 
# axes.set_title('Velocity along centerline',fontsize=14)
# axes.legend(loc=6,fontsize=8) 
# fig2.savefig("nonmonotone_velocity.pdf")

fig3 = plt.figure( dpi=300)
lwh = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(pr.iloc[:,9] , pr.iloc[:,6], 'k', lw=lwh, label="SU2 PR")
axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,8], 'r', lw=lwh, label="NIMOC CoolProp")
axes.plot(cp.iloc[:,9] , cp.iloc[:,6], 'g', lw=lwh, label="SU2 CoolProp")

for i in range(nn):
    dmax[i] = max(pr.iloc[i,6],cp.iloc[i,6])
    dmin[i] = min(pr.iloc[i,6],cp.iloc[i,6])
    
ax2.plot(pr.iloc[:,9], (dmax-dmin)/dmax*100 , 'k*', lw=lwh/10)    
ax2.set_ylabel('$\Delta_T$(%)',fontsize=12) 
ax2.set_ylim(0,2)
axes.set_ylim(400,540)
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('T[K]',fontsize=12) 
axes.set_title('Temperature along centerline',fontsize=14)
axes.legend(loc=6,fontsize=8) 
fig3.savefig("nonmonotone_T.pdf")

fig4 = plt.figure( dpi=300)
lwh = 2
axes = fig4.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(pr.iloc[:,9] , pr.iloc[:,0], 'k', lw=lwh, label="SU2 PR")
axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,7], 'r', lw=lwh, label="NIMOC CoolProp")
axes.plot(cp.iloc[:,9] , cp.iloc[:,0], 'g', lw=lwh, label="SU2 CoolProp")
for i in range(nn):
    dmax[i] = max(pr.iloc[i,0],cp.iloc[i,0])
    dmin[i] = min(pr.iloc[i,0],cp.iloc[i,0])
    
ax2.plot(pr.iloc[:,9], (dmax-dmin)/dmax*100 , 'k*', lw=lwh/10)    
ax2.set_ylabel('$\Delta_{\\rho}$(%)',fontsize=12) 
ax2.set_ylim(-2,20)
axes.set_ylim(0,400)
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$\\rho[kg/m^3$]',fontsize=12) 
axes.set_title('Density along centerline',fontsize=14)
axes.legend(loc=0,fontsize=8) 
fig4.savefig("nonmonotone_rho.pdf")

fig5 = plt.figure( dpi=300)
lwh = 2
axes = fig5.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(pr.iloc[:,9] , pr.iloc[:,5]/pr.iloc[:,0]/pr.iloc[:,6]/51.2, 'k', lw=lwh, label="SU2 PR")
axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,9]/nimoc.iloc[:,8]/nimoc.iloc[:,7]/51.2, 'r', lw=lwh, label="NIMOC CoolProp")
axes.plot(cp.iloc[:,9] , cp.iloc[:,5]/cp.iloc[:,0]/cp.iloc[:,6]/51.2, 'g', lw=lwh, label="SU2 CoolProp")
for i in range(nn):
    dmax[i] = max(pr.iloc[i,5]/pr.iloc[i,0]/pr.iloc[i,6]/51.2, cp.iloc[i,5]/cp.iloc[i,0]/cp.iloc[i,6]/51.2)
    dmin[i] = min(pr.iloc[i,5]/pr.iloc[i,0]/pr.iloc[i,6]/51.2, cp.iloc[i,5]/cp.iloc[i,0]/cp.iloc[i,6]/51.2)
    
ax2.plot(pr.iloc[:,9], (dmax-dmin)/dmax*100 , 'k*', lw=lwh/10)    
ax2.set_ylabel('$\Delta_Z$(%)',fontsize=12) 
# ax2.set_ylim(-2,20)
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('Z',fontsize=12) 
axes.set_title('Compressibility factor along centerline',fontsize=14)
axes.legend(loc=6,fontsize=8)
fig5.savefig("nonmonotone_Z.pdf") 

fig6 = plt.figure( dpi=300)
lwh = 2
axes = fig6.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
nn = len(pr.iloc[:,9])
ax2 = axes.twinx()
dmax = np.zeros(nn)
dmin = np.zeros(nn)
axes.plot(pr.iloc[:,9] , pr.iloc[:,5], 'k', lw=lwh, label="SU2 PR")
axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,9], 'r', lw=lwh, label="NIMOC CoolProp")
axes.plot(cp.iloc[:,9] , cp.iloc[:,5], 'g', lw=lwh, label="SU2 CoolProp")
for i in range(nn):
    dmax[i] = max(pr.iloc[i,5],cp.iloc[i,5])
    dmin[i] = min(pr.iloc[i,5],cp.iloc[i,5])
    
ax2.plot(pr.iloc[:,9], (dmax-dmin)/dmax*100 , 'k*', lw=lwh/10)    
ax2.set_ylabel('$\Delta_P$(%)',fontsize=12) 
ax2.set_ylim(0,9)
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('P[Pa]',fontsize=12) 
axes.set_title('Pressure along centerline',fontsize=14)
axes.legend(loc=6,fontsize=8) 
fig6.savefig("nonmonotone_P.pdf")

# fig7 = plt.figure( dpi=300)
# lwh = 2
# axes = fig7.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(pr.iloc[:,9] , np.sqrt((pr.iloc[:,2]/pr.iloc[:,0])**2 + (pr.iloc[:,3]/pr.iloc[:,0])**2)/pr.iloc[:,1], 'k', lw=lwh, label="SU2 PR")
# axes.plot(nimoc.iloc[:,1] , nimoc.iloc[:,5], 'r', lw=lwh, label="NIMOC CoolProp")
# axes.plot(cp.iloc[:,9] , np.sqrt((cp.iloc[:,2]/cp.iloc[:,0])**2 + (cp.iloc[:,3]/cp.iloc[:,0])**2)/cp.iloc[:,1], 'g', lw=lwh, label="SU2 CoolProp")
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('c[m/s]',fontsize=12) 
# axes.set_title('Sound speed along centerline',fontsize=14)
# axes.legend(loc=2,fontsize=8) 
# fig7.savefig("nonmonotone_c.pdf")


fig8 = plt.figure( dpi=300)
lwh = 2
axes = fig8.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(pr.iloc[:,9] , 1-pr.iloc[:,14]-1/pr.iloc[:,1]/pr.iloc[:,1], 'k', lw=lwh, label="SU2 PR")
axes.plot(nimoc.iloc[:,1] , 1-nimoc.iloc[:,12]-1/nimoc.iloc[:,6]/nimoc.iloc[:,6], 'r', lw=lwh, label="NIMOC CoolProp")
axes.plot(cp.iloc[:,9] , 1-cp.iloc[:,14]-1/cp.iloc[:,1]/cp.iloc[:,1], 'g', lw=lwh, label="SU2 CoolProp")
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$dM/d\\rho$',fontsize=12) 
axes.set_title('$dM/d\\rho$ along centerline',fontsize=14)

sub_axes = plt.axes([0.5, 0.5, 0.25, 0.25]) 
x = []
# plot the zoomed portion
for i in cp.iloc[:,9].index:
    if (1-cp.iloc[i,14]-1/cp.iloc[i,1]/cp.iloc[i,1])>0:
        x.append(i)
sub_axes.plot(cp.iloc[x[0]:x[-1],9], 1-cp.iloc[x[0]:x[-1],14]-1/cp.iloc[x[0]:x[-1],1]/cp.iloc[x[0]:x[-1],1], 'g') 


axes.legend(loc=2,fontsize=8) 
fig8.savefig("nonmonotone_g.pdf")
