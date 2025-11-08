import pytest
import numpy as np
from astropy.time import Time
from astropy.coordinates import EarthLocation, SkyCoord
import astropy.units as u
from src.astronomy_software.agent import AIAgent

@pytest.fixture
def sample_positions():
    """
    Provides a sample list of SkyCoord objects for testing.
    """
    location = EarthLocation(lat=34.0522 * u.deg, lon=-118.2437 * u.deg, height=71 * u.m)
    times = Time('2023-01-01T00:00:00') + np.arange(0, 10, 2) * u.hour
    positions = [
        SkyCoord(ra=10*u.deg, dec=20*u.deg, frame='icrs', obstime=times[0], location=location),
        SkyCoord(ra=12*u.deg, dec=22*u.deg, frame='icrs', obstime=times[1], location=location),
        SkyCoord(ra=15*u.deg, dec=25*u.deg, frame='icrs', obstime=times[2], location=location),
        SkyCoord(ra=18*u.deg, dec=28*u.deg, frame='icrs', obstime=times[3], location=location),
        SkyCoord(ra=22*u.deg, dec=32*u.deg, frame='icrs', obstime=times[4], location=location),
    ]
    return positions

def test_identify_optimal_observation_times(sample_positions):
    """
    Tests the identify_optimal_observation_times method of the AIAgent.
    """
    agent = AIAgent()
    location = EarthLocation(lat=34.0522 * u.deg, lon=-118.2437 * u.deg, height=71 * u.m)
    optimal_times = agent.identify_optimal_observation_times(sample_positions, location)
    assert len(optimal_times) > 0

def test_detect_anomalies(sample_positions):
    """
    Tests the detect_anomalies method of the AIAgent.
    """
    agent = AIAgent()
    anomalies = agent.detect_anomalies(sample_positions)
    assert len(anomalies) == 0

    # Add a position with a large time gap to create an anomaly
    anomalous_positions = sample_positions.copy()
    anomalous_positions.append(
        SkyCoord(ra=30*u.deg, dec=40*u.deg, frame='icrs', obstime=sample_positions[-1].obstime + 1 * u.day)
    )
    anomalies = agent.detect_anomalies(anomalous_positions)
    assert len(anomalies) > 0
