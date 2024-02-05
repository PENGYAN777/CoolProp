#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:10:17 2022

@author: P.Yan

read csv file with P,T, compute Z, Gamma and wirte in thee csv file
"""

import numpy as np
import CoolProp as CP
import pandas as pd

fluidname = "PR::MDM"
data = pd.read_csv("m6.csv", ",")
P = data.iloc[:,6] 
T = data.iloc[:,8] 
D = data.iloc[:,0] 
print("size", P.index)

G = np.zeros(P.size)
Z = np.zeros(P.size)
# ht = np.zeros(P.size)
# s = np.zeros(P.size)
# c = np.zeros(P.size)
for i in P.index:
    G[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics',
                                'T',T[i],'P',P[i],fluidname)
    Z[i] =  CP.CoolProp.PropsSI('Z','T',T[i],'P',P[i],fluidname)
    # h =  CP.CoolProp.PropsSI('H','T',T[i],'P',P[i],fluidname)
    # c[i] =  CP.CoolProp.PropsSI('SPEED_OF_SOUND','T',T[i],'P',P[i],fluidname)
    # u = c[i]*data.iloc[i,1] 
    # ht[i] = h + 0.5*u*u
    
# append new columns
shG =pd.DataFrame({'G':G,'Z':Z, })
newData = pd.concat([data, shG], join = 'outer', axis = 1)
# save newData in csv file
# newData.to_csv("m4sh.csv")
newData.to_csv("m6new.csv")
