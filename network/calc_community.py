import networkx as nx
import numpy as np
import pickle
import community

G = nx.Graph()
node1, node2 = np.loadtxt("../parallel/total-1.dat", usecols=(4,5), unpack=True, skiprows=1)

for i in range(len(node1)):
    G.add_edge(node1[i], node2[i])

# Python-Louvain: https://github.com/taynaud/python-louvain
# A python lib in accordance with networkx;
# Installed by "conda install -c conda-forge python-louvain"
# Code details can be found here: 
# https://github.com/taynaud/python-louvain/blob/master/community/community_louvain.py
# Documentation found here:
# https://python-louvain.readthedocs.io/en/latest/api.html#
part = community.best_partition(G,resolution=0.2)

# Methods in Networkx.algorithms
# https://networkx.github.io/documentation/stable/reference/algorithms/community.html
from networkx.algorithms import community

# greeday modularity communities
part = community.greedy_modularity_communities(G)

# girvan_newman model: slow
import itertools
comp = community.girvan_newman(G)
limited = itertools.takewhile(lambda c: len(c) <= k, comp)
for communities in limited:
    print(tuple(sorted(c) for c in communities))
    print(len(communities))

pickle.dump(part, open("commu_partition_dict.pkl", 'wb'))
