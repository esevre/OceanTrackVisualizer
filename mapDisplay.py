#
#  Display the Basemap, and draw data on it
#
#

#
#  mpl_toolkits.basemap provides mapping tools for projecting points on a map
#
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
#
# this will be used for plotting line segments with colormap based colors
#
from matplotlib.collections import LineCollection

#
#  Erik's custom function headers
#
import processFile as pf
import dataComputation as dc

#
#
#
def generate_plotable_data(filename : str):
    header, data = pf.get_data_from_tab_separated_file(filename)
    x = np.array([x for x, y, age in data])
    y = np.array([y for x, y, age in data])

    # note: may want to move data to corrected line in a different function ... something to consider
    # Correct data to fit on line
    x, y = dc.map_xy_to_line(x, y)

    ages = np.array([age for x, y, age in data])
    pts = []

    for i in range(len(x)):
        pts.append(dc.point(x[i], y[i]))

    spreading_rates = dc.generate_spreading_rates(ages, pts)
    return x, y, ages, spreading_rates


#
#  todo: write plot_track_line_with_correction function
#
def plot_track_line_with_correction_from_tab_file(filename : str):
    pass

#
#  todo: write plot_single_track_from_tab_file function
#
def plot_single_track_from_tab_file(filename : str):
    pass

#
#  todo: write plot_single_track_from_csv_file function
#
def plot_single_track_from_csv_file(filename : str):
    pass


#
#  todo: write plot_tracks_from_tab_files function
#
def plot_tracks_from_tab_files(filename : str):
    pass


#
#  todo: write plot_tracks_from_csv_files function
#
def plot_tracks_from_csv_files(filename : str):
    pass






