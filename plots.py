import numpy
import pylab
import sys
import matplotlib.font_manager as font_manager

def main(args):
    """
    Creates a file <prefix>_plots.pdf showing the time evolution of various
    network properties, where <prefix> is specified as a command-line argument.
    """

    prefix = args[0]
    size = 6
    pylab.rcParams["axes.titlesize"] = size
    pylab.rcParams["axes.labelsize"] = size
    pylab.rcParams["xtick.labelsize"] = size
    pylab.rcParams["ytick.labelsize"] = size
    pylab.rcParams["legend.fontsize"] = size    
    fig = pylab.figure(1, figsize = (14, 30), dpi = 500)

    #############################
    ### Degree (simultaneous) ###
    #############################
    
    fh = open("%s_SIM_DEG/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 921
    ax = fig.add_subplot(9, 2, 1)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 1, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 922
    ax = fig.add_subplot(9, 2, 2)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 2, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    #############################
    ### Degree (sequential) ###
    #############################
    
    fh = open("%s_SEQ_DEG/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 923
    ax = fig.add_subplot(9, 2, 3)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 3, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 924
    ax = fig.add_subplot(9, 2, 4)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 4, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)


    ##################################
    ### Betweenness (simultaneous) ###
    ##################################
    
    fh = open("%s_SIM_BET/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 925
    ax = fig.add_subplot(9, 2, 5)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 5, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 926
    ax = fig.add_subplot(9, 2, 6)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 6, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    ################################
    ### Betweenness (sequential) ###
    ################################
    
    fh = open("%s_SEQ_BET/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 927
    ax = fig.add_subplot(9, 2, 7)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 7, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 928
    ax = fig.add_subplot(9, 2, 8)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 8, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    ################################
    ### Closeness (simultaneous) ###
    ################################
    
    fh = open("%s_SIM_CLO/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 929
    ax = fig.add_subplot(9, 2, 9)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 9, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 9210
    ax = fig.add_subplot(9, 2, 10)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 10, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    ##############################
    ### Closeness (sequential) ###
    ##############################
    
    fh = open("%s_SEQ_CLO/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 9211
    ax = fig.add_subplot(9, 2, 11)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 11, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 9212
    ax = fig.add_subplot(9, 2, 12)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 12, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    ##################################
    ### Eigenvector (simultaneous) ###
    ##################################
    
    fh = open("%s_SIM_EIG/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 9213
    ax = fig.add_subplot(9, 2,13)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 13, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 9214
    ax = fig.add_subplot(9, 2, 14)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 14, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    ################################
    ### Eigenvector (sequential) ###
    ################################
    
    fh = open("%s_SEQ_EIG/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 9215
    ax = fig.add_subplot(9, 2, 15)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 15, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 9216
    ax = fig.add_subplot(9, 2, 16)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 16, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)

    ##############
    ### Random ###
    ##############
    
    fh = open("%s_RAN/FILES" %(prefix), "r")
    a = [open(line.strip(), "r").readlines() for line in fh.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # clustering
    y5, Y5, Y5ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        i += 1
        if i == len(a):
            i = 0
            Y1.append(numpy.mean(y1))
            Y1ERR.append(numpy.std(y1))
            y1 = []
            Y2.append(numpy.mean(y2))
            Y2ERR.append(numpy.std(y2))
            y2 = []
            Y3.append(numpy.mean(y3))
            Y3ERR.append(numpy.std(y3))
            y3 = []
            Y4.append(numpy.mean(y4))
            Y4ERR.append(numpy.std(y4))
            y4 = []
            Y5.append(numpy.mean(y5))
            Y5ERR.append(numpy.std(y5))
            y5 = []
    T = range(len(Y1))

    # 9217
    ax = fig.add_subplot(9, 2,17)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"robustness $R$, clustering $C$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y1, "b-", linewidth = 1, alpha = 0.6, label = "$R$")
    pylab.plot(T, Y4, "g-", linewidth = 1, alpha = 0.6, label = "$C$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 17, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"assortativity $r$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y5, "r-", linewidth = 1, alpha = 0.6, label = "$r$")
    pylab.legend(loc = "upper right", frameon = True)
    
    # 9218
    ax = fig.add_subplot(9, 2, 18)
    pylab.xlabel(r"epoch $t$")
    xmax =  max(T) - max(T) % 100
    pylab.xlim(0, xmax)
    pylab.xticks(range(0, xmax + 100, 100))
    pylab.ylabel(r"variance $v$")
    #pylab.ylim(0, 1)
    ax.yaxis.set_ticks_position("left")
    pylab.plot(T, Y2, "b-", linewidth = 1, alpha = 0.6, label = "$v$")
    pylab.legend(loc = "upper left", frameon = True)
    ax = fig.add_subplot(9, 2, 18, sharex = ax, frameon = False)
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    pylab.ylabel(r"mean path length $\ell$")
    #pylab.ylim(-0.1, 0.1)
    ax.yaxis.set_ticks_position("right")
    pylab.plot(T, Y3, "g-", linewidth = 1, alpha = 0.6, label = "$\ell$")
    pylab.legend(loc = "upper right", frameon = True)
    
    pylab.savefig("%s_plots.pdf" %(prefix),
                  format = "pdf",
                  bbox_inches = "tight")
    pylab.close(1)

if __name__ == "__main__":
    main(sys.argv[1:])
