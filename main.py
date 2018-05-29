#
#  Main program for visualization of spreading rates
#
#


from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


import processFile as pf

header, data = pf.get_data_from_tab_separated_file('file.csv')
header, data = pf.get_data_from_tab_separated_file('file.csv')
header, data = pf.get_data_from_tab_separated_file('file.csv')

x = np.array([x for x, y, age in data])
y = np.array([y for x, y, age in data])
age = np.array([age for x, y, age in data])

x_old = np.array([x for x, y, age in data])
y_old = np.array([y for x, y, age in data])


import dataComputation as dc
pts = []
for i in range(len(x)):
    pts.append(dc.point(x[i], y[i]))

for pt in pts:
    print(pt)

pta = dc.point(x[0], y[0])
ptb = dc.point(x[-1], y[-1])

demo1 = dc.project_point_on_line(pta, pta, ptb)
demo2 = dc.project_point_on_line(ptb, pta, ptb)

print("demo 1: ", demo1)
print("demo 2: ", demo2)
print(ptb - pta)


pts = dc.project_points_on_line(pts, pta, ptb)

for i, pt in enumerate(pts):
    x[i] = pt.x
    y[i] = pt.y

print(x)
print(y)

for i in range(len(x)):
    xs = [x_old[i], x[i]]
    ys = [y_old[i], y[i]]
    plt.plot(xs, ys, 'r', linewidth=0.5)
plt.plot(x_old, y_old, 'or', x, y, 'ob')
plt.title("Red: Original Points,\nBlue: Corrected Points")
plt.show()

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
x_old, y_old = m(x_old, y_old)

# cs = m.contour(x, y, age)
for i in range(len(x)):
    xs = [x_old[i], x[i]]
    ys = [y_old[i], y[i]]
    m.plot(xs, ys, 'r', linewidth=1.5)
p = m.plot(x_old, y_old, 'ro')
p = m.plot(x, y, 'y', linewidth=1.0)
p = m.plot(x, y, 'yo', linewidth=1.0)

plt.title("Yellow Track: Corrected Data\nRed Dots: Original Data")
plt.show()



