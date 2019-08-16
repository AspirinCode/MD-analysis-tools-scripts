#!/bin/csh
#SBATCH --job-name=dssp
#SBATCH --partition=eng
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
##SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --time=6:00:00
#SBATCH --oversubscribe

python plot-dssp.py
