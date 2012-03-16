#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple implementation of L1-compressed sensing using openopt.LP with
FuncDesigner
"""

# Module metadata variables ---------------------------------------------------

__author__ = "Toshihiro Kamishima ( http://www.kamishima.net/ )"
__date__ = "2012/03/16"
__version__ = "1.0.0"
__copyright__ = "Copyright (c) 2012 Toshihiro Kamishima all rights reserved."
__license__ = "MIT License: http://www.opensource.org/licenses/mit-license.php"
__docformat__ = "restructuredtext en"

# Public symbols --------------------------------------------------------------

__all__ = ['compressed_sensing2']

# Imports ---------------------------------------------------------------------

import sys
import numpy as np
from openopt import LP
import FuncDesigner as fd
from compressed_sensing import *

# Functions -------------------------------------------------------------------

def compressed_sensing2(x1, trans):
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

    # define variable
    t = fd.oovar('t', size=n_inputs)
    x = fd.oovar('x', size=n_inputs)

    # objective to minimize: f x^T -> min
    objective = fd.sum(t)

    # init constraints
    constraints = []

    # equality constraint: a_eq x^T = b_eq
    constraints.append(fd.dot(trans, x) == x1)

    # inequality constraint: -t < x < t
    constraints.append(-t <= x)
    constraints.append(x <= t)

    # start_point
    start_point = {x:np.zeros(n_inputs), t:np.zeros(n_inputs)}

    # solve linear programming
    prob = LP(objective, start_point, constraints=constraints)
    result = prob.minimize('pclp') # glpk, lpSolve... if available

    # print result
#    print "x =", result.xf # arguments at mimimum
#    print "objective =", result.ff # value of objective

    return result.xf[x]

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
    hat1_x0 = compressed_sensing(x1, a)
    hat2_x0 = compressed_sensing2(x1, a)
    print "orig_x0 = [ %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f ]" % tuple(x0)
    print "est1_x0 = [ %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f ]" % tuple(hat1_x0)
    print "est2_x0 = [ %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f %8.5f ]" % tuple(hat2_x0)
    candes_tao = float(n_sparse) * np.log(n_inputs / float(n_sparse))
    print "condition: if O(", candes_tao, ") <", n_outputs
