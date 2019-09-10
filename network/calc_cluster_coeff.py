import networkx as nx
import numpy as np
import pickle

#graph_inputs = ["network-cutoff-7-allatom.dat",
#                "network-cutoff-6-a.dat",
#                "network-cutoff-4-a.dat",
#                "network-cutoff-5-a.dat",
#                "network-cutoff-3-a.dat",
#                "network-cutoff-7-a.dat"]

graph_inputs = ["tetra-data/network-tetra-all.dat"]

for input in graph_inputs:
    G = nx.Graph()
    node1, node2 = np.loadtxt(input, usecols=(4,5), unpack=True, skiprows=1)
    for i in range(len(node1)):
        G.add_edge(node1[i], node2[i])

    graph_num_node = G.number_of_nodes()
    print(f"{input} contains {graph_num_node} nodes.")

    graph_num_edge = G.number_of_edges()
    print(f"{input} contains {graph_num_edge} edges.")

    cu = nx.clustering(G)
    cu_res = np.array([(int(key), cu[key]) for key in cu.keys() ])
    cu_sorted = cu_res[cu_res[:,0].argsort()]
    pickle.dump(cu_sorted, open(f"cluster_coeff.pkl", 'wb'))

    #node_bet_central = nx.betweenness_centrality(G)
    #res = np.array([(int(key), node_bet_central[key]) 
    #                    for key in node_bet_central.keys() ])

    #res_sorted = res[res[:,0].argsort()]
    #pickle.dump(res_sorted, open(f"C_B_{input[0:-4]}.pkl", 'wb'))

print("Finished!")
