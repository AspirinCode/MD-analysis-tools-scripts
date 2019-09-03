#Example: examples/automodel/model-addrsr.py
# Addition of restraints to the default ones
from modeller import *
from modeller.automodel import * # Load the automodel class
log.verbose()
env = environ()
# directories for input atom files
env.io.atom_files_directory = [’.’, ’../atom_files’]
class MyModel(automodel):
  def special_restraints(self, aln):
    rsr = self.restraints
    at = self.atoms
#   Add some restraints from a file:
#   rsr.append(file=’my_rsrs1.rsr’)
#   Residues 20 through 30 should be an alpha helix:
    rsr.add(secondary_structure.alpha(self.residue_range(’20:’, ’30:’)))
# Two beta-strands:
    rsr.add(secondary_structure.strand(self.residue_range(’1:’, ’6:’)))
    rsr.add(secondary_structure.strand(self.residue_range(’9:’, ’14:’)))
# An anti-parallel sheet composed of the two strands:
    rsr.add(secondary_structure.sheet(at[’N:1’], at[’O:14’],
            sheet_h_bonds=-5))
# Use the following instead for a *parallel* sheet:
# rsr.add(secondary_structure.sheet(at[’N:1’], at[’O:9’],
# sheet_h_bonds=5))
# Restrain the specified CA-CA distance to 10 angstroms (st. dev.=0.1)
# Use a harmonic potential and X-Y distance group.
    rsr.add(forms.gaussian(group=physical.xy_distance,
            feature=features.distance(at[’CA:35’],
                                      at[’CA:40’]),
                                      mean=10.0, stdev=0.1))

a = MyModel(env,
            alnfile = ’alignment.ali’, # alignment filename
            knowns = ’5fd1’, # codes of the templates
            sequence = ’1fdx’) # code of the target
a.starting_model= 1 # index of the first model
a.ending_model = 1 # index of the last model

# (determines how many models to calculate)
a.make() # do comparative modeling
