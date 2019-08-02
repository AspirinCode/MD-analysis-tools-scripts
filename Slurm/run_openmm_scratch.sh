#!/bin/csh
#SBATCH --reservation=shf317_93
#SBATCH --partition=im2080-gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --export=ALL
#SBATCH -t 48:00:00
#SBATCH --oversubscribe
#SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name=v2-cbd

module load cuda/10.0
module load anaconda/python3
#setenv CUDA_VISIBLE_DEVICES 0

setenv OPENMM_PLUGIN_DIR /share/ceph/woi216group/shared/apps/openmm-7.3.0/lib/plugins
setenv PYTHONPATH /share/ceph/woi216group/shared/apps/openmm-7.3.0/lib/python3.5/site-packages
setenv LD_LIBRARY_PATH /share/ceph/woi216group/shared/apps/openmm-7.3.0/lib:$LD_LIBRARY_PATH

#set LOCAL = /share/ceph/scratch/shf317/${SLURM_JOBID}
set LOCAL = /scratch/shf317/${SLURM_JOBID}

#set init = cal-add-step7.8 
#set input = step7.0_production
#set istep = step7_1
#python -u openmm_run.py -i ${input}.inp -t toppar.str -p ${init}.psf -c ${init}.crd -b ${init}.str -orst ${LOCAL}/${istep}.rst -odcd  ${LOCAL}/${istep}.dcd | tee  ${LOCAL}/${istep}.out > /dev/null
#cp ${LOCAL}/${istep}.* $SLURM_SUBMIT_DIR
#sleep 5
#exit

#Equilibration

# Phase 0
#set input = step7_phase0
#set init = step5_charmm2omm
#python -u openmm_run.py -i ${input}.inp -t toppar.str -p ${init}.psf -c ${init}.crd -orst ${LOCAL}/${istep}.rst -odcd ${LOCAL}/${istep}.dcd | tee ${LOCAL}/${istep}.out > /dev/null
#cp ${LOCAL}/${istep}.* $SLURM_SUBMIT_DIR
#sleep 2

#
## Normal phase
#set init = step5_charmm2omm
#set cnt = 1
#
#while ( ${cnt} <= 6 )
#    @ pcnt = ${cnt} - 1
#    set istep = step6.${cnt}_equilibration
#    set pstep = step6.${pcnt}_equilibration
#
# 
#    if ( ${cnt} == 1 ) then
#        python -u openmm_run.py -i ${istep}.inp -t toppar.str -p ${init}.psf -c ${init}.crd -b ${init}.str -orst ${LOCAL}/${istep}.rst -odcd  ${LOCAL}/${istep}.dcd | tee  ${LOCAL}/${istep}.out > /dev/null
#    else
#        if ( ! -e ${pstep}.rst ) break
#        python -u openmm_run.py -i ${istep}.inp -t toppar.str -p ${init}.psf -c ${init}.crd -irst ${pstep}.rst -orst  ${LOCAL}/${istep}.rst -odcd  ${LOCAL}/${istep}.dcd | tee ${LOCAL}/${istep}.out > /dev/null
#    endif
#    cp ${LOCAL}/${istep}.* $SLURM_SUBMIT_DIR
#    sleep 2
#    @ cnt += 1
#end
#
#exit

# Production
cd $SLURM_SUBMIT_DIR

# step5.3_charmm2omm are the one with 4 pot changed to 4 cal;
set init = step5_charmm2omm 

set cnt = 1
set cntmax = 140
while (${cnt} <= ${cntmax})
   if ( ! -e step7_${cnt}.dcd ) break
   @ cnt = $cnt + 1
end
if ( $cnt > $cntmax ) exit

set input = step7_production

set i = 0
while ( ${i} <= 7 )

    @ pcnt = ${cnt} - 1
    set istep = step7_${cnt}
    set pstep = step7_${pcnt}

    if ( ${cnt} == 1 ) set pstep = step6.6_equilibration

    if ( ! -e ${pstep}.rst ) exit

    #if ( ${cnt} <= 20 ) then
    #    set input = step7_phase1
    #  else if ( ${cnt} <= 40 ) then
    #    set input = step7_phase2
    #  else if ( ${cnt} <= 60 ) then
    #    set input = step7_phase3
    #  else if ( ${cnt} <= 80 ) then
    #    set input = step7_phase4
    #  else if ( ${cnt} <= 100 ) then
    #    set input = step7_phase5
    #  else
    #    set input = step7_phase5 
    #endif
    echo $input $cnt

    python -u openmm_run.py -i ${input}.inp -t toppar.str -p ${init}.psf -c ${init}.crd -irst ${pstep}.rst -orst ${LOCAL}/${istep}.rst -odcd ${LOCAL}/${istep}.dcd | tee ${LOCAL}/${istep}.out > /dev/null
    sleep 2

    if ( ! -e ${LOCAL}/${istep}.rst ) exit

    cp ${LOCAL}/${istep}.* $SLURM_SUBMIT_DIR
    sleep 2
    @ i += 1
    @ cnt = ${cnt} + 1
end

sbatch run_openmm_scratch.sh

exit
