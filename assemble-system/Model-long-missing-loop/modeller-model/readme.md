## Use Modeller & other tools to model the loop  


## 0. Preprocess
- Use VMD to write PDB file for each chain for multi-subunit protein;  
Because currently I am not able to figure out multimeric protein loop modeling in Modeller;

## 1. Modeller  
### 1.1 Align sequence and PDB structure sequence  
Use `/align/align.py` to generate the sequence alignment `two-component.ali`;  
This is going to guide the `loopmodel` module what residues to add for missing loops. Also it would be good to name both the PDB and the sequence `ali` file to both four-letter name, eg., "m1v2", "t1v2". Not sure if otherwise Modeller still works.  

Code snippet:  
```
from modeller import *
env = environ()
aln = alignment(env)
mdl = model(env, file='m1v2', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='m1v2', atom_files='m1v2.pdb')
aln.append(file='t1v2.ali', align_codes='t1v2')
aln.align2d()
aln.write(file='two-alignment.ali', alignment_format='PIR')
aln.write(file='two-alignment.pap', alignment_format='PAP')
```

### 1.2 Model the missing residues  
  Use `mod-seg.py` to model the missing residues;  
Note:   
- If the protein does not start from residue 1, then in this script the residue ID all regard the first residue appearing in PDB file as residue 1. So you might need to do some calculation to convert the residue ID.  
- Here Python class `loopmodel` is used instead of `automodel`, because in `automodel` other residues will also be modified during energy minimization. Here we hope only the missing residues get modelled while other residues are kept as the original.  
- One might also choose to have more models generated, here only two models will be generated.

Code snippet:  
```
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
        return selection(self.residue_range('487:', '516:') ,
                         self.residue_range('342:', '356:') ,
                         self.residue_range('619:', '624:'))

a = MyLoop(env,
           alnfile  = 'two-alignment.ali',      # alignment filename
           knowns   = 'm1v2',               # codes of the templates
           sequence = 't1v2',               # code of the target
           loop_assess_methods=assess.DOPE) # assess each loop with DOPE
a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model

a.loop.starting_model = 1           # First loop model
a.loop.ending_model   = 2           # Last loop model

a.make()                            # do modeling and loop refinement
```
