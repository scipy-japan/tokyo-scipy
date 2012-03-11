import numpy as np
cimport numpy as np
cimport cython

DOUBLE = np.float64
ctypedef np.float64_t DOUBLE_t 


def matmultp(a, b):
    """Pure Python implementation. Very slow"""
    n, l = a.shape
    m = len(b[0])
    c = np.zeros((n, m))
    for i in xrange(n):
        for j in xrange(m):
            c[i, j] = 0.0
            for k in xrange(l):
                c[i, j] += a[i, k] * b[k, j]
    return c


def matmult1(np.ndarray[DOUBLE_t, ndim=2] a, np.ndarray[DOUBLE_t, ndim=2] b):
    """Cythonized version with static typing
    """
    cdef int i, j, k
    cdef int n, m, l
    cdef np.ndarray[DOUBLE_t, ndim=2] c
    n = len(a)
    l = len(a[0])
    m = len(b[0])
    c = np.zeros((n, m))
    for i in xrange(n):
        for j in xrange(m):
            c[i, j] = 0.0
            for k in xrange(l):
                c[i, j] += a[i, k] * b[k, j]
    return c


@cython.wraparound(False)
def matmult2(np.ndarray[DOUBLE_t, ndim=2] a, np.ndarray[DOUBLE_t, ndim=2] b):
    """Cythonized version with static typing and directive
    """
    cdef int i, j, k
    cdef int n, m, l
    cdef np.ndarray[DOUBLE_t, ndim=2] c
    n = len(a)
    l = len(a[0])
    m = len(b[0])
    c = np.zeros((n, m))
    for i in xrange(n):
        for j in xrange(m):
            c[i, j] = 0.0
            for k in xrange(l):
                c[i, j] += a[i, k] * b[k, j]
    return c

cdef void matmult_intrn(int n, int m, int l,
        double *a, double *b, double *c):
    """Internal C-like function
    This can be completely converted to Native C code with no python overhead
    """
    cdef int i, j, k
    for i in xrange(n):
        for j in xrange(m):
            c[i*m + j] = 0.0
            for k in xrange(l):
                c[i*m + j] += a[i*l + k] * b[k*m + j]


def matmult3(np.ndarray[DOUBLE_t, ndim=2] a, np.ndarray[DOUBLE_t, ndim=2] b):
    """A wrapper function to matmult_intrn. This will be actually called by the
    Python interpreter.
    """
    cdef int n, m, l
    cdef np.ndarray[DOUBLE_t, ndim=2] c
    n = len(a)
    l = len(a[0])
    m = len(b[0])
    c = np.zeros((n, m))
    matmult_intrn(n, m, l, <double*>a.data, <double*>b.data, <double*>c.data)
    return c

# import external C implementation
cdef extern from "matmult_c.h":
   void matmult_c(int n, int m, int l, double *a, double *b, double *c)


def matmult4(np.ndarray[DOUBLE_t, ndim=2] a, np.ndarray[DOUBLE_t, ndim=2] b):
    """ A wapper function for external matmult_c.
    """
    cdef int n, m, l
    cdef np.ndarray[DOUBLE_t, ndim=2] c
    n = len(a)
    l = len(a[0])
    m = len(b[0])
    c = np.zeros((n, m))
    matmult_c(n, m, l, <double*>a.data, <double*>b.data, <double*>c.data)
    return c

