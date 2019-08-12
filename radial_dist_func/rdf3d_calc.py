from math import sqrt, ceil, pi
from os import listdir
import pickle

import numpy as np
from matplotlib import pyplot as plt

def find_1st_min(array):
    """
    Find the first minimum of array;
    :param array: a Numpy array
    :return: the array index of the first minimum
    """
    # Shift the array 1 step forward, append 0 at the end
    diff = np.copy(array)
    diff = np.delete(diff, 1, 0)
    diff = np.append(diff, [0], 0)

    assert len(diff) == len(array)

    # Do subtraction to get the difference between each pair of neighbors
    diff = diff - array

    flag = 0
    for i in range(len(diff)):
        if diff[i] < 0 and flag == 0:
            flag = 1
        if diff[i] > 0 and flag == 1:
            return i
    return 0

def rdf_3d(file_dir, dr=0.15, maxbin=300, figname='rdf.png', save_hist=False):
    """
    Plot 3D radial distribution function. Initially benchmarked on quinone.

    :param file_dir: directory containing coordinates files, eg. './data'
                    each coor file has 1st line as box size, and remainings
                    as coordinates;
    :param dr: 0.15 default, the bin size of histogram;
    :param maxbin: maximum number of bins;
    :param figname: name for output figure
    :return: 0
    """

    files = listdir(file_dir)
    nfile = len(files)

    hist = np.zeros(maxbin+1)

    for file in files:
        x, y, z = np.loadtxt(f'{file_dir}/{file}', unpack=True)
        npart = len(x)
        box_size = np.asarray([x[0], y[0], z[0]])
        box_half = box_size/2.0
        for i in range(1, npart):
            for j in range(i+1, npart):
                dx = x[i] - x[j]
                dy = y[i] - y[j]
                dz = z[i] - z[j]

                # Atoms pair with image cell atoms if distance > half the box size
                if dx < -box_half[0]: dx += box_size[0]
                if dx > box_half[0]: dx -= box_size[0]
                if dy < -box_half[1]: dy += box_size[1]
                if dy > box_half[1]: dy -= box_size[1]
                if dz < -box_half[2]: dz += box_size[2]
                if dz > box_half[2]: dz -= box_size[2]

                rd = sqrt(dx*dx+dy*dy+dz*dz)

                bin = int(ceil(rd/dr))
                if bin <= maxbin:
                    hist[bin] += 1

    # Postprocessing to normalize
    hist = hist/nfile
    # Distance array with dr as the spacing
    distance = np.arange(0.5, maxbin+1.5) * dr
    # Volumn of the shell at distance r: 4 * pi * r^2 * dr
    vshell = np.power(distance, 2) * 4 * pi * dr
    # Density: N / V
    box_vol = box_half[0] * box_half[1] * box_half[2]
    density = (npart-1) / box_vol
    # Normalize
    hist_norm = ( hist/vshell ) / density

    # For calc coordination number, by integrating the RDF out to the first minimum;
    first_min = find_1st_min(hist_norm)
    dist_first_peak = distance[0:first_min+1]
    # sum[ 4 * pi * r^2 * dr * g(r) ] * N / V
    ncoor = np.power(dist_first_peak, 2)*hist_norm[0:first_min+1] * 4 * pi * dr
    ncoor = np.sum(ncoor) * (npart-1) / box_vol

    # Save the histogram results
    if save_hist == True:
        pickle_name = f'{file_dir}_py.pickle'
        pickle.dump([hist_norm, distance, box_half, maxbin, dr],
               open(pickle_name, 'wb'))

    # Output calculation result of coordination number and details
    print("="*18)
    print("Directory name is ", file_dir)
    print("Calculation details: dr = ", dr, ", bin number = ", maxbin)
    print("Coordination number is ", ncoor)
    print("The first shell is located inside ", distance[first_min], " Angstrom.")

    # Plot
    plt.plot(distance, hist_norm, label=file_dir)
    plt.xlabel('Distance between quinone head groups ')
    plt.ylabel('g(r)')
    plt.xticks(np.arange(0, 45, step=5))
    plt.legend()
    plt.savefig(figname)
    plt.close(figname)
    plt.clf()

def load_pkl_data(pickle_file):
    hist_norm, distance, box_half, maxbin, dr = pickle.load(open(pickle_file, 'rb'))
    return hist_norm, distance, box_half, maxbin, dr

if __name__ == '__main__':
    #rdf_3d('10-men8', dr=0.2, maxbin=220, figname='10-men8-rdf.png', save_hist=True)
    #rdf_3d('20-men8', dr=0.2, maxbin=220, figname='20-men8-rdf.png', save_hist=True)
    rdf_3d('30-men8', dr=0.2, maxbin=220, figname='30-men8-rdf.png', save_hist=True)
    rdf_3d('40-men8', dr=0.2, maxbin=220, figname='40-men8-rdf.png', save_hist=True)
    rdf_3d('50-men8', dr=0.2, maxbin=220, figname='50-men8-rdf.png', save_hist=True)

    hist_norm, distance, box_half, maxbin, dr = load_pkl_data("50-men8_py.pickle")
    print(hist_norm)

