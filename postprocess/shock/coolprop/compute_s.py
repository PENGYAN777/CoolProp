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

fluidname = "HEOS::MDM"
Tc =  CP.CoolProp.PropsSI("Tcrit",fluidname)
Pc =  CP.CoolProp.PropsSI("pcrit",fluidname)
dc =  CP.CoolProp.PropsSI("rhocrit",fluidname)
data = pd.read_csv("m4.csv", ",")
P = data.iloc[:,6] 
T = data.iloc[:,8] 
print("size", P.index)

G = np.zeros(P.size)
ht = np.zeros(P.size)
s = np.zeros(P.size)
c = np.zeros(P.size)
for i in P.index:
    G[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics',
                                'T',T[i],'P',P[i],fluidname)
    s[i] =  CP.CoolProp.PropsSI('S','T',T[i],'P',P[i],fluidname)
    h =  CP.CoolProp.PropsSI('H','T',T[i],'P',P[i],fluidname)
    c[i] =  CP.CoolProp.PropsSI('SPEED_OF_SOUND','T',T[i],'P',P[i],fluidname)
    u = c[i]*data.iloc[i,1] 
    ht[i] = h + 0.5*u*u
    
# append new columns
shG =pd.DataFrame({'sound': c, 'entropy': s, 'total enthalpt': ht, 'fundamental_derivative_of_gas_dynamics':G })
newData = pd.concat([data, shG], join = 'outer', axis = 1)
# save newData in csv file
# newData.to_csv("m4sh.csv")
newData.to_csv("m4new.csv")