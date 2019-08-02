import os,sys,re,math
from numpy import *

input = open ("./" + sys.argv[1] + "/" + sys.argv[2] + "_" + sys.argv[3] + ".dat", "r").readlines()

for column in range(1, 10):
        energylist = []
        for line in input:
                energy = float(line.split()[column])
                energylist.append(energy)
                energya = array(energylist,dtype=float)
        average = energya.mean()
        sd = energya.std()
        if str(column) == "1":
                ave1 = average
        elif str(column) == "2":
                ave2 = average
        elif str(column) == "3":
                ave3 = average
        elif str(column) == "4":
                ave4 = average
        elif str(column) == "5":
                ave5 = average
        elif str(column) == "6":
                ave6 = average
        elif str(column) == "7":
                ave7 = average
        elif str(column) == "8":
                ave8 = average
        elif str(column) == "9":
                ave9 = average
tot = ave1 + ave2 + ave3 + ave4 + ave5 + ave6 + ave7 + ave8 + ave9
print  sys.argv[3],ave1/tot,ave2/tot,ave3/tot,ave4/tot,ave5/tot,ave6/tot,ave7/tot,ave8/tot,ave9/tot

