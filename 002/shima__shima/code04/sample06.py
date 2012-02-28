#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Uring the property that if any non-finite values are in a column, the sum of
the columns becomes non-finite.
"""

import sys
import timeit
import numpy as np
import scipy as sp

# function to measure the execution time
def testfunc():
    # write your own code here ------------------------------------------------
    ans = arr[:, np.isfinite(np.sum(arr, axis=0))]
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
