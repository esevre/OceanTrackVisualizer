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
from colormap import ColorMap, get_blue_green_red_colormap


def plot_track_line_with_correction_from_tab_file(filename : str, title : str = 'Corrected Track Line'):
    """
    Plot the track line and the corrected track line showing
    the error between the two, and the data used for the computation.

    :param filename: containing tab seperated data
    :param title: display title for the plot
    """

    x_old, y_old, ages, spreading_rates = dc.generate_plotable_data(filename)
    x, y = dc.map_xy_to_line(x_old, y_old)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    xavg = (xmax-xmin)/2.0
    yavg = (ymax-ymin)/2.0
    x_buffer = (xmax-xmin) / 10.0
    y_buffer = (ymax-ymin) / 10.0
    xmin -= x_buffer
    xmax += x_buffer
    ymin -= y_buffer
    ymax += y_buffer

    # Generate a basemap for the desired region
    m = Basemap(projection='merc', llcrnrlat=ymin, urcrnrlat=ymax,
                llcrnrlon=xmin, urcrnrlon=xmax, lat_ts=yavg, resolution='h')
    m.etopo(scale=2.0)
    m.drawcoastlines()

    # draw parallels and meridians.
    m.drawparallels(np.arange(ymin, ymax, 1.0))
    m.drawmeridians(np.arange(xmin, xmax, 1.0))

    x, y, = m(x,y)
    x_old, y_old = m(x_old, y_old)

    for i in range(len(x)):
        xs = [x_old[i], x[i]]
        ys = [y_old[i], y[i]]
        m.plot(xs, ys, 'r', linewidth=1.0)
    p = m.plot(x_old, y_old, 'ro')
    p = m.plot(x,y,'y', linewidth=1.0)
    p = m.plot(x,y,'yo', linewidth=1.0)
    plt.title(title)
    plt.show()


#
#  todo: write plot_single_track_from_tab_file function
#
def plot_single_track_from_tab_file(filename : str, title : str = "Spreading Rate:"):
    x_old, y_old, ages, spreading_rates = dc.generate_plotable_data(filename)
    x, y = dc.map_xy_to_line(x_old, y_old)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    xavg = (xmax-xmin)/2.0
    yavg = (ymax-ymin)/2.0
    x_buffer = (xmax-xmin) / 10.0
    y_buffer = (ymax-ymin) / 10.0
    xmin -= x_buffer
    xmax += x_buffer
    ymin -= y_buffer
    ymax += y_buffer
    # Generate a basemap for the desired region
    m = Basemap(projection='merc', llcrnrlat=ymin, urcrnrlat=ymax,
                llcrnrlon=xmin, urcrnrlon=xmax, lat_ts=yavg, resolution='h')
    m.etopo(scale=2.0)
    m.drawcoastlines()

    # draw parallels and meridians.
    m.drawparallels(np.arange(ymin, ymax, 1.0))
    m.drawmeridians(np.arange(xmin, xmax, 1.0))

    # todo: change code below to draw line segments with color based on spreading rates
    x, y, = m(x,y)
    colormap = get_blue_green_red_colormap(spreading_rates.min(), spreading_rates.max())
    for i in range(len(x)-1):
        xs = [x[i], x[i + 1]]
        ys = [y[i], y[i + 1]]
        m.plot(xs, ys, color=colormap.get_color_tuple(spreading_rates[i]), linewidth=15.0)

    plt.show()


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






