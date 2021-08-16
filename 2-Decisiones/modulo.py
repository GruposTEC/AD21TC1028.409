#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:28:44 2021

@author: avmejia
"""


print(f'En el archivo modulo.py __name__ tiene como valor  {__name__}')


def modulo():
    print("dentro del modulo")


if __name__ == "__main__":
    modulo()
