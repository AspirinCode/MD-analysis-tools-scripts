#!/bin/csh


#Usage:for sbatch jobs with slightly varying parameters
set i = 1
set cnt = 101
set maxcnt = 200
set unit = 12
set unito = 62
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

# A list of variables to use
set binsize = ( 0.1 0.3 0.7 1.0 )
set j = 0
while ( ${i} <= 3 )
   @ j = 1
   while ( ${j} <= 4 )
       #glycerol backbone
       set out = "sbatch --export=sysn=00_men8_pg_zw,sys=00_mkpgzw,mol=glyb,type=pgzw,cnt=101,maxcnt=200,unit=${unit},unito=${unito},binsize=$binsize[${j}] run_densi${i}.sh"
       echo ${out}
       @ j = ${j} + 1
   end
   @ i = ${i} + 1
end

exit
