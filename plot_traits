import pandas as pd
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors


"""""""""""""""""""""""""""""""""
Plotting based on Pearson r
"""""""""""""""""""""""""""""""""


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

def axesR_plot(r = None, label_axes = None, orthComp = True, figoutpath='AxesR_plot.png'):
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
    r: float list, pearson r
    label_axes: list of strings, labels for [x,y] axes
    orthComp: opaitonal, boolean, if True, provide Y axis as vector to highlight
              ...comparison of relationship to 0, or orthogonal axes
    figoutpath: str, filename/type if to save figure
    ---
    Returns: No return, plots and saves plot of axis relation
    '''
    
    # plotting setup
    plt.figure(figsize=(10,10))    
    plt.text(1.1, 0, 'Trustworthy', color='black', fontsize=12)
    plt.axis('off')
    ax = plt.gca()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal')  
    ax.set_title(figoutpath) 
    ax.annotate("", xy=(1, 0), xytext=(-1, 0), arrowprops=dict(arrowstyle="<->"), color='black')
    if orthComp: ax.annotate("", xy=(0, 1), xytext=(0, -1), arrowprops=dict(arrowstyle="<->"), color='black')
    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    
    # plot each trait
    if label_axes and len(label_axes) == len(r):
        for i in range(0, len(label_axes)):
            # create plot points
            soa = np.array([
                # coordinates for horizontal line (vector 1)
                [0, 0, 1, 0],
                [0, 0, -1, 0],
                # coordinates for related vector, vector 2
                [0, 0, rVecCoords(r[i])[0], rVecCoords(r[i])[1]],
                [0, 0, -1*rVecCoords(r[i])[0], -1*rVecCoords(r[i])[1]]
                ])
            X, Y, U, V = zip(*soa)
            c = i%len(colors)
            ax.quiver(-1*rVecCoords(r[i])[0], -1*rVecCoords(r[i])[1], rVecCoords(r[i])[0], rVecCoords(r[i])[1], angles='xy', scale_units='xy', width=0.005, scale=0.5, color=colors[c])
            plt.text(U[2]*1.1, rVecCoords(r[i])[1]*1.1, label_axes[i], color=colors[c], fontsize=12)
            
    # show and save plot 
    plt.draw()
    if figoutpath: plt.savefig(figoutpath)
    plt.show()
    
    

r values manually read from excel files
axesR_plot(r=[-0.603881480678335, -0.258798133617142, 0.649824342140376, 0.710274155232283], label_axes=['Angry', 'Adventurous', 'Friendly', 'Intellectual'], orthComp=True, figoutpath='s1FaceSM' )
axesR_plot(r=[-0.481273640379479, 0.0830071402971593, 0.654790548087786, 0.601089997305581], label_axes=['Angry', 'Adventurous', 'Friendly', 'Intellectual'], orthComp=True, figoutpath='s1FamiliarSM' )




"""""""""""""""""""""""""""""""""
Plotting based on factor analysis
"""""""""""""""""""""""""""""""""



def FactorAnalysis_plot(r = None, label_axes = None, figoutpath='FactorAnalysis_plot.png'):
    '''
    Plot factor analysis results 
    correlation between axes. X and Y axises respresent two factors.
    --- 
    ARGUMENTS:
    ---
    r: float list, pearson r
    label_axes: list of strings, labels for [x,y] axes
    figoutpath: str, filename/type if to save figure
    ---
    Returns: No return, plots and saves plot of axis relation
    '''
    
    # plotting setup
    plt.figure(figsize=(10,10))    
    plt.text(1.1, 0, 'PC1', color='black', fontsize=12)
    plt.text(0, 1.1, 'PC2', color='black', fontsize=12)
    plt.axis('off')
    ax = plt.gca()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_aspect('equal')  
    ax.set_title(figoutpath) 
    ax.annotate("", xy=(1, 0), xytext=(-1, 0), arrowprops=dict(arrowstyle="<->"), color='black')
    ax.annotate("", xy=(0, 1), xytext=(0, -1), arrowprops=dict(arrowstyle="<->"), color='black')
    colors = ['b', 'g', 'r', 'c', 'm', 'y']
    
    # plot each trait
    if label_axes and len(label_axes) == len(r):
        for i in range(0, len(label_axes)):
            c = i%len(colors)
            ax.quiver(0, 0, r[i][0], r[i][1], width=0.005, scale=4, color=colors[c])
            plt.text(r[i][0]*1.1, r[i][1]*1.1, label_axes[i], color=colors[c], fontsize=12)
            
    # show and save plot 
    plt.draw()
    if figoutpath: plt.savefig(figoutpath)
    plt.show()
    

df_features= pd.read_csv("s1FaceSM.csv")
fa = FactorAnalyzer(n_factors=2, rotation=None)
fa.fit(df_features)
FactorAnalysis_plot([fa.loadings_[1], fa.loadings_[3], fa.loadings_[10],fa.loadings_[11]], label_axes=['Angry', 'Adventurous', 'Friendly', 'Intellectual'], figoutpath='s1FaceSM' )

df_features= pd.read_csv("s1FamiliarSM.csv")
fa2 = FactorAnalyzer(n_factors=2, rotation=None)
fa2.fit(df_features)
FactorAnalysis_plot(r=[fa2.loadings_[1], fa2.loadings_[3], fa2.loadings_[10],fa2.loadings_[11]], label_axes=['Angry', 'Adventurous', 'Friendly', 'Intellectual'], figoutpath='s1FamiliarSM' )

df_features= pd.read_csv("s1GroupSM.csv")
fa3 = FactorAnalyzer(n_factors=2, rotation=None)
fa3.fit(df_features)
FactorAnalysis_plot(r=[fa3.loadings_[1], fa3.loadings_[3], fa3.loadings_[10],fa3.loadings_[11]], label_axes=['Angry', 'Adventurous', 'Friendly', 'Intellectual'], figoutpath='s1GroupSM' )

