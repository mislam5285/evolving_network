# Evolving a Complex Network

Python code for evolving complex networks to maximize their [robustness](http://dx.doi.org/10.1371/journal.pone.0059613).

`evolving_network.py`: This script uses the parameters specified in `<params file>` to evolve a seed network until it is maximally robust, and saves the resulting (robust) network in GraphML format.

```bash
$ python evolving_network.py <params file>
```

The parameters file (see [params.json.sample](params.json.sample)) has the following JSON format:
```bash
{
    "seedNetwork"        : {"name" : "barabasi_albert_graph", 
                            "args" : {"n" : 100, "m" : 3}},
    "mutantsPerEpoch"    : 10,
    "rewiringsPerMutant" : 10,
    "stagnantEpochs"     : 30,
    "attackStrategy"     : "degree", 
    "sequentialMode"     : false,
    "maximizeRobustness" : true, 
    "outFile"            : "network.graphml", 
    "verbose"            : true
}
```
where `seedNetwork` specifies the seed network to evolve (see details below); `mutantsPerEpoch` specifies the number of mutants to generate in each epoch; `rewiringsPerMutant` specifies the number of edge rewirings per mutant; `stagnantEpochs` specifies how many epochs to wait until termination, during which there is no increase in robustness; `attackStrategy` specifies the attack strategy (betweenness, closeness, degree, eigenvector, or random) to use in order to assess the robustness of the evolving network; `sequentialMode` specifies whether the mode of attack is sequential or simultaneous; `maximizeRobustness` specifies whether to maximize or minimize robustness of the evolving network; `outfile` specifies the name of the output file which will store the evolved network; and `verbose` specifies whether or not to output the properties of the network as it evolves.

The `seedNetwork` parameter includes `name`, which can be any network construction method from [NetworkX](https://networkx.github.io/) (`barabasi_albert_graph` for example), and `args`, which are the arguments for that method (`n` and `m` for example).

`plots.py`: This script creates plots (as PDF files) showing the time evolution of various network properties (averaged over all the replicates) generated from the results produced by the `evolving_network.py` program (if `verbose` is `true`). The names of the result files, one per replicate, are fed in via `STDIN`.

```bash
$ python plots.py < FILES
```

## Software Dependencies

* [igraph](http://igraph.org/)
* [Matplotlib](http://matplotlib.org/)
* [NetworkX](https://networkx.github.io/)
* [NumPy](http://www.numpy.org/)
* [Python](https://www.python.org/)

## Contact

If you have any questions about the software, please email swami.iyer@gmail.com.

