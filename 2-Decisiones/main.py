#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 21:00:56 2021

@author: avmejia
"""

import modulo

print(f'En el archivo main.py __name__ tiene como valor  {__name__}')
print(type(__name__))


def main():
    print("dentro del metodo main")


if __name__ == "__main__":
    main()
