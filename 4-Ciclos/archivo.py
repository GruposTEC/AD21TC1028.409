#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:43:10 2021

@author: avmejia
"""

# print(f.readlines())

f = open("lista.csv", "r")

for alumno in f:
    print(alumno)
    if alumno == "Matricula;Correo\n":
        print("Es igual")
    else:
        print("No es igual")
f.close()
