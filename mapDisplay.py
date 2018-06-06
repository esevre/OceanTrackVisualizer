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


class ColorPoint:
    def __init__(self, val : float, r : float, g : float, b : float, a : float = 0):
        self.val = val
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
        self.a = float(a)

    def __str__(self):
        return "val(%3.2f), (r,g,b,a) : %3.2f, %3.2f, %3.2f, %3.2f" % (self.val, self.r, self.g, self.b, self.a)


class ColorMap:
    def __init__(self, min : float, max : float):
        self.min = float(min)
        self.max = float(max)
        self.minColorPoint = ColorPoint(min, 0, 0, 0)
        self.maxColorPoint = ColorPoint(max, 1, 1, 1)
        self.color_points = [self.minColorPoint, self.maxColorPoint]
        self.tolerance = 1e-6

    def set_min(self, r : float, g : float, b : float, a : float = 1):
        self.color_points[0] = ColorPoint(self.min, r, g, b, a)
        self.minColorPoint = ColorPoint(self.min, r, g, b, a)

    def set_max(self, r : float, g : float, b : float, a : float = 1):
        self.color_points[-1] = ColorPoint(self.max, r, g, b, a)
        self.maxColorPoint = ColorPoint(self.max, r, g, b , a)

    def set_midpoint(self, r : float, g : float, b : float, a : float = 1):
        midpoint = 0.5 * (self.max + self.min)
        self.add_color_point(midpoint, r, g, b, a)

    def add_color_point(self, val : float, r : float, g : float, b : float, a : float = 1):
        # Check for a new min
        if (val < self.min):
            self.min = val
            self.color_points.insert(0, ColorPoint(val, r, g, b, a))
            return
        # Check for a new max
        if (val > self.max):
            self.max = val
            self.color_points.append(ColorPoint(val, r, g, b, a))
            return
        # Search for the index we want to place a new color node between
        for index, cp in enumerate(self.color_points):
            # Check if the current index is being replaced
            if (np.fabs(cp.val - val) < self.tolerance):
                self.color_points[index] = ColorPoint(val, r, g, b, a)
                return
            # Check if the data should be inserted before the current index:
            if (val < cp.val):
                self.color_points.insert(index, ColorPoint(val, r, g, b, a))
                return
        # It should not reach this point !
        print("invalid entry in colormap object")

    def get_color(self, val : float) -> ColorPoint:

        if val <= self.min:
            return self.minColorPoint
        if val >= self.max:
            return self.maxColorPoint
        id = 0
        for index, cp in enumerate(self.color_points):
            if val < cp.val:
                id = index
                break
        p1 = self.color_points[id - 1]
        p2 = self.color_points[id]
        w1 = (p2.val - val) / (p2.val - p1.val)
        w2 = 1.0 - w1

        r = w1 * p1.r + w2 * p2.r
        g = w1 * p1.g + w2 * p2.g
        b = w1 * p1.b + w2 * p2.b
        a = w1 * p1.a + w2 * p2.a

        return ColorPoint(val, r, g, b, a)


def get_blue_green_red_colormap(min : float, max : float) -> ColorMap :
    colormap = ColorMap(min, max)
    colormap.set_min(0, 0, 1)
    colormap.set_midpoint(0, 1, 0)
    colormap.set_max(1, 0, 1)
    return colormap


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






