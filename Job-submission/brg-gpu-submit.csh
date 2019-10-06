#!/bin/csh
#SBATCH -N 2
#SBATCH -p GPU
#SBATCH --ntasks-per-node 16
#SBATCH --gres=gpu:p100:2
#SBATCH --job-name="holostro"
#SBATCH -t 48:00:00
#SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

## -N 2 can be changed

module load namd/namd_gpu

nvidia-smi

$BINDIR/namd2 +p $SLURM_NPROCS +pemap 0-13+14 step6.1_equilibration.inp | tee step6.1_equilibration.out > /dev/null

set i = 1
  @ i = ${i} + 4
  while ( ${i} <= 6 )
     @ pcnt = ${i} - 1
  if ( ${pcnt} > 0 && (! -e step6.${pcnt}_equilibration.coor)) exit
  $BINDIR/namd2 +p $SLURM_NPROCS +pemap 0-13+14 step6.${i}_equilibration.inp | tee step6.${i}_equilibration.out > /dev/null
  @ i = ${i} + 1
end
