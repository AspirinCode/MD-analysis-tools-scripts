readpsf ../../step5.1_assembly.psf
animate read dcd ../rct-v2-lig-300k-500ns.dcd waitfor all
set numframe [molinfo 0 get numframes]
#set totframe [ expr { $numframe / 4 } ]
for { set i 0 } { $i < $numframe } { incr i 4 } {
    animate goto $i
    set prot [atomselect 0 "protein"]
    $prot writepdb pdb_dir/frame$i.pdb
}
