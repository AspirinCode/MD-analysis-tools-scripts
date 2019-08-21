#!/bin/csh

# This script is for collecting files for assembling the system 
# once we got the step3_packing result

set SOURCE = /home/shf317/workdir2/trpv2/v2-apo-nd-vanilla
cp $SOURCE/run_charmm.sh $SOURCE/step5.1_rename.inp $SOURCE/step5.2_pene_resolved.inp $SOURCE/step5.2_input.inp ./
cp $SOURCE/step4*inp ./
cp $SOURCE/step5_assembly.inp ./
cp $SOURCE/step5_input.inp $SOURCE/step5_input*str ./
cp $SOURCE/water_tmp.crd ./
cp $SOURCE/pentest.py ./
