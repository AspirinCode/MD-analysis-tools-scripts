# Jupyter notebook use on Slurm 

Use following script:  
  If you want to access as many files as possible, it is better to run this script on the root path.   
  `sbatch jupyter.slurm`  
  
"jupyter.slurm":  
```
#!/bin/bash
#SBATCH --partition=lts
#SBATCH --nodes=1
#SBATCH --ntasks-per-node 1
#SBATCH --time=3:00:00
#SBATCH --job-name=jupyter-notebook
#SBATCH --output=jupyter-notebook-%J.log

# Load Python module
module load anaconda/python3

# get tunneling info
export XDG_RUNTIME_DIR=""

ipnport=$(shuf -i8000-9999 -n1)
ipnip=$(hostname -s)

## print tunneling instructions to jupyter-log-{jobid}.txt
echo -e "
    Copy/Paste this in your local terminal to ssh tunnel with remote
    -----------------------------------------------------------------
    ssh -N -f -L $ipnport:$ipnip:$ipnport ${USER}@sol.cc.lehigh.edu
    -----------------------------------------------------------------

    Then open a browser on your local machine to the following address
    ------------------------------------------------------------------
    localhost:$ipnport
    ------------------------------------------------------------------
    and use the token that appears below to login.

    OR replace "$ipnip" in the address below with "localhost" and copy
    to your local browser.
    "

#jupyter notebook --no-browser --port=$ipnport --ip=$ipnip
jupyter lab --port=$ipnport --ip=$ipnip --no-browser
```
