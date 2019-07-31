# This script is for align a PDB model and a template
# Given a peptide of 650 aa, it takes several min to finish the alignment
# Note: the 't1v2' should appear in 't1v2.ali' file

from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='m1v2', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='m1v2', atom_files='m1v2.pdb')
aln.append(file='t1v2.ali', align_codes='t1v2')
aln.align2d()
aln.write(file='two-alignment.ali', alignment_format='PIR')
aln.write(file='two-alignment.pap', alignment_format='PAP')
