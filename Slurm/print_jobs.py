#!/bin/python

# Specified for different system
partition = "engi"
totres = 2616

# Do a batch for every 5 residues as 'residue I'
# for 'residue J': loop it through the whole I+1 to the end of tetramer
#for i in range(int(totres/5)):
#    beg = i*5 + 1
#    end = (i+1)*5
#    print(f"sbatch --export=batchid={i+1},batchbeg={beg},batchend={end} -p {partition} -J nx -t 12:00:00 run_batch_pl.sh")

# Handle the remaining residues <= 5
#i += 1
#beg = i*5 + 1
#if beg < totres:
#    print(f"sbatch --export=batchid={i+1},batchbeg={beg},batchend={totres} -p {partition} -J nx -t 12:00:00 run_batch_pl.sh")


# Print job submission codes with estimated time
def calc_time(ires):
    """
    argu:ires:i-th residue;
    return:
        hours, min needed for the job;
    """
    base = 2.9                      # unit:day
    itime = base*(1-ires/totres)
    hr = int(itime*24)              # convert to hr:min:00
    min = int((itime*24-hr)*60)
    return hr+2, min

for i in range(totres):
    beg = i + 1
    end = i + 1
    hr, min = calc_time(i)
    print(f"sbatch --export=batchid={i+1},batchbeg={beg},batchend={end} -p {partition} -J nx -t {hr}:{min}:00 run_batch_pl.sh")
