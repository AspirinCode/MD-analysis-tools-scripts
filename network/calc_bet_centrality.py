import networkx as nx
import numpy as np
import pickle

G = nx.Graph()
node1, node2 = np.loadtxt(graph_input, usecols=(0,1), unpack=True)

for i in range(len(node1)):
    G.add_edge(node1[i], node2[i])

graph_num_node = G.number_of_nodes()
print(f"This graph contains {graph_num_node} nodes. ")

graph_num_edge = G.number_of_edges()
print(f"This graph contains {graph_num_edge} edges. ")

node_bet_central = nx.betweenness_centrality(G)
pickle.dump(node_bet_central, open("node_betweeen_centrality.pkl", 'wb'))

res = np.array([(int(key), node_bet_central[key]) for key in node_bet_central.keys() ])
res_sorted = res[res[:,0].argsort()]
ax.xaxis.set_minor_locator(MultipleLocator(10))


pos = dict(zip(idx.astype(int), np.column_stack((x, y, z))))

pos = {}
for i in range(len(idx)):
    pos[str(int(idx[i]))] = (x[i], y[i], z[i])

for key in pos.keys():
    position[key] = {'posi': pos[key]}

nx.set_node_attributes(G, poistion)

pos = nx.get_node_attributes(G, 'posi')
n = G.number_of_nodes()

degrees = [val for (node, val) in G.degree()]

edge_max = max(degrees)
colors = [plt.cm.plasma(degrees[i]/edge_max) for i in range(n)]

with plt.style.context(('ggplot')):
    fig = plt.figure(figsize=(10,7))
    ax = Axes3D(fig)

    for key, value in pos.items():
        xi = value[0]
        yi = value[1]
        zi = value[2]

        ax.scatter(xi, yi, zi, c=colors[key], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)

    for i, j in enumerate(G.edges()):
        x = np.array((pos[j[0]][0], pos[j[1]][0]))
        y = np.array((pos[j[0]][1], pos[j[1]][1]))
        z = np.array((pos[j[0]][2], pos[j[1]][2]))
        ax.plot(x, y, z, c='black', alpha=0.5)

    ax.view_init(30, angle)
    ax.set_axis_off()

    plt.show()

    return


