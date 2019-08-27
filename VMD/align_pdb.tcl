set prefix apo-state1

# We have files:
# apo-state1-0.pdb, apo-state1-1.pdb, ..., apo-state1-9.pdb;
# We want to orient all other pdb files to apo-state1-0.pdb

for { set i 0 } { $i <= 9 } {incr i 1} {
    mol new $prefix-$i.pdb
    if {$i == 0 } {
        set sel1 [atomselect $i "backbone"]
    } else {
        set sel2 [atomselect $i "backbone"]
        set transformation_matrix [measure fit $sel2 $sel1]
        set move_sel [atomselect $i "all"]
        $move_sel move $transformation_matrix
        $move_sel writepdb tf-$prefix-$i.pdb
    }
}
