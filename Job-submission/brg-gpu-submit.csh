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



###================================
#   Another example 
###================================

#!/bin/csh
#SBATCH --partition=gpu-shared
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=12
##SBATCH --gres=gpu:k80:2
#SBATCH -t 00:10:00
#SBATCH --export=ALL
#SBATCH --no-requeue

#K80 -- 4GPUs & 24 cores; P100 -- 2 GPUs & 14 cores;

#Path to GPU enabled NAMD
module load cuda
setenv PATH /home/shashaf/apps/namd/v2.12/:$PATH
setenv LD_LIBRARY_PATH /home/shashaf/apps/namd/v2.12/:$LD_LIBRARY_PATH
setenv LD_LIBRARY_PATH /home/shashaf/apps/namd/v2.12/lib:$LD_LIBRARY_PATH

namd2 +p12 namd.inp | tee namd.out > /dev/null


###================================
#   NAMD setting 
###================================

module load namd/2.12

setenv CONV_RSH ssh

cd ${SLURM_SUBMIT_DIR}

set SLURM_NODEFILE=`get_slurm_nodelist`

set NODELIST = namd2.nodelist
set NODES    = `cat $SLURM_NODEFILE | sort -u `

echo group main > $NODELIST
foreach node ( $NODES )
  echo host $node >> $NODELIST
end

set charmrun = `which charmrun`
set namd2 = `which namd2`

set i = 1
#  @ i = ${i} + 2
while ( ${i} <= 6 )
   @ pcnt = ${i} - 1
   if ( ${pcnt} > 0 && (! -e step6.${pcnt}_equilibration.coor)) exit
   $charmrun $namd2 +p ${SLURM_NTASKS} ++nodelist ${NODELIST} ++ppn ${SLURM_NNODES} step6.${i}_equilibration.inp > step6.${i}_equilibration.out
   @ i = ${i} + 1
end

exit
