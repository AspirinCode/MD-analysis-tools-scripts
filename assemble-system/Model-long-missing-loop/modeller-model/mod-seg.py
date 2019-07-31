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
