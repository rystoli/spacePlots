from importer import *
sys.dont_write_bytecode = True

######################################################################
# Distance matrix plotting
######################################################################

def DM_plot(labels,DM,figoutpath='DM_plot.png'):
    '''
    Plot distance matrix (DM)
    ---
    ARGUMENTS:
    ---
    labels: list of strings, each element a variable name
    DM: 2x2 numpy array, symmetric DM
    figoutpath: optional, str, filename/type if to save figure
    ---
    Returns: no return, produces plot
    '''
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    fig, axs = plt.subplots(figsize=(11, 9))
    sns.heatmap(DM, xticklabels = labels, yticklabels = labels, cmap=cmap)
    plt.xticks(rotation=45)
    if figoutpath: fig.savefig(figoutpath)
    plt.show()

######################################################################
# Network graph plotting
######################################################################

# TO DO
### cluster node/edge reformatting option
### more flexible formatting

def write_rawDot( labels, DM ):
    '''
    Write raw dot file before formatting
    ---
    ARGUMENTS:
    ---
    labels: list of strings, each element a variable name
    DM: 2x2 numpy array, symmetric DM
    ---
    Return: no return, writes .dot file
    '''
    pg_DM = np.array(DM, [('len',  float)])
    G = nx.from_numpy_matrix(pg_DM)
    G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),labels)))
    G = nx.drawing.nx_agraph.to_agraph(G)
    G.write('rawDot.dot')

def write_formatDot(labels, rawDot = 'rawDot.dot', nodehex = '#9ec3ff', edgehex = '#e2e2e2'):
    '''
    Write reformatted dot file
    ---
    ARGUMENTS:
    ---
    labels: list of strings, each element a variable name
    rawDot: defaults to 'rawDot.dot', written by write_rawDot(), recommend
            ...leaving this all alone, letting it operate as written, as
            ...it assumes the rawDot.dot has formatting of original dot output
    nodehex: str, default hexidecimal coloring of nodes
    edghex: str, default hexidecimal coloring of edges
    ---
    Return: no return, writes reformatted formatDot.dot file
    '''
    
    with open('rawDot.dot') as f:
        content = f.readlines()
    f.close()
    content = [x.strip() for x in content] 
    content.insert(1,'graph [overlap=false outputorder=edgesfirst];')
    content.insert(2,'node [shape="circle" style=filled color="gray" fixedsize=true size=4000 label="" fontname=Arial fontsize=12 labeljust="r"];')
    content.insert(3,'edge [style="dashed" color="%s" penwidth=2.2];' % edgehex)

    # label 
    for i,label in enumerate(labels):
        content.insert(i+3,'%s [fillcolor="%s" xlabel="%s"];' % (label,nodehex,label))
    
    # write formatted dot file
    newdot = open('formatDot.dot', 'w')
    for item in content:
        newdot.write("%s\n" % item)
    newdot.close()

def dot_plot( formatDot = 'formatDot.dot' ):
    '''
    Plots and writes plot image 'NetworkGraph_plot.png' from 
    ...reformmated dot file 'formatDot.dot'
    ---
    ARGUMENTS:
    ---
    formatDot: str, filepath of reformmated dot file (or dot file you wish to plot)
    ---
    Return: no return, outputs plot/writes NetworkGraph_plot.png
    '''
    pg_Plot = pg.AGraph('formatDot.dot')
    pg_Plot.layout() 
    pg_Plot.draw('NetworkGraph_plot.png')

def DM_to_NetworkGraph_plot( labels, DM ):
    '''
    Plots and writes plot image 'NetworkGraph_plot.png' from distance matrix
    ---
    ARGUMENTS:
    ---
    labels: list of strings, each element a variable name
    DM: 2x2 numpy array, symmetric DM
    ---
    Return: no return, outputs plot/writes NetworkGraph_plot.png
    '''
    write_rawDot( labels, DM )
    write_formatDot( labels )
    dot_plot()

######################################################################
# Axis relation plotting (r coefficient relation)
######################################################################

def r2slope( r ):
    '''
    Take r coefficient, returns slope of one vector
    relative to another vector assumed to be a horizontal line
    ---
    ARGUMENTS:
    ---
    r: float, pearson r
    ---
    Returns: float, returns slope of vector compared to other vector assumed to be m=0/1
    '''
    deg = np.rad2deg(np.arccos(r))
    return np.tan(np.deg2rad(deg))

def rVecCoords( r ):
    '''
    Gets coordinates for vector with length 1 as slope for r
    relative to horizontal vector
    ---
    ARGUMENTS:
    ---
    r: float, pearson r
    ---
    Returns: list, x,y coordinates of vector, length 1 end with slope
             ...of axis relative to another assuming r correlation
             ...between the two
    '''
    return [np.cos(np.arccos(r)),np.sin(np.arccos(r))]

def axesR_plot( r, label_axes = None, orthComp = True, figoutpath='AxesR_plot.png'):
    '''
    Plot relation of two axes to one another based on Pearson
    correlation between axes. One axis is horizontal X axis,
    light gray vertical axis is provided by default for comparison
    to no relation. For recommended ways to estimate
    r coefficient between groups of variables, e.g., groups
    via clustering/PCA, see: http://www.statsoft.com/Textbook/Cluster-Analysis
    ---
    ARGUMENTS:
    ---
    r: float, pearson r
    label_axes: optional, list of strings, labels for [x,y] axes
    orthComp: opaitonal, boolean, if True, provide Y axis as vector to highlight
              ...comparison of relationship to 0, or orthogonal axes
    figoutpath: optional, str, filename/type if to save figure
    ---
    Returns: No return, plots and saves plot of axis relation
    '''
    # create plot points
    #### each array is a 2-point vector, [x1, y1, x2, y2]
    soa = np.array([
        # coordinates for horizontal line (vector 1)
        [0, 0, 1, 0],
        [0, 0, -1, 0],
        # coordinates for related vector, vector 2
        [0, 0, rVecCoords(r)[0], rVecCoords(r)[1]],
        [0, 0, -1*rVecCoords(r)[0], -1*rVecCoords(r)[1]]
        ])

    # plot
    X, Y, U, V = zip(*soa)
    plt.figure(figsize=(8,8))
    ax = plt.gca()
    if orthComp: ax.annotate("", xy=(0, 1), xytext=(0, -1), arrowprops=dict(arrowstyle="<->"), color='#F5F5F5')
    ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal')
    if label_axes:
        plt.text(1.1, 0, label_axes[0], fontsize=12)
        plt.text(U[2]+.1*np.sign(U[2]), rVecCoords(r)[1]+.1, label_axes[1], fontsize=12)
    plt.axis('off')
    plt.draw()
    if figoutpath: plt.savefig(figoutpath)
    plt.show()
