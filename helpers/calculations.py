import threading

from sgp4.api import Satrec
from sgp4.api import SGP4_ERRORS
from sgp4.api import jday

from datetime import datetime as dt

from astropy.time import Time
from astropy.coordinates import TEME, CartesianDifferential, CartesianRepresentation
from astropy import units as u
from astropy.coordinates import ITRS

def get_julian_date():
    day = dt.utcnow()
    tuple_date = (day.year,day.month,day.day,day.hour,day.minute,day.second)
    jd, fr = jday(*tuple_date)
    jd, fr = jday(*tuple_date)
    jd = int(jd)

    return jd+fr

def get_satellite_geo_position(tle_1, tle_2):
    satellite = Satrec.twoline2rv(tle_1, tle_2)

    t = Time(get_julian_date(), format='jd')
    error_code, teme_p, teme_v = satellite.sgp4(t.jd1, t.jd2)  # in km and km/s
    if error_code != 0:
        raise RuntimeError(SGP4_ERRORS[error_code])
        
    teme_p = CartesianRepresentation(teme_p*u.km)
    teme_v = CartesianDifferential(teme_v*u.km/u.s)
    teme = TEME(teme_p.with_differentials(teme_v), obstime=t)

    itrs = teme.transform_to(ITRS(obstime=t))
    location = itrs.earth_location
    geo_pos = location.geodetic
    return geo_pos.lat.value, geo_pos.lon.value, geo_pos.height.value
