#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple implementation of L1-compressed sensing using openopt.LP
"""

# Module metadata variables ---------------------------------------------------

__author__ = "Toshihiro Kamishima ( http://www.kamishima.net/ )"
__date__ = "2012/03/15"
__version__ = "1.0.0"
__copyright__ = "Copyright (c) 2012 Toshihiro Kamishima all rights reserved."
__license__ = "MIT License: http://www.opensource.org/licenses/mit-license.php"
__docformat__ = "restructuredtext en"

# Public symbols --------------------------------------------------------------

__all__ = ['compressed_sensing']

# Imports ---------------------------------------------------------------------

import sys
import numpy as np
from openopt import LP

# Functions -------------------------------------------------------------------

def compressed_sensing(x1, trans):
    """L1 compressed sensing
    
    :Parameters:
        x1 : array-like, shape=(n_outputs,)
            input sparse vector
        trans : array-like, shape=(n_outputs, n_inputs)
            transformation matrix
    :Returns:
        decoded vector, shape=(n_inpus,)
    :RType:
        array-like
    """

    # obrain sizes of inputs and outputs
    (n_outputs, n_inputs) = trans.shape

    # objective to minimize: f x^T -> min
    f = np.zeros((n_inputs * 2), dtype=np.float)
    f[n_inputs:2 * n_inputs] = 1.0

    # constraint: a x^T == b
    a_eq = np.zeros((n_outputs, 2 * n_inputs), dtype=np.float)
    a_eq[:, 0:n_inputs] = trans

    b_eq = x1

    # constraint: -t <= x <= t
    a = np.zeros((2 * n_inputs, 2 * n_inputs), dtype=np.float)
    for i in xrange(n_inputs):
        a[i, i] = -1.0
        a[i, n_inputs + i] = -1.0
        a[n_inputs + i, i] = 1.0
        a[n_inputs + i, n_inputs + i] = -1.0

    b = np.zeros(n_inputs * 2)

    # solve linear programming
    prob = LP(f, Aeq=a_eq, beq=b_eq, A=a, b=b)
    result = prob.minimize('pclp') # glpk, lpSolve... if available

    # print result
#    print "x =", result.xf # arguments at mimimum
#    print "objective =", result.ff # value of objective

    return result.xf[0:n_inputs]

# Main routine ----------------------------------------------------------------

if __name__ == '__main__':

    """ try to change the number of observations
    under the condition n_inputs=5 and n_sparse=2
    almost always fails if n_outpus=2, 
    so so if n_outputs=3, 
    almost perfectly works if n_oupts=4
    """
    n_outputs = 5

    x0 = np.array([0, 1, 0, 1, 0, 0, 0], dtype=np.float) # hidden input vector
    n_inputs = 7 # change accordingly
    n_sparse = 2 # change accordingly

    # random transformation matrix following normal distribution
    a = np.random.randn(n_outputs, n_inputs)
    print "A =\n", a

    # observed vector
    x1 = np.dot(a, x0)
    print "x1 =\n", x1

    # decode input vector
    hat_x0 = compressed_sensing(x1, a)
    print "org_x0 = [ %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f ]" % tuple(x0)
    print "est_x0 = [ %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f %5.2f ]" % tuple(hat_x0)
    candes_tao = float(n_sparse) * np.log(n_inputs / float(n_sparse))
    print "condition: if O(", candes_tao, ") <", n_outputs
