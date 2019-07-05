#!/bin/csh


#Usage:for copy files to similar directories
set i = 0
set cnt = ( 650 650 650 650 650 650 )
set maxcnt = ( 750 750 750 750 750 750 )
set unit = 0
set unito = 0
set cpfile1 = "multi_densi_z.inp"
set cpfile2 = "run_densi.sh"

#while ( ${i} <= 9 )
#   @ cnt = ${i} * 10 + 1
#   @ maxcnt = ${i} * 10 + 10
#   @ unit = ${i} + 10
#   @ unitout = ${i} + 70
#   echo "sbatch --export=mol=tail,type=pgar,cnt=${cnt},maxcnt=${maxcnt},unit=${unit},unitout=${unitout} run_densi.sh"
#   @ i = ${i} + 1
#end

while ( ${i} <= 5 )
   @ unit = ${i} + 10
   @ unito = ${i} + 70
   @ j = ${i} + 1

#cd to the directory
   echo "cd ~/workdir/${i}0_men8_pg_zw/"
   if ( ${i} <= 4 ) then
      echo "cp ~/workdir/50_men8_pg_zw/${cpfile1} ~/workdir/${i}0_men8_pg_zw/"
      echo "cp ~/workdir/50_men8_pg_zw/${cpfile2} ~/workdir/${i}0_men8_pg_zw/"
   endif

#tail1-men8
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=tail1,type=men8,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#tail1-pgar
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=tail1,type=pgar,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#tail1-zwar
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=tail1,type=zwar,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#head-group-men8
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=mkhd,type=men8,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#glycerol backbone
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=glyb,type=pgzw,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#cla
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=cla,type=none,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#pot
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=pot,type=none,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#PO4
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=po4,type=pgzw,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
#Water
   set out = "sbatch --export=sysn=${i}0_men8_pg_zw,sys=${i}0_mkpgzw,mol=wat,type=none,cnt=$cnt[${j}],maxcnt=$maxcnt[${j}],unit=${unit},unito=${unito} run_densi.sh"
   echo ${out}
   @ i = ${i} + 1
end

exit
   
