#!/bin/csh
#SBATCH --job-name=charmm
#SBATCH --partition=eng
#SBATCH --qos=nogpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --export=ALL
##SBATCH --mail-user=shf317@lehigh.edu
#SBATCH --mail-type=ALL
#SBATCH --time=36:00:00
#SBATCH --oversubscribe
# echo commands to stdout

set arr=('a' 'b' 'c' 'd')
#set arr=('b' 'c' 'd')

foreach i ($arr)
    echo "========================"
    echo 'Now processing chain ' $i ':'

    mkdir -p chain-${i}
    cp step1.2_chain-${i}.pdb chain-${i}/m1v2.pdb
    cp align.py mod-seg.py t1v2.ali chain-${i}/
    cd chain-${i}
    set char = `echo $i | awk '{ print toupper($0) }'`
    sed -i -e "s/:A/:${char}/g" align.py

    /home/shf317/bin/modeller9.21/bin/mod9.21 align.py
    /home/shf317/bin/modeller9.21/bin/mod9.21 mod-seg.py

    echo 'Modeller results for chain ' $i ':'
    tail -n20 mod-seg.log
    echo "========================"
    cd ..
end
