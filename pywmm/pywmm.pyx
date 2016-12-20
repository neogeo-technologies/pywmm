cimport cython

cdef extern from "wmm/GeomagnetismHeader.h":
    # Data structure defined in GeomagnetismHeader.h used by the get_geomagnetics_elements function
    ctypedef struct MAGtype_GeoMagneticElements:
        double Decl
        double Incl
        double F
        double H
        double X
        double Y
        double Z
        double GV
        double Decldot
        double Incldot
        double Fdot
        double Hdot
        double Xdot
        double Ydot
        double Zdot
        double GVdot


cdef extern from "wmm_wrap.h":
    # Imports definitions from a c header file
    # Corresponding source file (cfunc.c) must be added to
    # the extension definition in setup.py for proper compiling & linking

    MAGtype_GeoMagneticElements _get_geomagnetics_elements "get_geomagnetics_elements"(double lon, double lat, double alt, double year, char* cof_file_name)


def get_geomagnetics_elements(lat, lon, alt, year=None, cof_file_path=None):
    # Exposes the get_geomagnetics_elements c function to python

    if year is None:
        from datetime import date
        year = date.today().year

    import os
    if cof_file_path is None:
        cof_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "WMM.COF")

    if not os.path.exists(cof_file_path):
        import errno
        raise IOError(errno.ENOENT, os.strerror(errno.ENOENT), cof_file_path)

    cdef double dlon = lon
    cdef double dlat = lat
    cdef double dalt = alt
    cdef double dyear = year
    cdef char* scof_file_path = cof_file_path

    # alt is the height above MSL / above geoid (not above ellipsoid)!
    # unit for alt: kilometer
    result = _get_geomagnetics_elements(dlon, dlat, dalt, dyear, scof_file_path)

    return result
