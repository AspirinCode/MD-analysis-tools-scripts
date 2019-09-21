#!/usr/bin/python
import networkx as nx
import numpy as np
import pickle

# Read all the graphes and convert into adjacency matrix array
def convert_graph_to_adjacency_array(G):
    adj_mat = nx.to_numpy_matrix(G, nodelist=np.sort(G.nodes()) )
    adj_arr = np.array(adj_mat).reshape(-1,len(G.nodes()))  # convert to array
    return adj_arr


graph_ls = []
adj_arr = []
for i in range(5):
    G = nx.Graph()
    node1, node2 = np.loadtxt(f"parallel/total-{i+1}.dat", usecols=(4,5),
                                unpack=True, skiprows=1)
    for i in range(len(node1)):
        G.add_edge(node1[i], node2[i])
    graph_ls.append(G)
    adj_arr.append(convert_graph_to_adjacency_array(G))

# Stack the above arrays together and average on the final axis
adj_stk = np.dstack(tuple(adj_arr))
print("Stacked array shape is ", adj_stk.shape, ".")
mean_arr = np.mean(adj_stk, axis=2)

# Filter the contacts with > 75% contact freq
node_filtered = []
edge_cnt      = 0
for i in range(2616):
    for j in range(2616):
        if mean_arr[i,j] > 0.75:
            edge_cnt += 1
            node_filtered.append((i,j))
print(f"Find {edge_cnt} edges with > 75% contact frequency.")

pickle.dump(node_filtered, open('node_filtered.pkl', 'wb'))
print("Saved the avaraged graph! Congrats!")

# Build the final time-averaged graph
G = nx.Graph()
for i in range(len(node_filtered)):
    G.add_edge(node_filtered[i])

# Continue other operation;
