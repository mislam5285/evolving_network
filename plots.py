import numpy
import pylab
import sys
import matplotlib.font_manager as font_manager

def main(args):
    """
    Creates a files (plot1-6.pdf) showing the time evolution of various
    network properties, generated from the results produced by the 
    evolving_network.py program. The names of the result files, one per 
    replicate, are fed in via STDIN.
    """
    a = [open(line.strip(), "r").readlines() for line in sys.stdin.readlines()]
    m = max([len(v) for v in a])
    a = [v + [v[-1]] * (m - len(v)) for v in a]
    i = 0
    y1, Y1, Y1ERR = [], [], [] # robustness
    y2, Y2, Y2ERR = [], [], [] # degree variance
    y3, Y3, Y3ERR = [], [], [] # avg. path length
    y4, Y4, Y4ERR = [], [], [] # communities
    y5, Y5, Y5ERR = [], [], [] # clustering
    y6, Y6, Y6ERR = [], [], [] # assortativity
    while len(a[i]) > 0:
        toks = map(float, a[i].pop(0).strip().split())
        y1.append(toks[0])
        y2.append(toks[1])
        y3.append(toks[2])
        y4.append(toks[3])
        y5.append(toks[4])
        y6.append(toks[5])
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
            Y6.append(numpy.mean(y6))
            Y6ERR.append(numpy.std(y6))
            y6 = []

    T = range(len(Y1))
    font_prop = font_manager.FontProperties(size = 12)

    # robustness vs epoch
    pylab.figure(1, figsize = (7, 5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"robustness $R$", fontproperties = font_prop)
    #pylab.errorbar(T, Y1, Y1ERR, color = "k", fmt = ".")
    pylab.plot(T, Y1, "k-", linewidth = 2, alpha = 0.6)
    pylab.xlim(0, max(T))
    pylab.savefig("plot1.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)

    # degree variance vs epoch
    pylab.figure(1, figsize = (7, 5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"degree variance $Var(k)$", fontproperties = font_prop)
    #pylab.errorbar(T, Y2, Y2ERR, color = "k", fmt = ".")
    pylab.plot(T, Y2, "k-", linewidth = 2, alpha = 0.6)
    pylab.xlim(0, max(T))
    pylab.savefig("plot2.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)

    # average path length vs epoch
    pylab.figure(1, figsize = (7, 5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"average path length $\ell$", fontproperties = font_prop)
    #pylab.errorbar(T, Y3, Y3ERR, color = "k", fmt = ".")
    pylab.plot(T, Y3, "k-", linewidth = 2, alpha = 0.6)
    pylab.xlim(0, max(T))
    pylab.savefig("plot3.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)

    # number of communities vs epoch
    pylab.figure(1, figsize = (7, 5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"number of communities $\kappa$", fontproperties = font_prop)
    #pylab.errorbar(T, Y4, Y6ERR, color = "k", fmt = ".")
    pylab.plot(T, Y4, "k-", linewidth = 2, alpha = 0.6)
    pylab.xlim(0, max(T))
    pylab.savefig("plot4.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)

    # clustering coefficient vs epoch
    pylab.figure(1, figsize = (7, 5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"clustering coefficient $C$", fontproperties = font_prop)
    #pylab.errorbar(T, Y5, Y5ERR, color = "k", fmt = ".")
    pylab.plot(T, Y5, "k-", linewidth = 2, alpha = 0.6)
    pylab.xlim(0, max(T))
    pylab.savefig("plot5.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)

    # assortativity coefficient vs epoch
    pylab.figure(1, figsize = (7, 5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"assortativity coefficient $r$", fontproperties = font_prop)
    #pylab.errorbar(T, Y6, Y4ERR, color = "k", fmt = ".")
    pylab.plot(T, Y6, "k-", linewidth = 2, alpha = 0.6)
    pylab.xlim(0, max(T))
    pylab.savefig("plot6.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)

if __name__ == "__main__":
    main(sys.argv[1:])
