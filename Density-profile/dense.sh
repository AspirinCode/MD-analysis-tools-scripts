!/bin/bash
#SBATCH --job-name=DENSITY
#SBATCH --partition=imlab
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH --output=job.out
#SBATCH --error=job.err
##SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --time=02:00:00
#SBATCH --oversubscribe
# echo commands to stdout

#charmm="/home/shf317/bin/c40a1_ifort"
charmm="/home/shf317/bin/charmm"

cd $SLURM_SUBMIT_DIR

# run OpenMP program
#for i in 0 1 2 3 5
#do
#  cd /home/shf317/workdir/${i}0_men8_pg_zw/
#  cp /home/shf317/workdir/50_men8_pg_zw/sa_lipid.inp ./
##  mkdir analysis
#  ${charmm} sysname=${i}0_mkpgzw ns=100  < sa_lipid.inp > /dev/null
#done

#cd /home/shf317/workdir/${sysn}/
#cp /home/shf317/workdir/50_men8_pg_zw/multi_densi_z.inp ./
#charmm sysn=${sysn} sys=${sys} mol=${mol} type=${type} cnt=${cnt} maxcnt=${maxcnt} unit=${unit} unito=${unito} binsize=${binsize} < multi_densi_z.inp > /dev/null
charmm sysn=${sysn} sys=${sys} mol=${mol} type=${type} cnt=${cnt} maxcnt=${maxcnt} unit=${unit} unito=${unito} < multi_densi_z.inp > /dev/null
