
In VMD:
```
vmd -dispdev text ../step5.1_assembly.psf
>>> aminate read dcd 1frame.dcd
>>> set a1 [atomselect 0 "protein"]
>>> $a1 writepdb output.pdb
>>> exit 

vmd -dispdev text step5_assembly.pdb
>>> set a1 [atomselect 0 "protein"]
>>> $a1 writepdb prot-only.pdb
>>> exit
```

Go to the XSSP folder:
```
./mkdssp -i initial-trpv2.pdb -o initial-trpv2.dssp
```

Delete the first 28 rows of DSSP output:
```
sed '1,28d' initial-trpv2.dssp > initialv2-dataonly.dssp
```

Print only the 17th character in each line:
```
cut -c17-17 initialv2-dataonly.dssp > initialv2-extr.dssp
```

Feed into python script.

```
import numpy as np

with open('test-text.dssp', 'r') as f:
    lines = f.readlines()

dssp_dict = {
    "H": 1, # alpha helix 4-12
    "B": 2, # isolated beta-bridge 
    "E": 3, # strand
    "G": 4, # 3-10 helix
    "I": 5, # pi helix
    "T": 6, # turn
    "S": 7  # bend
}

dssp = np.zeros(len(lines))
i = 0
for line in lines:
    line = line.split()
    if line != []:
        dssp[i] = dssp_dict[line[0]]
    i += 1

print(dssp)
>>> array([0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 6., 0., 1., 1., 1., 1., 1., 1.])
```

Furthere processing to get more frames to form a time trajectory.
