#!/bin/sh
#Input: step1_preprocess.tcl, PDB file

#Truncate unnecessary residues and write PDB file for each chain;
vmd -dispdev text -eofexit < step1_preprocess.tcl > step1_preprocess.log
