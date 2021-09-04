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
    alumno = alumno[:len(alumno)-1]
    print(alumno)


f.close()
