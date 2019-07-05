#!/bin/csh
#./sizejob.csh > size.ls

# Usage: for measuring the box size;

set i = 0
set cpfile1 = 'boxsize.py'
set cnt = ( 500 500 500 579 569 527 )
set j = 0

while ( ${i} <= 5 )
  echo "cd ~/workdir/${i}0_men8_pg_zw/namd"
  if ( ${i} <= 4 ) then
      echo "cp ~/workdir/50_men8_pg_zw/namd/${cpfile1} ~/workdir/${i}0_men8_pg_zw/namd/"
  endif
  @ j = ${i} + 1
  set out = "python boxsize.py $cnt[${j}] ~/workdir/analysis/arch_mem/${i}0_men8_size.plo"
  echo ${out}
  @ i = ${i} + 1
end
