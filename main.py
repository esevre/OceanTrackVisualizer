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


colormap = md.get_blue_green_red_colormap(-3.14, 3.14)


for cp in colormap.color_points:
    print(cp)

print(colormap.get_color(0.25))
print("*****************************")
for i in range(61):
    print(colormap.get_color(-3.14+0.1 * i))




