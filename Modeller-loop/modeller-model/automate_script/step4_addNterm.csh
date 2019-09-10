set initf = step3.1_addCBD.pdb
set inpf =  TRPV2_30uMCBD_ND_UPenn_State1_24K_C4_3.4A_FINAL.pdb
set beg = ( 162 5231 10300 15369 )
set end = ( 297 5366 10435 15504 )

cp $initf step4_addNterm.pdb
sed -i -e '$d' step4_addNterm.pdb

set chain = ( E F G H )
foreach i ( 1 2 3 4 )
    echo "${beg[$i]},${end[$i]}p $inpf"
    sed -n ${beg[$i]},${end[$i]}p $inpf > temp.pdb
    sed -e "s/./${chain[$i]}/22" temp.pdb >> step4_addNterm.pdb
    echo "TER" >> step4_addNterm.pdb
end

# Clean-up robot
rm temp.pdb
echo "END" >> step4_addNterm.pdb
