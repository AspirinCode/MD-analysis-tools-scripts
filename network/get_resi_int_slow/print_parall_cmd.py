#!/bin/python

# Specified for different system
partition = "lts"
totres = 2616

# Do a batch for every 5 residues as 'residue I'
# for 'residue J': loop it through the whole I+1 to the end of tetramer
for i in range(int(totres/5)):
    beg = i*5 + 1
    end = (i+1)*5
    print(f"sbatch --export=batchid={i+1},batchbeg={beg},batchend={end} -p {partition} -J nx -t 72:00:00 run_batch_pl.sh")

# Handle the remaining residues <= 5 
i += 1
beg = i*5 + 1
if beg < totres:
    print(f"sbatch --export=batchid={i+1},batchbeg={beg},batchend={totres} -p {partition} -J nx -t 72:00:00 run_batch_pl.sh")

