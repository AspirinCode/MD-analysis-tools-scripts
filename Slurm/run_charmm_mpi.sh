#!/bin/csh
#SBATCH --job-name=archmem
#SBATCH --partition=all-cpu
#SBATCH --qos=nogpu
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=2
#SBATCH --export=ALL
#SBATCH --time=48:00:00
#SBATCH --oversubscribe

#charmm="/home/shf317/bin/c40a1_ifort"
#set charmm=`/home/shf317/bin/charmm_mpi`
set charmm = /home/shf317/bin/charmm_mpi
module load mvapich2/2.1/intel-16.0.3

#set SLURM_NODEFILE=`get_slurm_nodelist`
cd $SLURM_SUBMIT_DIR

#MPI execute command
#-f: specify implementation-defined specification file
#-n: specify number of processes to use
#mpiexec -f ${SLURM_NODEFILE} -n ${SLURM_NTASKS} ${charmm} < step6.1_equilibration.inp > step6.1_equilibration.out

mpiexec -n ${SLURM_NTASKS} ${charmm} < step6.1_equilibration.inp > step6.1_equilibration.out

exit
