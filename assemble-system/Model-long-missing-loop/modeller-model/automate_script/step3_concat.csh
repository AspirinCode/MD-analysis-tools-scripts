#!/bin/csh

set sysname = modeller-apo-nd-trpv2-190812
set outname = step3_concat.pdb
set chainid = ('a' 'b' 'c' 'd')

# set up the model IDs we like for each chain
set modelid = (4 1 3 2)

set cnt = 1
rm $outname # Clear up the folder

foreach i ($chainid)
    set uppercase = `echo $i | awk '{ print toupper($0) }'`
    echo "Working on Chain " $uppercase

    #add chain ID to each chain, Modeller depletes them
    sed -e "s/./${uppercase}/22" $sysname/chain-${i}-${modelid[$cnt]}.pdb > junk.pdb

    #delete first 4 rows of REMARKs etc;
    sed -e '1,4d' < junk.pdb >> $outname

    #delete the END of first 3 chains but keep last one
    if ( $cnt < 3 ) then
        sed -i -e '$d' $outname
    endif
    @ cnt += 1
end

rm junk.pdb # Clean up
echo "Job finished"

exit
