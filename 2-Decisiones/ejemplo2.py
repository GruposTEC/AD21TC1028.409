#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    moneda1 = int(input("Dame moneda 1"))
    moneda2 = 5
    moneda3 = 20
    if moneda1 < moneda2:
        moneda1 = moneda1
    else:
        moneda2 = moneda1
    if moneda1 < moneda3:
        moneda1 = moneda1
    else:
        moneda1 = moneda3
    print(moneda1)


if __name__ == "__main__":
    main()
