import networkx as nx
import numpy as np
import pickle
import community

G = nx.Graph()
node1, node2 = np.loadtxt("../parallel/total-1.dat", usecols=(4,5), unpack=True, skiprows=1)

for i in range(len(node1)):
    G.add_edge(node1[i], node2[i])

#part = best_partition(G)
part = community.best_partition(G,resolution=0.2)

# greeday modularity communities
part = community.greedy_modularity_communities(G)

# girvan_newman model
import itertools
comp = community.girvan_newman(G)
limited = itertools.takewhile(lambda c: len(c) <= k, comp)
for communities in limited:
    print(tuple(sorted(c) for c in communities))
    print(len(communities))

pickle.dump(part, open("commu_partition_dict.pkl", 'wb'))
