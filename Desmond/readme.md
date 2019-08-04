# Build Desmond file  


# dms-validate and fix


# Process Desmond trajectory 

- Retrieve trajectories  
Login to Kollman account: shashaf@kollman.psc.edu   
Type following commands:
```shell
  module load vmd/1.9
  vmd -dispdev text initsys.para.dms
  
  # This step can be very slow because of waitfor all
  vmd > animate read dtr workdir.1/run.stk waitfor all
  # An alternative could be: > animate read dtr workdir.1/run.stk beg 4168 end 6250 waitfor all
  
  # vmd > read file_type filename [beg nb] [end ne ] [skip ns] [waitfor nw] [molecule_number] 
  # We can also specify begin from which frame to reduce the load;
  # eg. vmd > animate read dtr workdir.1/run.stk beg 4168 waitfor all
  
  vmd > molinfo 0 get numframes
  vmd > 41
  vmd > animate delete beg 0 end 1 skip 1 0
  vmd > animate write dcd v2-cbd-100ns.dcd beg 0 end 40 skip 20

```

- Read above converted trajectory in CHARMM script  
The important point is this read in grammar;

```fortran
   traj firstu 11 nunit 1 skip @skip begin 0 stop @nfile iwrite 22
   !traj iread 11 begin 0 stop 417 iwrite 22 nfile 1
   !traj iread 11 iwrite 22 nread 1 begin @start skip @skip
```

- Processing
The same as others.
