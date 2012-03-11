#!/usr/bin/python

import timeit

setup_string = """
import numpy as np
import matmult_cython as cymm

N = 100
M = 100
L = 100
x = np.random.randn(N, L)
y = np.random.randn(L, M)
"""

test_strings = ["np.dot(x, y)", "cymm.matmultp(x, y)", "cymm.matmult1(x, y)",
        "cymm.matmult2(x, y)", "cymm.matmult3(x, y)", "cymm.matmult4(x, y)"]

n_retry_default = 1000
for test_string in test_strings:
    n_retry = n_retry_default
    #if "matmultp" in test_string:
    #    n_retry = n_retry_default / 1000
    test_time = timeit.Timer(test_string, setup_string).timeit(n_retry)
    print "%20s used %12.5e s"%(test_string, test_time / n_retry )
