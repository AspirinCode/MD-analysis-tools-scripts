#!/bin/csh
#SBATCH --job-name="inter"
#SBATCH --partition=eng
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 48:00:00
# echo commands to stdout 
 
set LOCAL = /scratch/${USER}/${SLURM_JOBID}

cd $SLURM_SUBMIT_DIR

set resid = ${ir}

while ( ${resid} <= ${fr} )
   charmm local=${LOCAL} sys=${sys} resid=${resid} < inter_om.inp > /dev/null

   mv ${LOCAL}/om_${sys}_${resid}_*.dat $SLURM_SUBMIT_DIR/${sys}
   sleep 2

   @ resid += 1
end


exit

