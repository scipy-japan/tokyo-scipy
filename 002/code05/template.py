#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Template for Code 5 @ Tokyo.Scipy #2
"""

import sys
import timeit
import numpy as np
import scipy as sp

F = 500 # the size of the domain of the feature
N = 10000 # the number of samples

# reference function
def reference():
    ans = np.zeros((N, F))
    ans[np.arange(N, dtype=np.int), arr] = 1

    return ans

# function to measure the execution time
def testfunc():
    # write your own code here ------------------------------------------------
    ans = np.zeros((N, F))
    ans[np.arange(N, dtype=np.int), arr] = 1
    # -------------------------------------------------------------------------

    return ans

# generate test data
arr = np.arange(N, dtype=np.int) % F

print "check = ", np.all(reference() == testfunc())

# check execution time
t = timeit.Timer("testfunc()", "from __main__ import testfunc")
print t.timeit(100)
