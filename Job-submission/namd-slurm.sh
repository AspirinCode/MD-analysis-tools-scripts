#!/bin/csh
#SBATCH --reservation=shf317_93
#SBATCH --partition=im2080-gpu
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=10
#SBATCH --export=ALL
#SBATCH -t 6:00:00
#SBATCH --oversubscribe
#SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name=40_MEN8

module load namd/2.12-gpu
set namd2 = `which namd2`

#cd $SLURM_SUBMIT_DIR
set LOCAL = /scratch/${USER}/${SLURM_JOBID}
echo $LOCAL

set infile = new-step7.1.inp
set scratch = `sed -n "/set scratch/s/;//g"p ${infile} | awk '{print $3}'`
sed -i -e "/set scratch/s|\${scratch}|\${LOCAL}|g" ${infile}
echo $scratch


set cnt = 1
set cntmax = 1200 #Please change to the needed maximum ns

#For counting to which ns production has run
while (${cnt} <= ${cntmax})
   if ( ! -e step7.${cnt}_production.coor ) break
   @ cnt = $cnt + 1
end
if ( $cnt > $cntmax ) exit

echo $cnt

set i = 0
while ( ${i} <= 35 ) #Change to maximum ns that can be run in 48h
  if ( ${cnt} != 1 ) then
   @ pcnt = ${cnt} - 1
   if ( ! -e step7.${pcnt}_production.coor ) exit
   if ( ${cnt} > ${cntmax} ) exit
   set icnt  = `sed -n "/set cnt/s/;//g"p ${infile} |awk '{print $3}'`
   set ifile = `sed -n "/set inputname/s/;//g"p ${infile} |awk '{print $3}'`
   set jfile = step7.${pcnt}_production
   sed -i -e "/set cnt/s/${icnt}/${cnt}/g" -e "/set inputname/s/${ifile}/${jfile}/g" ${infile}
  endif

   $namd2 +p $SLURM_NPROCS ${infile} | tee ${LOCAL}/step7.${cnt}_production.out > /dev/null
   cp ${LOCAL}/*${cnt}* $SLURM_SUBMIT_DIR
#   cp ${LOCAL}/*${cnt}_* $SLURM_SUBMIT_DIR
   rm $SLURM_SUBMIT_DIR/*restart*
      sleep 5

   @ i = ${i} + 1
   @ cnt = ${cnt} + 1
end

sbatch run_namd_scratch.sh
exit
