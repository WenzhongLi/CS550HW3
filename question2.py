#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: li
'''
import numpy as np

# nodeA, B, C, D, E, F, G, H
A = [[0, 1, 1, 1, 0, 0, 1, 0],
     [1, 0, 1, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 0],
     [1, 0, 0, 0, 1, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0]]

A = np.array(A)

D = [[4, 0, 0, 0, 0, 0, 0, 0],
     [0, 3, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 0, 0, 0, 0, 0],
     [0, 0, 0, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 0, 4, 0],
     [0, 0, 0, 0, 0, 0, 0, 1]]

D = np.array(D)

print(D-A)

L = D - A

en_value, en_vector = np.linalg.eigh(L)
print(en_value)
print(en_vector)


