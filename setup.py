from setuptools import setup
from setuptools import Extension

from Cython.Distutils import build_ext
from Cython.Build import cythonize

NAME = "pywmm"
VERSION = "0.1"
DESCR = "Python module wrapping NOAA WMM C lib using Cython"
URL = "https://github.com/neogeo-technologies/pywmm"
REQUIRES = ['cython']
LICENSE='public domain'

AUTHOR = "Benjamin Chartier (Neogeo Technologies)"
EMAIL = "b.chartier@neogeo-technologies.fr"

KEYWORDS = ["magnetic", "variation", "declination"]
CLASSIFIERS = [
    "Programming Language :: Python",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering :: GIS",
    "Topic :: Utilities"
    ]

SRC_DIR = "pywmm"
PACKAGES = [SRC_DIR]

EXT = Extension(
    "pywmm.pywmm",
    [SRC_DIR + "/wmm_wrap.c",
     SRC_DIR +  "/wmm/GeomagnetismLibrary.c",
     SRC_DIR + "/pywmm.pyx"],
    libraries=[])

if __name__ == "__main__":
    setup(
        install_requires=REQUIRES,
        packages=PACKAGES,
        zip_safe=False,
        name=NAME,
        version=VERSION,
        description=DESCR,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        cmdclass={"build_ext": build_ext},
        ext_modules=cythonize(EXT),
        package_data = {'pywmm': [SRC_DIR + "/data/*.COF"]},
        include_package_data=True
        )
