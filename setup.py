from setuptools import setup
from setuptools import Extension

from Cython.Distutils import build_ext
from Cython.Build import cythonize

import os

NAME = "pywmm"
VERSION = "0.1"
DESCR = "Python module wrapping NOAA WMM C lib using Cython"
URL = "https://github.com/neogeo-technologies/pywmm"
REQUIRES = ['cython']
LICENSE='MIT'

AUTHOR = "Benjamin Chartier (Neogeo Technologies)"
EMAIL = "b.chartier@neogeo-technologies.fr"

SRC_DIR = "pywmm"
PACKAGES = [SRC_DIR]

EXT = Extension(
    "pywmm.pywmm",
    [os.path.join(SRC_DIR, "wmm_wrap.c"),
     os.path.join(SRC_DIR, "wmm", "GeomagnetismLibrary.c"),
     os.path.join(SRC_DIR, "pywmm.pyx")],
    libraries=[])

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=cythonize(EXT),
          package_data = {'pywmm': [os.path.join(SRC_DIR, "data", '*.COF')]},
          include_package_data=True
          )
