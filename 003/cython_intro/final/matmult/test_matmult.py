#!/usr/bin/python

import timeit

import numpy as np
import matmult_cython as cymm
import matmult_f2py as fpmm

def getOrder(x):
    if x.flags.carray :
        return "C"
    elif x.flags.farray :
        return "F"
    else :
        return "unkown"

N = 100
M = 50
L = 30
order = "C"
x = np.empty((N, L), order=order)
y = np.empty((L, M), order=order)
x[:, :] = np.random.randn(N, L)
y[:, :] = np.random.randn(L, M)
z_npdot = np.dot(x, y)
print "order of z_npdot = %s" % getOrder(z_npdot)

test_funcs = {"cymm.matmultp":cymm.matmultp,
              "cymm.matmult1":cymm.matmult1,
              "cymm.matmult2":cymm.matmult2,
              "cymm.matmult3":cymm.matmult3,
              "cymm.matmult4":cymm.matmult4,
              "cymm.matmult5":cymm.matmult5,
              "cymm.matmult6":cymm.matmult6,
              "fpmm.matmult_f":fpmm.matmult_f,
              "fpmm.matmult_c":fpmm.matmult_c}

for (func_name, dot_func) in sorted(test_funcs.items()):
   z = dot_func(x, y)
   print func_name, np.allclose(z_npdot,  z), getOrder(z)
