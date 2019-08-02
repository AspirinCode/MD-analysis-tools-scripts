#!/bin/csh
#SBATCH --partition=im1080
#SBATCH --qos=no-gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --export=ALL
#SBATCH -t 48:00:00
#SBATCH --oversubscribe
#SBATCH --mail-user=shaalltime@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --job-name=rest2-v2

#set MAX_ICNT = 50
#module load namd/2.13
#set namd2 = `which namd2`

set NAMD_DIR = /home/shf317/bin/NAMD/NAMD_2.13b1_Linux-x86_64-verbs-smp

# let: allow simple arithmetic calc
set nrep = 10
set icnt = 0


@ pcnt = $icnt - 1
@ pstep = 100 * $icnt
@ istep = $pstep + 100
@ ncnt = $icnt + 1

sed -e "s/pcnt/$pcnt/g" -e "s/pstep/$pstep/g" -e "s/istep/$istep/g" base.conf > job$icnt.conf

#if [ $icnt -lt $MAX_ICNT ]
#then
#  echo
#  #qsub --dependencies $COBALT_JOBID -t 1:00:00 -n 128 -A $PROJECT --env icnt=$ncnt:n=$n:nrep=$nrep run.sh
#fi

# ./make_output_dirs.sh output $nrep
@ nppn = ${SLURM_NTASKS} / $nrep

# +p${nrep}, this number be the same as $nrep, or its multiples;
$NAMD_DIR/charmrun +p${SLURM_NTASKS} $NAMD_DIR/namd2 ++ppn $nppn +replicas $nrep job$icnt.conf +stdout output/%d/job$icnt.%d.log
