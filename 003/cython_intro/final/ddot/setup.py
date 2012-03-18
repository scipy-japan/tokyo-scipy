from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

config = Configuration()

ddot_sources = ["ddot_c.c", "ddot_f.f90"]
config.add_library("ddot", sources=ddot_sources)
config.add_extension("ddot_cython", sources=["ddot_cython.c"],
        libraries=["ddot"], depends=ddot_sources) 
config.add_extension("ddot_f2py", sources=["ddot_f2py.pyf"],
        libraries=["ddot"], depends=ddot_sources) 

setup(**config.todict())
