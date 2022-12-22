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


ig = pd.read_csv("mesh1.csv", ",", skiprows=0)





# fig 1
fig1 = plt.figure( dpi=300)
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ig.iloc[:,4]*1000 , ig.iloc[:,2], 'k', lw=2, label="n=6k")


axes.set_xlabel('$X[mm]$',fontsize=12)
#axes.set_yscale("log")
axes.set_ylabel('$P/P_t$',fontsize=12) 

axes.set_title('Static-to-total pressure ratio along centerline',fontsize=14)

axes.legend(loc=6) # 
# axes.set_xlim(0,120)
# axes.set_ylim(0.2,1)
#axes.legend(loc=2) # 2 means left top
fig1.savefig("nozzle_di_ce_gv.pdf")

