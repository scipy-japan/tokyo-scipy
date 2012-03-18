from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

config = Configuration()
config.add_extension("cython_struct", 
           sources=["cython_struct.c","struct_test.c"])

setup(**config.todict())
