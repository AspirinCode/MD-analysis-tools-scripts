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
# echo commands to stdout 

#charmm="/home/shf317/bin/c40a1_ifort"
set charmm = "/home/shf317/bin/charmm"
set LOCAL = /scratch/${USER}/${SLURM_JOBID}

# run OpenMP program
#for i in `seq 0 5`;
  #${charmm}  < men8-conf.inp > men8-conf.out #/dev/null 
  #${charmm}  < step3_packing.inp > ${LOCAL}/step3_packing.out #/dev/null 
  #${charmm}  < step4_lipid.inp > ${LOCAL}/step4_lipid.out #/dev/null 
  #${charmm}  < step5_assembly.inp > ${LOCAL}/step5_assembly.out #/dev/null 
  #${charmm}  < step5.1_input.inp > ${LOCAL}/step5.1_input.out #/dev/null 
  #${charmm}  < pene_solver.inp > ${LOCAL}/pene_solver.out
  #${charmm} < hydro_thick.inp > ${LOCAL}/hydro_thick.out
  #${charmm} local=${LOCAL} timeseries=500ns tcnt=0 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  ##${charmm} local=${LOCAL} timeseries=501-1000ns tcnt=2084 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} local=${LOCAL} timeseries=1001-1500ns tcnt=4167 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} local=${LOCAL} timeseries=1501-2000ns tcnt=6250 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} local=${LOCAL} timeseries=2001-3000ns tcnt=8334 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} local=${LOCAL} timeseries=3001-4000ns tcnt=12500 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} local=${LOCAL} timeseries=4001-5000ns tcnt=16667 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} local=${LOCAL} timeseries=5001-6000ns tcnt=20834 < cbd_flip_calc.inp > /dev/null #${LOCAL}/cbd_flip_calc.out
  #${charmm} < recenter.inp > ${LOCAL}/recenter.out
  #${charmm}  local=${LOCAL} < residue_int.inp > ${LOCAL}/residue_int.out
  ${charmm}  local=${LOCAL} batchid=${batchid} batchbeg=${batchbeg} batchend=${batchend} < residue_int_tetra_pl.inp > /dev/null #${LOCAL}/residue_int_tetra_pl.out
  #${charmm}  local=${LOCAL} < residue_pos.inp > ${LOCAL}/residue_int.out
  #${charmm}  local=${LOCAL} < residue_pos.inp > ${LOCAL}/residue_int.out
  cp ${LOCAL}/* $SLURM_SUBMIT_DIR/parallel_5001_6000ns
  sleep 2

exit
