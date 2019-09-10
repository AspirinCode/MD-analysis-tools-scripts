import numpy as np
import pickle
import matplotlib.pyplot as plt

# Number of frames to average
nframe = 6

for i in range(1,nframe):
    c_B = pickle.load(open(f"C_B_total-{i}.pkl", "rb"))
    # Extract the betweenness centrality column
    col1 = c_B[:,1]
    # Fold 4 subunits into 4 columns for averaging
    col1_4col = col1.reshape((-1,4), order="F")
    # If first frame, set it to c_B_bundle
    if i == 1:
        c_B_bundle = col1_4col
    else:
        c_B_bundle = np.column_stack((c_B_bundle, col1_4col))

# Calculate the mean & std
c_B_ave = np.mean(c_B_bundle, axis=1)
c_B_std = np.std(c_B_bundle, axis=1)

# Plotting details
plt.figure(figsize=(30,10))
plt.plot(c_B[0:654,0], c_B_ave)
plt.fill_between(c_B[0:654,0], c_B_ave-c_B_std, c_B_ave+c_B_std,alpha=0.3, facecolor="red")
plt.xlabel("Residue ID", fontsize=18)
plt.ylabel("Betweenness centrality", fontsize=18)
plt.show()

