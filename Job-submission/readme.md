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

### Jupyter notebook Table of Content:
```
# Table of contents
1. [Introduction](#introduction)
2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)

## This is the introduction <a name="introduction"></a>
Some introduction text, formatted in heading 2 style

## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text
```
