from importer import *
import spaceplot_DMtools as spdmt # tools to load/manipulate distance matrices
import spaceplot_plotter as spp # plotting tools

######################################################################
# Plot suite
######################################################################

def spacePlot_suite( dm_csvpath, figlist = ['DM','Network'], axes_r = None ):
    '''
    Display and save spacePlots figures
    ---
    ARGUMENTS:
    ---
    dm_csvpath: str, path to DM csv file
        * csv should be symmetric distance matrix (i.e., 0 along diagnoal)
        * csv first row & column should be variable names, with the column of variable names
        ..named 'variables', e.g., text file as:
        
            variables, v1_name, v2_name, v3_name
            v1_name,   0,       .1,      .2
            v2_name,   .1,      0,       .3
            v3_name,   .2,      .3,      0
    figlist: optional, list of strs, specify plots, default to all plots but axes correlation plts
             spacePlot options:
                 - 'DM': Distance matrix plot
                 - 'Network': Network graph plot
    axes_r: optional, list, [float, r coefficient for axes relationship plot, produced if r coefficient
            ...provided in this argument], [list of strs, [label1,label2] ]
    ---
    Returns: No return, displays and saves all plots
    '''
    
    labels,DM = spdmt.read_DM( dm_csvpath )
    
    if 'DM' in figlist:
        spp.DM_plot(labels,DM)
    if 'Network' in figlist:
        spp.DM_to_NetworkGraph_plot( labels, DM )
        display(Image(filename='NetworkGraph_plot.png') )
    if axes_r:
        spp.axesR_plot(axes_r[0], label_axes=axes_r[1], orthComp=True )
