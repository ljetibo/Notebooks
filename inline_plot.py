import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import csv

def readCSV(filename):
    
    f = open(filename)
    readlines = csv.reader(open(filename))
    
    block, RBlock, RAll = [], [], []
    title = ""
    for row in f.readlines():
        if row.startswith("#"):
            title+=row
        else:
            line = row.split(",")
            try:
                block.append(float(line[0]))
                RBlock.append(float(line[1]))
                RAll.append(float(line[2]))
            except:
                pass

    title = title.replace(",", " ")
    title = title.replace("\n", "")
    title = title.replace("#", "")
    return title, block, RBlock, RAll

def plotCSV(filename, returned=False):
            
    title, block, RBlock, RAll = readCSV(filename)
    fig, ax = plt.subplots(figsize=[7,7])

    #MAIN PLOT SETTINGS AND PLOTS
    #----------------------------------------------------------------------
    ax.plot(block, RBlock, label="<P> per blocks", linewidth=2)
    ax.plot(block, RAll, label="<P> per total counts", linewidth=2)
    plt.title(title)
    plt.xlabel("N")
    plt.ylabel("<P>")
    

    #INSERTED AXIS SETTINGS AND PLOTS
    #----------------------------------------------------------------------
    axins = inset_axes(ax, width=6, height=4, loc=4, bbox_to_anchor=(0.6, 0.2),
                 bbox_transform=ax.figure.transFigure) # zoom = 6
    
    axins.plot(block, RBlock, label="<P> per blocks", linewidth=1.5)
    axins.plot(block, RAll, label="<P> per per total counts", linewidth=1.5) 

    x1, x2, y1, y2 = block[-1]-1, block[-1], RAll[-1]-0.1, RBlock[-1]+0.1
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    plt.xlabel("N")
    plt.ylabel("<P>")
    plt.legend(bbox_to_anchor=(0.9, 0.85),
               bbox_transform=ax.figure.transFigure)
    

    #PLOT IT
    #----------------------------------------------------------------------
    plt.show()
    
    if returned:
        return block, RBlock, RAll
    

plotCSV("inline_plot.txt")
