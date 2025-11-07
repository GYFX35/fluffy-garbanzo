import numpy as np
from astropy.coordinates import get_body, EarthLocation
from astropy.time import Time

class CelestialObject:
    """
    Represents a celestial object and provides methods to calculate its position.
    """

    def __init__(self, name):
        """
        Initializes a CelestialObject with a given name.

        Args:
            name (str): The name of the celestial object (e.g., 'sun', 'moon', 'mars').
        """
        self.name = name

    def get_position(self, time, location):
        """
        Calculates the position of the celestial object at a given time and location.

        Args:
            time (astropy.time.Time): The time of observation.
            location (astropy.coordinates.EarthLocation): The location of the observer.

        Returns:
            astropy.coordinates.SkyCoord: The coordinates of the celestial object.
        """
        return get_body(self.name, time, location)

def track_object(object_name, start_time, end_time, step_size, location):
    """
    Tracks the movement of a celestial object over a given time range.

    Args:
        object_name (str): The name of the celestial object to track.
        start_time (astropy.time.Time): The start time of the tracking period.
        end_time (astropy.time.Time): The end time of the tracking period.
        step_size (astropy.time.TimeDelta): The time step for tracking.
        location (astropy.coordinates.EarthLocation): The location of the observer.

    Returns:
        list: A list of the celestial object's positions at each time step.
    """
    celestial_object = CelestialObject(object_name)
    times = start_time + np.arange(0, (end_time - start_time).sec, step_size.sec) * step_size
    positions = [celestial_object.get_position(t, location) for t in times]
    return positions
