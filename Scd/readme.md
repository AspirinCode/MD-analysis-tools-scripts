# Scd calculation


## Trajectory data pre-processing  
Trajectory file header is shown by `dumpdcd` command.  

```
[shf317@sol namd]$ dumpdcd step7.999.dcd
100
5000
5000
500000
0
0
0
0
0
0.040910
1
0
0
0
0
0
0
0
0
24
```

We use `dcd_seq.csh` file to make the dcd files sequential so that the `Correl` module in CHARMM can work with the dcd files correctyly.
