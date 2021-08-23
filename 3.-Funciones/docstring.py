#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 08:44:35 2021

@author: avmejia
"""
"""
Las 2 lineas del algoritmo

"""

def punto_cartesiano(x , y ):
    """
    Este es el metodo para demostrar docstrings

    Parameters
    ----------
    x : int
        La coordena x del punto.
    y : int
        La coordena y del punto.

    Returns
    -------
    x : int
        La suma de la coordenada x más la coordenada y.

    """
    x = x + y
    return x


def main():
    '''
    

    Returns
    -------
    None.

    '''
    x = "Hola "
    y = "Mundo"
    print(x,y)

    print(f'{x}{y}')
    
    x= int(input("Dame x "))
    y= int(input("Dame y "))
    
    suma = punto_cartesiano(x, y)
    
    print(suma)

main()

