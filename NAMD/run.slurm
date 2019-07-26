#!/bin/csh
#SBATCH --partition=im1080
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --export=ALL
#SBATCH -t 00:10:00
#SBATCH --oversubscribe
##SBATCH --mail-user=chd415@lehigh.edu
##SBATCH --mail-type=BEGIN
##SBATCH --mail-type=END

setenv I_MPI_SHM_LMT shm

set echo

module unload namd
module unload cuda/8.0
module load cuda/10.0
module load mvapich2/2.2/intel-18.0.1 


setenv PATH /home/chd415/apps/namd/v2.13/:$PATH
setenv LD_LIBRARY_PATH /home/chd415/apps/namd/v2.13/:$LD_LIBRARY_PATH
setenv LD_LIBRARY_PATH /home/chd415/apps/namd/v2.13/lib:$LD_LIBRARY_PATH

#module load namd/2.13
#set namd2 = `which namd2`


set LOCAL = /share/ceph/scratch/${USER}/${SLURM_JOBID}
set SLURM_NODEFILE=`get_slurm_nodelist`
set NODEFILE = namd.nodelist
echo group main > $NODEFILE

foreach node ($SLURM_JOB_NODELIST)
    echo host $node >> $NODEFILE
end

cd $SLURM_SUBMIT_DIR/

@ cxt = ${cnt} - 1
@ pstep = 1000 * ${cnt}
@ istep = ${pstep} + 1000
@ ncnt = ${cnt} + 1
@ nrep = 8

#if ( ! -e  step5_${cxt}.coor ) exit

sleep 5

@ inputnum = ${cnt} - 1

sed -e 's/inputnum/'${inputnum}'/g' step5.namd | sed -e 's/outputnum/'${cnt}'/g' | sed -e 's/USER/'${USER}'/g' | sed -e 's/SLURM_JOBID/'${SLURM_JOBID}'/g' > junk.namd

sed -e 's/pcnt/'${cxt}'/g' -e 's/pstep/'${pstep}'/g' -e 's/istep/'${istep}'/g' base.conf > job_$cnt.conf

./make_output_dirs.sh output ${nrep}
charmrun namd2 ++local +p${SLURM_NTASKS} ++nodelist namd.nodelist +replicas ${nrep} job_$cnt.conf +stdout output/%d/job_${cnt}.%d.log
#charmrun namd2 ++remote-shell ssh +p $SLURM_NPROCS junk.namd | tee junk.out > /dev/null



#$namd2 +p $SLURM_NPROCS junk.namd | tee step5_${cnt}.out > /dev/null

#sleep 5

#if ( ! -e  ${LOCAL}/step5_${cnt}.coor ) exit

cp -r ${LOCAL}/* $SLURM_SUBMIT_DIR/

sleep 5

@ cnt = ${cnt} + 1

sleep 5

if ( ${cnt} > ${cntmax} ) exit

#cd ../../..

#sbatch --export cnt=${cnt},cntmax=5 run.slurm  
exit
