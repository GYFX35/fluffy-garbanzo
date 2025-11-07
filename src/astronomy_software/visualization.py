import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

plt.style.use(astropy_mpl_style)

def plot_trajectory(positions, title='Celestial Object Trajectory'):
    """
    Plots the trajectory of a celestial object.

    Args:
        positions (list): A list of the celestial object's positions.
        title (str): The title of the plot.
    """
    fig, ax = plt.subplots()
    ra = [pos.ra.deg for pos in positions]
    dec = [pos.dec.deg for pos in positions]
    ax.plot(ra, dec, 'o-')
    ax.set_xlabel('Right Ascension (deg)')
    ax.set_ylabel('Declination (deg)')
    ax.set_title(title)
    ax.grid(True)
    plt.show()
