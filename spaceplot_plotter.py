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
