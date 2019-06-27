## Table of Content
1. [1D hydrophobic thickness](#1d-thick)
2. [2D hydrophobic thickness](#2d-thick)

## 1D hydrophobic thickness <a name="1d-thick"></a>
Do two centering process, first select a residue in the membrane to center it, then use the overall membrane center of mass to center it. This process is to avoid the case where the bottom leaflet is at the top of box, while top leaflet is at the bottom.

`1d_hydro_thick.inp` takes following arguments:
- sysname # for naming the file
- local # scratch directory
- cntmin # from which dcd to calculate the thickness
- cntmax # to which dcd to calcutalte the thickness

Command in the Slurm csh script:
```
${charmm} local=${LOCAL} sysname=ar3-30men8 cntmin=1 cntmax=1100 < 1d_hydro_thick.inp > /dev/null # 1d_hydro_thick.out
cp ${LOCAL}/* $SLURM_SUBMIT_DIR/analysis
```

## 2D hydrophobic thickness <a name="2d-thick"></a>

