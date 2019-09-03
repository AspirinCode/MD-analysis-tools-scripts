from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

env.io.atom_files_directory = ['.', '.']

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_atoms(self):
        # Two residue ranges (both will be refined simultaneously)
        return selection(self.residue_range('487:', '515:') ,
                         self.residue_range('342:', '354:') ,
                         self.residue_range('619:', '624:'))
    #def select_loop_atoms(self):
    #    return selection(self.residue_range('561:', '588:'))

a = MyLoop(env,
           alnfile  = 'two-alignment.ali',      # alignment filename
           knowns   = 'rhv2',               # codes of the templates
           sequence = 'shv2',               # code of the target
           loop_assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model

a.loop.starting_model = 1           # First loop model
a.loop.ending_model   = 2           # Last loop model

a.make()                            # do modeling and loop refinement


#Example: examples/automodel/model-multichain-sym.py
# Comparative modeling by the automodel class
#
# Demonstrates how to build multi-chain models, and symmetry restraints
#
from modeller import *
from modeller.automodel import * # Load the automodel class
log.verbose()
# Override the ’special_restraints’ and ’user_after_single_model’ methods:
class MyModel(automodel):
    def special_restraints(self, aln):
        # Constrain the A and B chains to be identical (but only restrain
        # the C-alpha atoms, to reduce the number of interatomic distances
        # that need to be calculated):
        s1 = selection(self.chains[’A’]).only_atom_types(’CA’)
        s2 = selection(self.chains[’B’]).only_atom_types(’CA’)
        self.restraints.symmetry.append(symmetry(s1, s2, 1.0))
    def user_after_single_model(self):
        # Report on symmetry violations greater than 1A after building
        # each model:
        self.restraints.symmetry.report(1.0)

env = environ()
# directories for input atom files
env.io.atom_files_directory = [’.’, ’../atom_files’]
# Be sure to use ’MyModel’ rather than ’automodel’ here!
a = MyModel(env,
            alnfile = ’twochain.ali’ , # alignment filename
            knowns = ’2abx’, # codes of the templates
            sequence = ’1hc9’) # code of the target
a.starting_model= 1 # index of the first model
a.ending_model = 1  # index of the last model
                    # (determines how many models to calculate)
a.make() # do comparative modeling
