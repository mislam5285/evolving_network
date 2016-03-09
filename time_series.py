import pandas, pylab, sys
import matplotlib.font_manager as font_manager

def main(args):
    """
    Plots the s-i-r curves from the results produced by disease_verbose.py (fed 
    via STDIN) and saves the plot in a file called sir.pdf.
    """
    data = pandas.read_table(sys.stdin, header = None)
    font_prop = font_manager.FontProperties(size = 12)
    pylab.figure(1, figsize = (7, 4.5), dpi = 500)
    pylab.xlabel(r"epoch $t$", fontproperties = font_prop)
    pylab.ylabel(r"robustness $R$, assortativity $r$, clustering $C$", 
                 fontproperties = font_prop)
    T = range(len(data))
    R, r, C = list(data[0]), list(data[1]), list(data[2])
    pylab.plot(T, R, "b-", linewidth = 2, alpha = 0.6, label = r"$R$")
    pylab.plot(T, r, "g-", linewidth = 2, alpha = 0.6, label = r"$r$")
    pylab.plot(T, C, "r-", linewidth = 2, alpha = 0.6, label = r"$C$")
    pylab.xlim(0, max(T))
    #pylab.ylim(0, 1.0)
    pylab.legend(loc = 'upper right', prop = font_prop)
    pylab.savefig("time_series.pdf", format = "pdf", bbox_inches = "tight")
    pylab.close(1)
    
if __name__ == "__main__":
    main(sys.argv[1:])
