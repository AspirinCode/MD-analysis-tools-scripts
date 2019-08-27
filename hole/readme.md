# HOLE2: detect pore radius  

## Download and Installation  
HOLE2 program can be downloaded here: http://www.holeprogram.org/. A variety of versions are available. MacOS version is not avaible though. 

First untar the compressed file, then export the PATH for hole2/exe/. In '.bashrc' file, add this line `PATH=$PATH:~/path-to-hole2/exe` and source the file. Otherwise, we need to type the full path for /exe directory every time. 


## Pipeline  
1. Call `HOLE` program to do calculation: `hole < hole.inp > hole.out`;   
```
! example input file run on Arseniev's gramicidin structure
! first cards which must be included for HOLE to work
! note that HOLE input is case insensitive (except file names)
coord hetatm-w.pdb           ! Co-ordinates in pdb format
radius ~/bin/hole2/rad/simple.rad   ! Use simple AMBER vdw radii
                ! n.b. can use ~ in hole
!
! now optional cards
cvect  0 0 1
cpoint 0 0 -13
sphpdb hole_out.sph             ! pdb format output of hole sphere centre info
                ! (for use in sph_process program)
endrad 5.           ! This is the pore radius that is taken
                                ! as where channel ends. 5.0 Angstroms is good
                                ! for a narrow channel
```

2. Plot the 2D graph of pore radius vs channel coordinate:
```
egrep "mid-|sampled" hole.out > hole_out.tsv
# plot tsv
```
3. A colored dot surface and visualize in VMD:  
3.1 Use sph_process
```
sph_process -dotden 15 -color hole_out.sph dotsurface.qpt
```
 `-dotden`: dot density on the surface;  
 `-color`: colored surface;  red: pore radius is too tight for a water molecule; green: room for a single water; blue: radius is double the minimum for a single water.  
 dotsurface.qpt can be displayed in Quanta.

3.2 Convert to VMD format  
`qpt_conv`: interactive job, take '.qpt' extension file e.g. dotsurface.qpt as input, choose VMD and others can be default;
The output is "dotsurface.vmd_plot", which can be used in VMD by `source dotsurface.vmd_plot`. This is a VMD configuration file. 

4. Triangulated surface and visualize in VMD: 
```
sph_process -sos -dotden 15 -color hole_out.sph solid_surface.sos
sos_triangle -s < solid_surface.sos > solid_surface.vmd_plot 
```
Then in terminal type `vmd hetatm-w.pdb` to open PDB file of protein and open Tk Console to type `source solid_surface.vmd_plot` or `source dotsurface.vmd_plot`. 

## Trajectory processing pipeline  
1. Write protein-only pdb from the DCD trajectory;  
Using `vmd -dispdev text -eofexit < make_traj_pdb.tcl`:
```
mol new ../step5.2_pene_resolved.psf
animate read dcd rct-100frm-v2-apo-vanilla-300k-1001-1500ns.dcd beg 95
set a1 [atomselect top "protein"]

# Set up a procedure
proc make_traj_pdb {} {
    set num [molinfo top get numframes]
    for {set i 0} {$i < $num} {incr i} {
        set a1 [atomselect top "protein"]
        animate goto $i
        #set filename snap.[format "%04d" $i].ppm
        set filename pdb_snap/apo-state1-[format "%d" $i].pdb
        #render snapshot $filename
        $a1 writepdb $filename
    }
}

make_traj_pdb
```
2. RMS align the structures with a reference: using `vmd -e align-pdb.tcl`. The tcl script is shown here: 
```
set prefix apo-state1

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
```  
3. Use an template HOLE2 input: hole-batch.inp. 
```
coord pdbname
radius ~/bin/hole2/rad/simple.rad   ! Use simple AMBER vdw radii
                ! n.b. can use ~ in hole
!
! now optional cards
cvect  0 0 1
cpoint 0 0 -24
sphpdb output.sph             ! pdb format output of hole sphere centre info
                ! (for use in sph_process program)
endrad 5.           ! This is the pore radius that is taken
                                ! as where channel ends. 5.0 Angstroms is good
                                ! for a narrow channel
```
Use `csh run_hole.csh` to run the batch job:
```
#!/usr/bin/csh

set i = 0
while ( $i <= 9 )
    sed -e "s/pdbname/tf-apo-state1-${i}\.pdb/g" -e "s/output/hole_${i}/g" hole-batch.inp > hole-temp.inp
    hole < hole-temp.inp > hole_${i}.out
    egrep "mid-|sampled" hole_${i}.out > hole_${i}.csv
    sph_process -dotden 15 -color hole_${i}.sph dotsurface_${i}.qpt
    sph_process -sos -dotden 15 -color hole_${i}.sph solid_surface_temp.sos
    sos_triangle -s < solid_surface_temp.sos > solid_surface_${i}.vmd_plot
    @ i += 1
end
```
4. Download the results for plotting and visualization. 
Use `csh run_achieve.csh`
```
#!/usr/bin/csh

set folder = hole-result
mkdir -p $folder

set i = 0
while ( $i <= 9 )
    mv hole_$i.csv $folder
    mv solid_surface_$i.vmd_plot $folder
    @ i += 1
end

tar -czf $folder.tar.gz $folder
```
5. Plot the csv using `python plot.py`. 
```
import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 10):
    z, radius = np.loadtxt(f"hole-result/hole_{i}.csv", unpack=True, usecols=(0,1))
    plt.plot(z, radius, label=f"pdb_{i}")

plt.legend()
plt.show()
```

### Reference links  
- Optional cards for HOLE: http://www.holeprogram.org/doc/old/hole_d03.html#card_may 
- Detailed old version documentation of HOLE: http://www.holeprogram.org/doc/old/index.html#contents 
