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
egrep "mid-|sampled" hole_out.txt > hole_out.tsv
# plot tsv
```
3. A colored dot surface and visualize in VMD:  
3.1 Use sph_process
```
sph_process -dotden 15 -color hole_out.sph dotsurface.qpt

# -dotden: dot density on the surface;
# -color: colored surface;
#       Red: pore radius is too tight for a water molecule;
#       Green: room for a single water;
#       Blue: radius is double the minimum for a single water.
# dotsurface.qpt can be displayed in Quanta, to use in VMD,
# need to use qpt_conv to convert.
```
3.2 Convert to VMD format  
`qpt_conv`: interactive job, take '.qpt' extension file e.g. dotsurface.qpt as input, choose VMD and others can be default;
The output is "dotsurface.vmd_plot", which can be used in VMD by `source dotsurface.vmd_plot`. This is a VMD configuration file. 

4. Triangulated surface and visualize in VMD: 
```
sph_process -sos -dotden 15 -color hole_out.sph solid_surface.sos
sos_triangle -s < solid_surface.sos > solid_surface.vmd_plot 
```
Then in terminal type `vmd hetatm-w.pdb` to open PDB file of protein and open Tk Console to type `source solid_surface.vmd_plot` or `source dotsurface.vmd_plot`. 


### Reference links  
- Optional cards for HOLE: http://www.holeprogram.org/doc/old/hole_d03.html#card_may 
- Detailed old version documentation of HOLE: http://www.holeprogram.org/doc/old/index.html#contents 
