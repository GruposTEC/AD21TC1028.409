#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:05:24 2021

@author: avmejia
"""

#No se cuantas veces se va repetir
#depende de un evento externo
i = "0"
while(i != "5"):
    i = input("dame un número : ")
    print(f"Hola {i}")
 
    
#Se cuantas veces se va a repetir 
i = 0     
while(True):
    i = i + 1
    print(f"Hola {i}")
    if i > 100:  
        break;

i = 0     
while(i < 100):
    i = i + 1
    print(f"Hola {i}")
    