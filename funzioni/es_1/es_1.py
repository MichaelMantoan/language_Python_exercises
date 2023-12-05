#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Leggere in input da tastiera due numeri maggiori di 0 e farne la somma.


def somma(n1, n2):
    return n1 + n2


while True:
    n1 = int(input("Inserire il primo numero (maggiore o uguale a 0): "))
    n2 = int(input("Inserire il secondo numero (maggiore o uguale a 0): "))
    if n1 > 0 and n2 > 0:
        break
    else:
        print("Inserire numeri maggiori o uguali a 0")

print("%d + %d = %d" % (n1, n2, somma(n1, n2)))
