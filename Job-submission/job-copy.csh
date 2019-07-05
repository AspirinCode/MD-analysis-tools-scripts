#!/bin/csh


#Usage:for copy files to similar directories
set cpfile = run_gpu_dep.sh
set i = 0
while ( ${i} <= 4 )
   echo "cp ~/workdir/50_men8_pg_zw/namd/${cpfile} ~/workdir/${i}0_men8_pg_zw/namd"
   @ i = ${i} + 1
end

#Usage:for batching several jobs simultaneously
#syntax: csh job.sh > junk.sbatch
#chmod +x junk.sbatch
#./junk.sbatch
set i = 0
while ( ${i} <= 5 )
   echo "cd ~/workdir/${i}0_men8_pg_zw/namd"
   echo "sbatch --job-name=mpz_p_${i}0 ~/workdir/${i}0_men8_pg_zw/namd/run_gpu_dep.sh"
   @ i = ${i} + 1
end

#Usage:for checking each system
#syntax: csh job.sh > junk.ls
#chmod +x junk.ls
#./junk.ls
set i = 0
while ( ${i} <= 5 )
   echo "echo ${i}0_men8_pg_zw/namd/"
   echo "ls -ltr ~/workdir/${i}0_men8_pg_zw/namd/ | tail -n5"
   @ i = ${i} + 1
end

#Usage:for checking job errors
set i = 0
while ( ${i} <= 5 )
   echo "echo ${i}0_men8_pg_zw/namd/"
   echo "cat ~/workdir/${i}0_men8_pg_zw/namd/job.err"
   @ i = ${i} + 1
end
exit
