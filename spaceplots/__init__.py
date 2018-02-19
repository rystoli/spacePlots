#version 2/18/18
"""
spacePlots is python code which makes use of many scientific python visualization libraries to quickly, from a distance matrix, summarize pairwise similarity data. This includes with and without dimension reduction techniques.
Git it at:
https://github.com/rystoli/spacePlots
"""


__version__ = "0.0.1"

import sys
sys.dont_write_bytecode = True
if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    raise ImportError("Python Version 2.6 or above is required for spacePlots.")
else:
    pass

del sys

# import
import spaceplot_DMtools as spdmt
import spaceplot_plotter as spp
import spaceplot_suite as sps
