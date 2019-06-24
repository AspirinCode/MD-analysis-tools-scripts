# Scc analysis

Scc measure the orderedness of lipid aliphatic chains by calculation the fluctuation of C-C axis and its angle regarding the membrane norm.


## Steps  
- Process the trajectories to make them consecutive;  
- Prepare `scc-c?.inp`, `scd-c?.inp` and slurm scripts for job;  
- Make directories: `scc_data`, `scd_data`;  
- Lauch the job;  
- Use Jupyter notebook to analyze the data and save the figure;  



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

We use `dcd-seq.csh` file to make the dcd files sequential so that the `Correl` module in CHARMM can work with the dcd files correctyly.

"dcd-seq.csh":
```
#!/bin/csh
#The file is for dumping and loading the correct firstTimeStep of each dcd file

set n = 801
set first = 5000
while ( $n <= 1000 )

    # Get the header of the DCD file and calculate should-be values;
    dumpdcd step7.${n}.dcd > temp.header
    @ first = 500000 * ( $n - 801 ) + 5000
    
    # Get the first column value of 2nd row
    set orig = `awk 'FNR == 2 {print}' temp.header | awk '{print $1}'`
    
    # Edit the value
    sed -i "2s/${orig}/${first}/" temp.header
    
    # Load into DCD files
    loaddcd step7.${n}.dcd < temp.header
    @ n += 1
end

```
