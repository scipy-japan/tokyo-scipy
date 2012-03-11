from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

config = Configuration()

config.add_extension("matmult_cython",
        sources=["matmult_cython.c", "matmult_c.c"],
        extra_compile_args=["-O3"])

setup(**config.todict())
