from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

config = Configuration()

matmult_sources = ["matmult_c.c", "matmult_f.f90"]
config.add_library("matmult", sources=matmult_sources)
config.add_extension("matmult_cython", sources=["matmult_cython.c"],
        libraries=["matmult"], depends=matmult_sources) 
config.add_extension("matmult_f2py", sources=["matmult_f2py.pyf"],
        libraries=["matmult"], depends=matmult_sources) 

setup(**config.todict())
