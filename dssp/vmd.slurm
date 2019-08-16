#!/bin/sh
#SBATCH --job-name=vmd
#SBATCH --partition=eng
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --mem=50gb
#SBATCH --ntasks-per-node=10
#SBATCH --export=ALL
##SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --time=4:00:00
#SBATCH --oversubscribe

# We call for 10 nodes because of the memory requirement

module load vmd #/1.9.3
vmd -dispdev text -eofexit < write_pdb.tcl > write_pdb.log
