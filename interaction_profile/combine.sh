#!/bin/csh
#SBATCH --job-name="sasa"
#SBATCH --partition=enge
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
#SBATCH -t 48:00:00
# echo commands to stdout 
 
module load anaconda/python2

if ( -e ./${sys}/${type}_${sys}.dat ) rm -f ./${sys}/${type}_${sys}.dat

  set resid = ${ir}
  while ( ${resid} <= ${fr} )
  ############################# Prepare initial data
  mv ${sys}/${type}_${sys}_${resid}_in.dat  ${sys}/${resid}_in.dat
  mv ${sys}/${type}_${sys}_${resid}_out.dat ${sys}/${resid}_out.dat

  paste ${sys}/seq.dat ${sys}/${resid}_in.dat  > ${sys}/${type}_${sys}_${resid}_in.dat
  paste ${sys}/seq.dat ${sys}/${resid}_out.dat > ${sys}/${type}_${sys}_${resid}_out.dat

  rm ${sys}/${resid}_in.dat
  rm ${sys}/${resid}_out.dat
  #############################

  join ./${sys}/${type}_${sys}_${resid}_in.dat ./${sys}/${type}_${sys}_${resid}_out.dat | awk '{print $1, $2, $3, $4, $5, $6, $7, $8, $9, $11}' > ./${sys}/${type}_${sys}_${resid}.dat
  python average_sd_om.py ${sys} ${type}_${sys} ${resid} >> ./${sys}/${type}_${sys}.dat

  @ resid += 1
  end


   endif
