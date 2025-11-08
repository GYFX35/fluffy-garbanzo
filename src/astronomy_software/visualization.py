import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)

def plot_trajectory(positions, optimal_times=None, anomalies=None, title='Celestial Object Trajectory'):
    """
    Plots the trajectory of a celestial object.

    Args:
        positions (list): A list of the celestial object's positions.
        optimal_times (list, optional): A list of optimal observation times. Defaults to None.
        anomalies (list, optional): A list of detected anomalies. Defaults to None.
        title (str): The title of the plot.
    """
    fig, ax = plt.subplots()
    ra = [pos.ra.deg for pos in positions]
    dec = [pos.dec.deg for pos in positions]
    ax.plot(ra, dec, 'o-')

    if optimal_times:
        optimal_ra = [pos.ra.deg for pos in positions if pos.obstime in optimal_times]
        optimal_dec = [pos.dec.deg for pos in positions if pos.obstime in optimal_times]
        ax.plot(optimal_ra, optimal_dec, 'r*', markersize=15, label='Optimal Observation Time')
        ax.legend()

    plot_title = title
    if anomalies:
        plot_title += f"
Anomalies: {', '.join(anomalies)}"

    ax.set_xlabel('Right Ascension (deg)')
    ax.set_ylabel('Declination (deg)')
    ax.set_title(plot_title)
    ax.grid(True)
    plt.show()
