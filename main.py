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

md.plot_single_track_from_tab_file(file1)

md.plot_tracks_from_tab_files([file1])