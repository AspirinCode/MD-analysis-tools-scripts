# Build Desmond file  


# dms-validate and fix

```
garden load v2software/1.34.0c7/bin
garden load msys/1.7.213c7/bin

# This command outputs all the validation results
dms-validate initsys.para.dms --all

# Following command is used to fix the Oxygen weight problem;
dms-fix-mass pre-fix-initsys.dms -o initsys.para.dms
```

# Work with DMS system  
Check the simulation time:  
```
# Load the latest version of msys software;
garden load msys/1.7.213c7/bin

fsdump --match=time workdir.1/000001/run.dtr
>>> ...  time=98880 {
  }
  time=99120 {
  }
  time=99360 {
  }
  time=99600 {
  }
  time=99840 {
  }
  time=100080 {
  }
}
``` 

Look at other fields and data in every frame in a frameset:  
```
# Look at the checkpoints taken during the first successful job step:
# Option --max=4 means "show only the first 4 elements of any array".
fsdump --max=4 $RAW/system_name/workdir/000000/checkpoint.atr

# For the trajectory frames from the first successful jobstep:
fsdump --max=4 $RAW/system_name/workdir/000000/run.dtr

# Print system size from dtr trajectory:
fsdump --match=UNITCELL $RAW//workdir/000000/run.dtr

# For more options 
fsdump --help
```


# Process Desmond trajectory 

- Retrieve trajectories  
Login to Kollman account: user_id@kollman.psc.edu   
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
