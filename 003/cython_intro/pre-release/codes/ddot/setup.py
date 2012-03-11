from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

config = Configuration()

config.add_extension("ddot_cython", sources=["ddot_cython.c", "ddot_c.c"])

setup(**config.todict())
