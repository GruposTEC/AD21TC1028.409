#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:01:00 2021

@author: avmejia
"""

import math

entrada = input("Dame un numero : ")
entrada_numero = float(entrada)
print(entrada)
print(f'Lo que intrdujiste es el numero {entrada_numero *3}')

print(
    f'La raiz cuadrada de {entrada_numero:.2f} es {math.sqrt(entrada_numero)}')
