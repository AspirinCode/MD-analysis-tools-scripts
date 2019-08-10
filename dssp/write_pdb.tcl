# Read PSF
mol new ../../step5.1_assembly.psf type psf

# Read DCD file
animate read dcd rct-v2-cbd-500ns.dcd waitfor all

# Loop over frames to write PDB file for protein only
set numframe [molinfo 0 get numframes]

# Every 4 frames 
for { set i 0 } { $i < $numframe } { incr i 4 } {
    animate goto $i
    set prot [atomselect 0 "protein"]
    $prot writepdb pdb_dir/frame$i.pdb
}
