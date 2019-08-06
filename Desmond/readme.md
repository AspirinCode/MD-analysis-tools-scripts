# Build Desmond file  


# Validation: dms-validate and fix

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
>>> {
  size=14
  time=2640 {
    ANTON2_CHECKPOINT_GC_BAROSTAT[496 x unsigned char]= ...
    ANTON2_CHECKPOINT_GC_THERMOSTAT[768 x unsigned char]= ...
    ANTON2_CHECKPOINT_ITEMS[56 x unsigned char]= ...
    BOX[3 x uint32_t]= 422418944 422418944 457394432
    CHARGESCALE[1 x double]= 2.048
    CHEMICALTIME[1 x double]= 2640
    DRUDEMOMENTUMSHIFT[1 x int32_t]= 0
    ENERGYSCALE[1 x double]= 4000
    FORCESCALE[1 x double]= 4000
    FORMAT[13 x char]= "ANTO..."
    INPUT_ARK[3539 x char]= "anto..."
    ISROGUE[1 x uint32_t]= 0
    KE2[3 x float]= 63628.836 63834.578 63829.852
    KE_RAW[3 x int32_t]= 95536949 95845864 95838771
    KE_RAW_GROUPS[3 x int32_t]= 95536949 95845864 95838771
    KIN_ENERGY[1 x float]= 377619.5
    MASSSCALE[1 x double]= 0.0023850860420650097
    MOMENTUM[1798086 x int32_t]= -3960077 -145638011 -95279856 -5977088 ...
    MOMENTUMSCALE[1 x double]= 2.5812096669940319
    POSITION[1798086 x int32_t]= -111456176 107209881 60722106 -113481160 ...
    POSITIONSCALE[1 x double]= 887.26584723149631
    PROCESSOR[9 x char]= "anto..."
    PROVENANCE[31 x char]= "anto..."
    STEP[1 x double]= 2640000
    TIMESCALE[1 x double]= 0.001
    TITLE[5 x char]= "ANTO..."
  }


# For the trajectory frames from the first successful jobstep:
fsdump --max=4 $RAW/system_name/workdir/000000/run.dtr

# Print system size from dtr trajectory:
fsdump --match=UNITCELL $RAW//workdir/000000/run.dtr

# For more options 
fsdump --help 

# Write the last frame to DMS file 
# An example to extract from the last checkpoint of a 10 ns run
dms-frame input.dms output.dms -t 10000 -i $workdir/000000/checkpoint.atr/
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
