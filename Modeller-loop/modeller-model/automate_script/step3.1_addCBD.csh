#!/bin/csh
set outname = step3.1_addCBD.pdb
set inpf = TRPV2_30uMCBD_ND_UPenn_State2_36K_C4_3.2A_FINAL.pdb

rm $outname
cp step3_concat.pdb $outname

echo "Delete END"
sed -i -e '$d' $outname

echo "Mutate HSD to HIS"
sed -i -e "s/HSD/HIS/g" $outname

grep CBD $inpf >> $outname
echo "END" >> $outname

echo "Job finished."

exit
