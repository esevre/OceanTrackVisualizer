#
#  Main program for visualization of spreading rates
#
#
#  Simple examples of what can be done with the code I am creating
#
import mapDisplay as md


#
#  Simplest code to plot the actual track line, and the corrected track line
#
file1 = 'file.csv'
md.plot_track_line_with_correction_from_tab_file(file1)


# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# lat_ts is the latitude of true scale.
# resolution = 'c' means use crude resolution coastlines.
# m = Basemap(projection='merc',llcrnrlat=ymin,urcrnrlat=ymax,\
#             llcrnrlon=xmin,urcrnrlon=xmax,lat_ts=yavg,resolution='h')
# m.etopo(scale=2.0)
# m.drawcoastlines()
#
# # draw parallels and meridians.
# m.drawparallels(np.arange(ymin, ymax, 1.0))
# m.drawmeridians(np.arange(xmin, xmax, 1.0))

#
# approximate our data and plot on the map
#
# x, y = m(x, y)
# x_old, y_old = m(x_old, y_old)



# for i in range(len(x)):
    # xs = [x_old[i], x[i]]
    # ys = [y_old[i], y[i]]
    # m.plot(xs, ys, 'r', linewidth=1.5)
# p = m.plot(x_old, y_old, 'ro')
# p = m.plot(x, y, 'y', linewidth=1.0)
# p = m.plot(x, y, 'yo', linewidth=1.0)
#
# plt.title("Yellow Track: Corrected Data\nRed Dots: Original Data")
# plt.show()



