#!/bin/csh

set time = `date +"%y%m%d"`
set sysname = apo-nd-trpv2
set dirname = modeller-${sysname}-${time}
mkdir -p $dirname

set arr=('a' 'b' 'c' 'd')
set num=(1 2 3 4 5)
foreach i ($arr)
    foreach j ($num)
        cp chain-${i}/t1v2.BL000${j}0001.pdb $dirname/chain-${i}-${j}.pdb
    end
end

tar -czf ${dirname}.tar.gz $dirname
