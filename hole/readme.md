# HOLE2: detect pore radius  

HOLE2 program can be downloaded here: http://www.holeprogram.org/ 

## Pipeline  
1. Call `HOLE` program to do calculation: `hole < hole.inp > hole.out`;   
2. Plot the 2D graph of pore radius vs channel coordinate:
```
egrep "mid-|sampled" hole_out.txt > hole_out.tsv
# plot tsv
```
3. A colored dot surface and visualize in VMD:  
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
`qpt_conv`: interactive job, choose VMD and others can be default;
The output is "dotsurface.vmd_plot", which can be used in VMD by `source dotsurface.vmd_plot`. This is a VMD configuration file. 

4. Triangulated surface and visualize in VMD: 
```
sph_process -sos -dotden 15 -color hole_out.sph solid_surface.sos
sos_triangle -s < solid_surface.sos > solid_surface.vmd_plot 
```
