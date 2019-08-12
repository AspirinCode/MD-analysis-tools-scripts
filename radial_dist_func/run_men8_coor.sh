#!/bin/csh
#SBATCH --job-name=charmm
#SBATCH --partition=lts
#SBATCH --qos=nogpu 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH --mail-user=shaalltime@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --time=12:00:00
#SBATCH --oversubscribe
# echo commands to stdout 

#charmm="/home/shf317/bin/c40a1_ifort"
set charmm = "/home/shf317/bin/charmm"
set LOCAL = /scratch/${USER}/${SLURM_JOBID}

cd /home/shf317/workdir2/old_dir/shf317/analysis/men8_coordir

set i = 2
while ( $i <= 5 )
    mkdir -p ${i}0-men8
    
    cd /home/shf317/workdir2/old_dir/shf317/${i}0_men8_pg_zw/ 
    cp /home/shf317/workdir2/old_dir/shf317/analysis/men8_coordir/men8_coor.inp ./
    
    if ( $i == 5 ) then 
        set cntmin = 1101
        set cntmax = 1200
    else 
        set cntmin = 901
        set cntmax = 1000
    endif
    
    ${charmm} fname=${i}0-men8 cntmin=${cntmin} cntmax=${cntmax} < men8_coor.inp > /dev/null
    @ i += 1

    #break
    cd /home/shf317/workdir2/old_dir/shf317/analysis/men8_coordir
end 

