### For job submission files:


`namd-slurm.sh` contains the information for submitting NAMD job on SOL cluster using Slurm job scheduler. It submits job automatically after the first one is finished.

### Dcd renaming:  
```
# NAMD output is usually in "step7.x_production.dcd" format;
# wants to convert to "step7.x.dcd" format;

#!/bin/csh

set i = 1035
while ( ${i} <= 1200 )
        echo "mv step7.${i}_production.dcd step7.${i}.dcd"
        #echo "rm step7.${i}.dcd"
        @ i += 1
end
```
