#!/bin/sh

#Truncate unnecessary residues
vmd -dispdev text -eofexit < step1_preprocess.tcl > step1_preprocess.log
