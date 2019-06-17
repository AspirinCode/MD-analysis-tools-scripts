# Build Desmond file  


# dms-validate and fix


# Process Desmond trajectory 

- Retrieve trajectories  
Login to Kollman account: shashaf@kollman.psc.edu   
Type following commands:
```shell
  module load vmd/1.9
  vmd -dispdev text initsys.para.dms
  vmd > animate read dtr workdir.1/run.stk waitfor all
  vmd > molinfo 0 get numframes
  vmd > 41
  vmd > animate write dcd v2-cbd-100ns.dcd beg 0 end 41 skip 20

```

- Read above converted trajectory in CHARMM script  
The important point is this read in grammar;

```fortran

```

- Processing
The same as others.
