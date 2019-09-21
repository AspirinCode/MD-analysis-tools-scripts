#!/bin/csh
#SBATCH --job-name=charmm
#SBATCH --partition=eng
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
##SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --time=36:00:00
#SBATCH --oversubscribe

set charmm = "/home/shf317/bin/charmm"
set LOCAL = /scratch/${USER}/${SLURM_JOBID}

set START = `date +%s`

${charmm} local=${LOCAL} timeseries=5001-6000ns iframe=${iframe} eframe=${eframe} < resi_int_fast_frame.inp > /dev/null #${LOCAL}/resi_int_fast_frame.out
cp ${LOCAL}/* $SLURM_SUBMIT_DIR/int-5001-6000ns/
sleep 2

set END = `date +%s`
@ DIFF = $END - $START
echo "It takes $DIFF seconds"

exit
