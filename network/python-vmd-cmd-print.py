#!/usr/bin/env python
import pickle
import numpy as np

idx, x, y, z = np.loadtxt("network_pos.dat", unpack=True)
coor = np.column_stack((x, y, z))
pos_dict = dict(zip(idx, coor))

col1, col2 = np.loadtxt("network-cutoff-7-allatom.dat", unpack=True, usecols=(0,1))

#print(pos_dict[col1[0]])

print("axes location off")
print("display projection orthographic")
print("color Display Background white")

print("draw color red")
for i in range(len(col1)):
    print("draw line {%.4f %.4f %.4f} {%.4f %.4f %.4f} width 1 " % 
          (pos_dict[col1[i]][0], pos_dict[col1[i]][1], pos_dict[col1[i]][2], 
           pos_dict[col2[i]][0], pos_dict[col2[i]][1], pos_dict[col2[i]][2]))

          
for key in pos_dict.keys():
    print("draw sphere {%.4f %.4f %.4f} radius 0.5 resolution 1" % 
          (pos_dict[key][0], pos_dict[key][1], pos_dict[key][2]))

print("draw color yellow")
list_high = pickle.load(open("list_high_cluster_065.pkl", 'rb'))
for i in range(len(list_high)):
    key = list_high[i]
    print("draw sphere {%.4f %.4f %.4f} radius 1 resolution 1" %
          (pos_dict[key][0], pos_dict[key][1], pos_dict[key][2]))

print("draw color blue")
list_low = pickle.load(open("list_low_cluster_045.pkl", 'rb'))
for i in range(len(list_low)):
    key = list_low[i]
    print("draw sphere {%.4f %.4f %.4f} radius 1 resolution 1" %
          (pos_dict[key][0], pos_dict[key][1], pos_dict[key][2]))

print("display resetview")
