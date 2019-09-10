import numpy as np
import matplotlib.pyplot as plt
import pickle

cluster = pickle.load(open("cluster_coeff.pkl", 'rb'))

plt.figure(figsize=(30,15))
plt.plot(cluster[0:654,0], cluster[0:654,1])
plt.xlim(0, 655)
plt.xlabel("Residue ID", fontsize=22)
plt.ylabel("Cluster coefficient", fontsize=22)
plt.fill_between(cluster[0:654,0], 0.65, 0.45, alpha=0.3, color="purple")
plt.xticks()
plt.xticks(np.arange(0, 655, 50), fontsize=18)
plt.yticks(fontsize=18)
plt.savefig("cluster_coeffi_plot.png", dpi=100)

# Store info about nodes with high cluster coefficient
string = ""
list_high = []
for i in range(int(len(cluster[:,0])/4)):
    if cluster[i,1] >= 0.65:
        string += f"{int(cluster[i,0])+1} "
        list_high.append(int(cluster[i,0])+1)
pickle.dump(list_high, open("list_high_cluster_065.pkl", 'wb'))

# Store info about nodes with low cluster coefficient
string = ""
list_low = []
for i in range(int(len(cluster[:,0])/4)):
    if cluster[i,1] < 0.45:
        string += f"{int(cluster[i,0])+1} "
        list_low.append(int(cluster[i,0])+1)
pickle.dump(list_low, open("list_low_cluster_045.pkl", 'wb'))
