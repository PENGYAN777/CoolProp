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


data = pd.read_csv("history.csv", ",", skiprows=0)






# fig 1
fig1 = plt.figure( dpi=300)
lwh = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(data.iloc[:,2] , data.iloc[:,3], 'k', lw=lwh, label="$\\rho$")
axes.plot(data.iloc[:,2] , data.iloc[:,4], 'r', lw=lwh, label="$\\rho u$")
axes.plot(data.iloc[:,2] , data.iloc[:,5], 'g', lw=lwh, label="$\\rho v$")
axes.plot(data.iloc[:,2] , data.iloc[:,6], 'b', lw=lwh, label="$\\rho e$")


axes.set_xlabel('Number of iteration',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('Residuals',fontsize=12) 

axes.set_title('History of residuals',fontsize=14)

axes.legend(loc=0) # 
# axes.set_xlim(0,700)
# axes.set_ylim(-12,3)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("dense_residual.pdf")

