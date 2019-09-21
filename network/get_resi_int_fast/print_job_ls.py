#!/usr/python

# Specify system parameter
traj_len    = 1000
freq_frame  = 4
time_step   = 0.24
total_frame = int(traj_len/time_step/freq_frame)
batch_size  = 20

# Job configuration printer functional
for i in range(int(total_frame/batch_size)):
    beg = batch_size * i + 1
    end = batch_size * (i + 1)
    print(f"sbatch --export=iframe={beg},eframe={end} -p eng -t 18:00:00 -J fast-int run_charmm.sh")
