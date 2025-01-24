# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:15:10 2025

@author: PC
"""

number=input()

bgh=int(number)%4

if int(bgh)==0:
 p=int(number)/4
 print(-(int(p)) ,int(p))
 
elif int(bgh)==2:
 p=int(number)/4
 p=p+1
 print(int(p) ,-(int(p)-1))
elif int(bgh)==1:
 p=int(number)/4
 print(-(int(p)) ,-(int(p)))
elif int(bgh)==3:
 p=int(number)/4
 print(int(p)+1 ,int(p)+1)