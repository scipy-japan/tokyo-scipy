#!/usr/bin/python

import numpy as np
import matmult_cython as cymm

N = 100
M = 50
L = 30
x = np.empty((N, L))
y = np.empty((L, M))
x[:, :] = np.random.randn(N, L)
y[:, :] = np.random.randn(L, M)
z_npdot = np.dot(x, y)

test_funcs = {"cymm.matmultp":cymm.matmultp,
              "cymm.matmult1":cymm.matmult1,
              "cymm.matmult2":cymm.matmult2,
              "cymm.matmult3":cymm.matmult3,
              "cymm.matmult4":cymm.matmult4}

for (func_name, dot_func) in sorted(test_funcs.items()):
   z = dot_func(x, y)
   print func_name, np.allclose(z_npdot,  z)
