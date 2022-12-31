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

fluidname = "MM"
data = pd.read_csv("m4.csv", ",")
# get P,T from 2nd and 3rd column 
P = data.iloc[:,1] 
T = data.iloc[:,2] 
print("size", P.index)

ht = np.zeros(P.size)
s = np.zeros(P.size)
for i in P.index:
    s[i] =  CP.CoolProp.PropsSI('S','T',T[i],'P',P[i],fluidname)
    h =  CP.CoolProp.PropsSI('H','T',T[i],'P',P[i],fluidname)
    c =  CP.CoolProp.PropsSI('SPEED_OF_SOUND','T',T[i],'P',P[i],fluidname)
    u = c*data.iloc[i,0] 
    ht[i] = h + 0.5*u*u
    
# append new columns
sh =pd.DataFrame({'entropy': s, 'total enthalpt': ht })
newData = pd.concat([data, sh], join = 'outer', axis = 1)

# save newData in csv file
newData.to_csv("m4s.csv")
