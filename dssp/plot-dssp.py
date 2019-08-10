import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
plt.switch_backend('agg')

dssp_dict = {
    "H": 1, # alpha helix 4-12
    "B": 2, # isolated beta-bridge
    "E": 3, # strand
    "G": 4, # 3-10 helix
    "I": 5, # pi helix
    "T": 6, # turn
    "S": 7  # bend
}

numframe = 1000 #2048 #10

for i in range(numframe):
    with open(f'extr/frame{i}-extr.dssp', 'r') as f:
        lines = f.readlines()

    dssp = np.zeros(len(lines))
    j = 0
    for line in lines:
        line = line.split()
        if line != []:
            dssp[j] = dssp_dict[line[0]]
        j += 1
    if i == 0:
        dssp_all = dssp
    else:
        #print(np.shape(dssp_all), np.shape(dssp))
        dssp_all = np.vstack((dssp_all, dssp))

cbar_kws = {
    "C": 0,
    "H": 1, # alpha helix 4-12
    "B": 2, # isolated beta-bridge
    "E": 3, # strand
    "G": 4, # 3-10 helix
    "I": 5, # pi helix
    "T": 6, # turn
    "S": 7  # bend

}

# maybe this set of color
cmap = ['#1f78b4','#a6cee3', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00']

fig = plt.figure(figsize=(18,18), dpi=100)
#sns.set_palette("bright")
#cmap=['#7fc97f','#beaed4','#fdc086', '#ffff99', '#386cb0','#f0027f', '#bf5b17', '#666666']
ax = sns.heatmap(dssp_all[:,0:653].T, square=False, cbar=True, vmin=0, vmax=7, cbar_kws={"ticks":range(8)}, cmap=cmap)
#plt.show()

fig.savefig(f'{numframe}-frames.png', format='png', dpi=100)
