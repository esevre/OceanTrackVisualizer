#
#  Main program for visualization of spreading rates
#
#
#  Simple examples of what can be done with the code I am creating
#
import mapDisplay as md
import dataComputation as dc
import processFile as pf

import os

#
#  Simplest code to plot the actual track line, and the corrected track line
#

def test_01():
    file1 = 'file.csv'

    md.plot_single_track_from_tab_file(file1)

    md.plot_tracks_from_tab_files([file1])


# test_01()
print('*****   Test 01 complete   ********')

def test_02():
    directory = 'segment4_tracks'
    file1 = os.path.join(directory, 'TrackA_tab.txt')
    file2 = os.path.join(directory, 'TrackAp_tab.txt')
    file3 = os.path.join(directory, 'TrackB_tab.txt')
    file4 = os.path.join(directory, 'TrackBp_tab.txt')
    file5 = os.path.join(directory, 'TrackC_tab.txt')
    file6 = os.path.join(directory, 'TrackCp_tab.txt')
    file7 = os.path.join(directory, 'TrackD_tab.txt')
    file8 = os.path.join(directory, 'TrackDp_tab.txt')
    file9 = os.path.join(directory, 'TrackEp_tab.txt')


    track_files = [file1, file2, file3, file4, file5, file6, file7, file8, file9]

    md.plot_tracks_from_tab_files(track_files)

test_02()