#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:33:21 2021

@author: avmejia
"""

var_global = 5
"""
PONER ALGORITMO
"""

def mayor2(x , y):
    """
    Funcion que saca el mayor de dos numeros enteros

    Parameters
    ----------
    x : int
        Primer numero.
    y : int
        Segundo numero.

    Returns
    -------
    temp : int
        el mayor de los números que llegaron.

    """
    global var_global
    
    var_global = 3
    temp = 0;
    if x > y :
        temp = x
    else:
        temp = y
    
    x = x + 1
    y = y + 1
    
    return temp  
    
primera = 10;
segunda = 5

mayor = mayor2(primera,segunda)

print(mayor)