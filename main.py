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
# md.plot_track_line_with_correction_from_tab_file(file1)

# md.plot_single_track_from_tab_file(file1)


colormap = md.ColorMap(0.0, 1.0)
colormap.set_min(0, 0, 1)
colormap.set_max(1, 0, 0)
colormap.set_midpoint(0, 1, 0)


for cp in colormap.color_points:
    print(cp)

print(colormap.get_color(0.25))
print("*****************************")
for i in range(11):
    print(colormap.get_color(0.1 * i))




