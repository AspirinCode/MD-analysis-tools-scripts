#!/bin/csh
#SBATCH --job-name=charmm
#SBATCH --partition=lts
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
##SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --time=12:00:00
#SBATCH --oversubscribe
# echo commands to stdout

set a1 = 50_men8_pg_zw
set a2 = 40_men8_pg_zw
set a3 = 30_men8_pg_zw
set a4 = 20_men8_pg_zw
set a5 = 10_men8_pg_zw
set a6 = 00_men8_pg_zw
set a7 = 30_mkol_pg_zw
set a8 = 30_men8_mkol_pg_zw
set a9 = ar3-00men8
set a10 = ar3-30men8
set a11 = ar3-50men8
set a12 =  ar3-30mkol
set a13 = ar3-30mix

set list = ( $a1 $a2 $a3 $a4 $a5 $a6 $a7 $a8 $a9 $a10 $a11 $a12 $a13 )
set cntmin = ( 1001 801 801 801 801 801 801 801 801 1001 1001 1001 1001 )
set cntmax = ( 1200 1000 1000 1000 1000 1000 1000 1000 1000 1200 1200 1200 1200 )
# foreach also works

set inpfile = /home/shf317/workdir2/old_dir/shf317/50_men8_pg_zw/system_size/system_size.inp

set i = 1
while ( $i <= 13 )
    echo "============================"
    echo "Now processing directory: "
    echo ${list[$i]}
    echo "============================"

    if ( $i != 1) then
        cd /home/shf317/workdir2/old_dir/shf317/${list[$i]}
        mkdir -p system_size
        cp ${inpfile} system_size/
    endif
        ${charmm} local=${LOCAL} sysn=${list[$i]} cntmin=${cntmin[$i]} cntmax=${cntmax[$i]} < system_size/system_size.inp > /dev/null

    @ i += 1
end

  cp ${LOCAL}/* /home/shf317/workdir2/old_dir/shf317/analysis/sys_size 
