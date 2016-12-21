# pywmm
Python module wrapping NOAA WMM C lib using Cython

## License
Public domain - since its source code comes mainly from https://www.ngdc.noaa.gov/geomag/WMM/DoDWMM.shtml
(which is in public domain):
- pywmm/data/WMM.COF
- pywmm/wmm/EGM9615.h
- pywmm/wmm/GeomagnetismHeader.h
- GeomagnetismLibrary.c

## Requirements
- Cython (see http://cython.readthedocs.io/en/latest/src/quickstart/install.html)
- a C compiler (gcc, msvc...)

## Installation
### Compilation and installation on MacOs :
```
$ cd your/local/dir
$ git clone https://github.com/neogeo-technologies/pywmm.git
$ cd pywmm
$ python setup.py install
```
You may need to sudo the last line.

###Compilation and installation on Windows :
```
$ cd your/local/dir
$ git clone https://github.com/neogeo-technologies/pywmm.git
$ cd pywmm/pywmm
$ cython -a pywmm.pyx
$ python setup.py install
```
On windows you may need to use the Microsoft Visual C++ compiler for Python command prompt tool.
See https://github.com/cython/cython/wiki/CythonExtensionsOnWindows for details.


## Usage
```
$ python
>>> import pywmm
>>> pywmm.get_geomagnetics_elements(80,0,0)
{'Decl': -3.411333428128801, 'GV': -3.411333428128801, 'Zdot': 10.7609431335789,
'Ydot': 51.48795302969407, 'GVdot': 0.4386276610626788, 'F': 54844.200805169676,
'H': 6627.667373902938, 'Xdot': -11.068757776171879, 'Incldot': 0.015994219459516176,
'Hdot': -14.112875190451874, 'Decldot': 0.4386276610626788, 'Fdot': 8.976604358017473,
'Y': -394.3715919103892, 'X': 6615.923659368474, 'Z': 54442.26655034374,
'Incl': 83.05910660208956}
```

Test values for the 2015 WMM.COF file are available there:
https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2015/WMM2015testvalues.pdf
(with altitudes relative to ellipsoid not geoid)
