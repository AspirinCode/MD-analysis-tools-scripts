
- script for writing snapshots along the trajectory:  
```
proc make_traj_time_movie_files {} {
set num [molinfo top get numframes]
for {set i 0} {$i < $num} {incr i} {
animate goto $i
set filename snap.[format "%04d" $i].ppm
render snapshot $filename
}
}
```

- script for writing rotating images:  
```
proc make_rotation_movie_files {} {
set frame 0
for {set i 0} {$i < 360} {incr i 2} {
set filename v2-340-1us-rtx.[format "%05d" $frame].ppm
render snapshot $filename
incr frame
rotate y by 2
}
}
```

- ffmpeg commands: 
```
ffmpeg -r 24 -i untitled.%05d.ppm -vcodec mpeg4 -b 2G test_junk.mp4
```

- script for RMS alignment:  
```
>>>set sel1 [atomselect 0 "backbone and resid 494 to 515 519 to 556"]
>>>set sel2 [atomselect 1 "backbone and resid 494 to 515 519 to 556”] 
>>>set transformation_matrix [measure fit $sel1 $sel2] 
{0.999958336353302 -0.009078864008188248 0.0009275606134906411 1.107559323310852} {0.009066441096365452 0.9998793005943298 0.012618061155080795 0.984622597694397} {-0.001042006304487586 -0.012609126046299934 0.9999199509620667 -5.127827167510986} {0.0 0.0 0.0 1.0} 
>>>set move_sel [atomselect 0 "all"] atomselect2 
>>>$move_sel move $transformation_matrix 
>>>$move_sel writepdb step5.1-transformed.pdb

```

- Auto-rotation:  
```
rotate [x | y | z] by <angle> <increment> -- smooth transition
Eg: rotate y by 1000 0.1
    Rotate stop
```

- Basid read-ins:  
```
color Display Background white
axes location Off

mol color Name
mol representation NewCartoon 0.300000 10.000000 4.100000 0
mol selection segname "PRO.*”
mol material Opaque
mol addrep 0
```

- Draw lines:  
```
draw delete all
draw materials off
draw color yellow
draw line  {    2.690    4.083  -26.750} {    1.676    3.852  -27.000} width     0
Draw color blue
draw point {   -4.469   -5.828  -31.898}
```

- Get the total charge:  
```
proc get_total_charge {{molid top}} {
eval "vecadd [[atomselect $molid all] get charge]"
}
```

- Periodic boundary show:  
```
pbc get #get the periodic boundary condition parameters
pbc box #draw the pbc box
pdb box -off #unshow the box
graphics 0 line {-4 -50 0} {-4 50 0} width 4 #draw the line on mol0

# In the case of no existing pbc box
vmd > set cell [pbc set {250 250 40000} -all]
vmd > pbc box -center origin -color black -width 1

# static pdc box
pbc box -center bb -color green # bb: bounding box
set box0 [pbc box_draw] # default color: blue
set box2 [pbc box_draw -center com -color red] # use center-of-mass as center

```

- Style set-up: 
```
for { set i 0 } { $i < $n } { incr i } {
mol modstyle 0 $i NewCartoon 0.300000 10.000000 4.100000 0 
}

```

- Operate on coordinates and turn them into one dcd file  
```
# load the structure and original set of coordinates 
mol load psf $start_psf pdb $start_pdb 
set whole [atomselect top all] 
set frame 0 
(loop begins here) 
   # add new frame to the trajectory, with coords copied from previous frame 
   animate dup frame $frame 0 
   incr frame 
   animate goto $frame 
   # modify coords of new frame 
   (do your own thing here) 
} 
# write the complete trajectory to disk 
animate write dcd $final_dcd beg 0 end $frame waitfor all 
```
- catdcd.sh: echo the catdcd command for large dcd file to concatenate together.

```
#!/bin/bash
printf "catdcd -o merged1.dcd "

for i in {1..250}
do
  printf "archglip_snap_${i}.dcd "
done
```
