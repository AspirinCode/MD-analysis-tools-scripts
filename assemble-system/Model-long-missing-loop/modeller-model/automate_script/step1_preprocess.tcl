mol new TRPV2_Apo_ND_UPenn_State1_42K_C4_3.86A_Final.pdb
set prot [atomselect top "resid 75 to 719"]
$prot writepdb step1.1_truncate_nterm.pdb
set prota [atomselect top "chain A and resid 75 to 719"]
$prota writepdb step1.2_chain-a.pdb
set protb [atomselect top "chain B and resid 75 to 719"]
$protb writepdb step1.2_chain-b.pdb
set protc [atomselect top "chain C and resid 75 to 719"]
$protc writepdb step1.2_chain-c.pdb
set protd [atomselect top "chain D and resid 75 to 719"]
$protd writepdb step1.2_chain-d.pdb
