#cython: boundscheck=False

import numpy as np
cimport numpy as np
cimport cython

DOUBLE = np.float64
ctypedef np.float64_t DOUBLE_t 

def ddotp(a, b):
    """Pure Python implementation. Very slow"""
    len_a = len(a)
    dot_value = 0
    for i in xrange(len_a):
        dot_value += a[i] * b[i]
    return dot_value

def ddot1(np.ndarray[DOUBLE_t, ndim=1] a, np.ndarray[DOUBLE_t, ndim=1] b):
    """Cythonized version with static typing
    This is about 500 times faster than ddotp
    """
    cdef int i, len_a
    cdef double dot_value = 0.0
    len_a = len(a)
    for i in xrange(len_a):
        dot_value += a[i] * b[i]
    return dot_value

@cython.wraparound(False)
def ddot2(np.ndarray[DOUBLE_t, ndim=1] a, np.ndarray[DOUBLE_t, ndim=1] b):
    """Modified version of ddot1 with special decorator
    wraparound(False) disables relative indexing of python and improves speed
    This is about 2 times faster than ddot2
    """
    cdef int i, len_a
    cdef double dot_value = 0.0
    len_a = len(a)
    for i in xrange(len_a):
        dot_value += a[i] * b[i]
    return dot_value

cdef double ddot_intrn(double *a, double *b, int len_a):
    """Internal C-like function
    This can be completely converted to Native C code with no python overhead
    """
    cdef int i
    cdef double dot_value = 0.0
    for i in xrange(len_a):
        dot_value += a[i] * b[i]
    return dot_value

def ddot3(np.ndarray[DOUBLE_t, ndim=1] a, np.ndarray[DOUBLE_t, ndim=1] b):
    """A wrapper function to ddot_intrn. This will be actually called by the
    Python interpreter. It is only slightly faster than ddot2 and as fast as
    the np.dot.
    """
    cdef int i, len_a
    cdef double dot_value = 0.0
    len_a = len(a)
    return ddot_intrn(<double *>a.data, <double *>b.data, len_a)

# import external C implementation
cdef extern from "ddot_c.h":
    double ddot_c(double *a, double *b, int len_a)

def ddot4(np.ndarray[DOUBLE_t, ndim=1] a, np.ndarray[DOUBLE_t, ndim=1] b):
    """ A wapper function for external ddot_c. This will be actually called by
    the Python interpreter. It is only slightly faster than ddot2 and as fast
    as the np.dot.
    """
    cdef int i, len_a
    cdef double dot_value = 0.0
    len_a = len(a)
    return ddot_c(<double *>a.data, <double *>b.data, len_a)

# import external Fortran implementation
cdef extern from "ddot_c.h":
    double ddot_f(double *a, double *b, int len_a)
    void ddot_f_(double *a, double *b, int *len, double *dot_value)

def ddot5(np.ndarray[DOUBLE_t, ndim=1] a, np.ndarray[DOUBLE_t, ndim=1] b):
    """ A direct wapper function for external ddot_f_. This will be actually
    called by the Python interpreter. It is only slightly faster than ddot2
    and as fast as the np.dot.
    """
    cdef int i, len_a
    cdef double dot_value = 0.0
    len_a = len(a)
    ddot_f_(<double *>a.data, <double *>b.data, &len_a, &dot_value)
    return dot_value

def ddot6(np.ndarray[DOUBLE_t, ndim=1] a, np.ndarray[DOUBLE_t, ndim=1] b):
    """ A wapper function for external ddot_f. This will be actually called by
    the Python interpreter. It is only slightly faster than ddot2 and as fast
    as the np.dot.
    """
    cdef int i, len_a
    cdef double dot_value = 0.0
    len_a = len(a)
    return ddot_f(<double *>a.data, <double *>b.data, len_a)
