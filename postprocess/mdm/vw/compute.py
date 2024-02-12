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
# data = pd.read_csv("pr.csv", ",")
# P = data.iloc[:,6] 
# T = data.iloc[:,8] 
# D = data.iloc[:,0] 
# print("size", P.index)

# G = np.zeros(P.size)
# # ht = np.zeros(P.size)
# # s = np.zeros(P.size)
# # c = np.zeros(P.size)
# for i in P.index:
#     G[i] = CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics',
#                                 'T',T[i],'P',P[i],fluidname)
#     # s[i] =  CP.CoolProp.PropsSI('S','T',T[i],'P',P[i],fluidname)
#     # h =  CP.CoolProp.PropsSI('H','T',T[i],'P',P[i],fluidname)
#     # c[i] =  CP.CoolProp.PropsSI('SPEED_OF_SOUND','T',T[i],'P',P[i],fluidname)
#     # u = c[i]*data.iloc[i,1] 
#     # ht[i] = h + 0.5*u*u
    
# # append new columns
# shG =pd.DataFrame({'G':G, })
# newData = pd.concat([data, shG], join = 'outer', axis = 1)
# # save newData in csv file
# # newData.to_csv("m4sh.csv")
# newData.to_csv("prnew.csv")

################# compute Gamma for van der wall model
import numpy as np
Tc =  CP.CoolProp.PropsSI("Tcrit",fluidname)
Pc =  CP.CoolProp.PropsSI("pcrit",fluidname)
dc =  CP.CoolProp.PropsSI("rhocrit",fluidname)
R = CP.CoolProp.PropsSI('GAS_CONSTANT',fluidname)
print("Universal gas constant:", R)
MW = CP.CoolProp.PropsSI('M',fluidname)
# print("molar mass:", MW)
Rs = R/MW
p = 0.931*Pc
t = 1.003*Tc
d = dc*0.446
g = 1.0125
a = 27*Rs*Rs*Tc*Tc/64/Pc
b = 1/8*Rs*Tc/Pc
# cv = CP.CoolProp.PropsSI('CVMASS','T', 1.01*Tc, 'P',Pc,  fluidname)
N = 120
v = 1/d
v0 = v*0.5
t0 = t*0.5
c = (1+2/N)*Rs*t*(v/(v-b))**2-2*a/v
s = Rs*np.log((v-b)/(v0-b)) + (Rs)/(g-1)*np.log(t/t0)

v1 = 0.57*v
d1 = 1/v1
# find t1 = t1(s,v1)
t2 = np.linspace(t*0.99,t*1.01,1000) 
t2 = pd.Series(t2)
s1 = np.zeros(t2.size) 
for i in t2.index:
    s1[i] = Rs*np.log((v1-b)/(v0-b)) + Rs/(g-1)*np.log(t2[i]/t0)
print("index:",np.argmin(abs(s1-s)))    
t1 = t2[np.argmin(abs(s1-s))]
c1 = (1+2/N)*Rs*t1*(v1/(v1-b))**2-2*a/v1
Gamma = 1 + d/c*(c1-c)/(d1-d)
print("Gamma:", Gamma)
