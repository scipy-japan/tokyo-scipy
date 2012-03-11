#!/usr/bin/python

import timeit

setup_string = """
import numpy as np
import ddot_cython as cyddot

N = 100000
x = np.random.randn(N)
y = np.random.randn(N)
"""

test_strings = ["np.dot(x, y)", "cyddot.ddotp(x, y)", "cyddot.ddot1(x, y)",
    "cyddot.ddot2(x, y)", "cyddot.ddot3(x, y)", "cyddot.ddot4(x, y)"]

n_retry_default = 1000
for test_string in sorted(test_strings):
    n_retry = n_retry_default
    if "ddotp" in test_string:
        n_retry = n_retry_default / 1000
    test_time = timeit.Timer(test_string, setup_string).timeit(n_retry)
    print "%20s used %12.5e s"%(test_string, test_time / n_retry )
