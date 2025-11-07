import pytest
from astropy.time import Time, TimeDelta
from astropy.coordinates import EarthLocation, SkyCoord
from astronomy_software.celestial import track_object

def test_track_object():
    """
    Tests the track_object function.
    """
    start_time = Time('2024-01-01T00:00:00')
    end_time = Time('2024-01-01T01:00:00')
    step_size = TimeDelta(3600, format='sec')
    location = EarthLocation(lat='34.0522', lon='-118.2437', height=0)

    positions = track_object('sun', start_time, end_time, step_size, location)

    assert isinstance(positions, list)
    assert all(isinstance(p, SkyCoord) for p in positions)
