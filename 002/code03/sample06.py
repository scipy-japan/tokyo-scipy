#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Straightforward approach, but demand the same size of memory as the original
array
"""

import sys
import timeit
import numpy as np
import scipy as sp

# function to measure the execution time
def testfunc():
    # write your own code here ------------------------------------------------
    ans = np.sum(arr[np.isfinite(arr)])
    # -------------------------------------------------------------------------

    # return result
    return ans

# generate test data
SCALE = 1000
arr = np.random.randn(10 * SCALE)
arr[0 * SCALE:1 * SCALE] = np.nan
arr[1 * SCALE:2 * SCALE] = np.inf
arr[2 * SCALE:3 * SCALE] = -np.inf
print "correct = ", np.sum(arr[3 * SCALE:])
np.random.shuffle(arr)
print "answer = ", testfunc()

# check execution time
t = timeit.Timer("testfunc()", "from __main__ import testfunc")
print t.timeit(10000)
