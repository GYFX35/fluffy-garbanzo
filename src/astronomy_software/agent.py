import numpy as np
from astropy.coordinates import AltAz

class AIAgent:
    """
    An AI agent for analyzing celestial object trajectories.
    """

    def identify_optimal_observation_times(self, positions, location):
        """
        Identifies the best times to observe a celestial object based on its altitude.

        Args:
            positions (list): A list of the celestial object's positions.
            location (astropy.coordinates.EarthLocation): The location of the observer.

        Returns:
            list: A list of optimal observation times.
        """
        altitudes = [pos.transform_to(AltAz(obstime=pos.obstime, location=location)).alt.deg for pos in positions]
        max_altitude = np.max(altitudes)
        optimal_times = [positions[i].obstime for i, alt in enumerate(altitudes) if alt == max_altitude]
        return optimal_times

    def detect_anomalies(self, positions):
        """
        Detects anomalies in the trajectory of a celestial object.

        Args:
            positions (list): A list of the celestial object's positions.

        Returns:
            list: A list of detected anomalies.
        """
        anomalies = []
        if len(positions) > 2:
            time_diffs = np.diff([p.obstime.jd for p in positions])
            median_time_diff = np.median(time_diffs)
            for i, diff in enumerate(time_diffs):
                if diff > 10 * median_time_diff:
                    anomalies.append(f"Large time gap detected at index {i}")
        return anomalies
