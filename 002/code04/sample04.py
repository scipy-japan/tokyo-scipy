#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Template for Code 4 @ Tokyo.Scipy #2
"""

import sys
import timeit
import numpy as np
import scipy as sp

# function to measure the execution time
def testfunc():
    # write your own code here ------------------------------------------------
    nans = np.logical_or(np.isnan(arr[0]), np.isnan(arr[1]))
    mask = np.tile(np.logical_not(nans), (2, 1))
    ans = arr[mask].reshape(2, 2)
    # -------------------------------------------------------------------------

    return ans

# generate test data
SCALE = 100
arr = np.empty((10 * SCALE, 10 * SCALE))
arr[:, :] = np.arange(10 * SCALE)
arr[range(0 * SCALE, 1 * SCALE), range(0 * SCALE, 1 * SCALE)] = np.nan
arr[range(1 * SCALE, 2 * SCALE), range(1 * SCALE, 2 * SCALE)] = np.inf
arr[range(2 * SCALE, 3 * SCALE), range(2 * SCALE, 3 * SCALE)] = -np.inf
idx = range(10 * SCALE)
np.random.shuffle(idx)
arr = arr[:, idx]

ans = testfunc()
print "answer shape = ", ans.shape
print "answer min = ", np.nanmin(ans)

# check execution time
t = timeit.Timer("testfunc()", "from __main__ import testfunc")
print t.timeit(100)
