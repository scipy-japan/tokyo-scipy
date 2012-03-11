#!/usr/bin/python

import numpy as np
import ddot_cython as cyddot

N = 100000
x = np.random.randn(N)
y = np.random.randn(N)
z_npdot = np.dot(x, y)

test_funcs = {"cyddot.ddotp":cyddot.ddotp, "cyddot.ddot1":cyddot.ddot1,
              "cyddot.ddot2":cyddot.ddot2, "cyddot.ddot3":cyddot.ddot3,
              "cyddot.ddot4":cyddot.ddot4}

for (func_name, dot_func) in sorted(test_funcs.items()):
   z = dot_func(x, y)
   print func_name, np.allclose(z_npdot,  z)
