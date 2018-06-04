#
#  Main program for visualization of spreading rates
#
#
#  mpl_toolkits.basemap provides mapping tools for projecting points on a map
#
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

import processFile as pf
import dataComputation as dc
import mapDisplay as md

from matplotlib.collections import LineCollection


#
#  Get data from a file, load into header and data objects
#
# header, data = pf.get_data_from_tab_separated_file('file.csv')
#
# x = np.array([x for x, y, age in data])
# y = np.array([y for x, y, age in data])
#
# age = np.array([age for x, y, age in data])
#
# x_old = np.array([x for x, y, age in data])
# y_old = np.array([y for x, y, age in data])
#
# pts = []
# pts_old = []
# for i in range(len(x)):
#     pts.append(dc.point(x[i], y[i]))
#     pts_old.append(dc.point(x_old[i], y_old[i]))
#
# spreading_rates = dc.generate_spreading_rates(age, pts)
# spreading_rates.append( spreading_rates[-1])
#
# spreading_rates_old = dc.generate_spreading_rates(age, pts_old)
#

file1 = 'file.csv'
x, y, ages, spreading_rates = md.generate_plotable_data(file1)

plt.plot(spreading_rates)
plt.show()

# plt.plot(spreading_rates_old)
# plt.show()


#
#  Map x,y coordinates to a straight line
#
# This correction happens when x,y are created
# x, y = dc.map_xy_to_line(x, y)


xavg, yavg = np.average(x), np.average(y)
xmin, xmax = min(x), max(x)
ymin, ymax = min(y), max(y)

print(xmin, ymin)
print(xavg, yavg)
print(xmax, ymax)

xmin =  62.
xmax =  68.
ymin = -15.
ymax = -12.

kilometer = 1000.0



# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
m = Basemap(projection='merc',llcrnrlat=ymin,urcrnrlat=ymax,\
            llcrnrlon=xmin,urcrnrlon=xmax,lat_ts=yavg,resolution='h')
m.etopo(scale=2.0)
m.drawcoastlines()

# draw parallels and meridians.
m.drawparallels(np.arange(ymin, ymax, 1.0))
m.drawmeridians(np.arange(xmin, xmax, 1.0))

#
# approximate our data and plot on the map
#
x, y = m(x, y)
# x_old, y_old = m(x_old, y_old)






# cs = m.contour(x, y, age)
# for i in range(len(x)):
    # xs = [x_old[i], x[i]]
    # ys = [y_old[i], y[i]]
    # m.plot(xs, ys, 'r', linewidth=1.5)
# p = m.plot(x_old, y_old, 'ro')
p = m.plot(x, y, 'y', linewidth=1.0)
p = m.plot(x, y, 'yo', linewidth=1.0)

plt.title("Yellow Track: Corrected Data\nRed Dots: Original Data")
plt.show()



