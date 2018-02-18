from importer import *
sys.dont_write_bytecode = True

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