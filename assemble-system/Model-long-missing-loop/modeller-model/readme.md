## Use Modeller & other tools to model the loop  


## 0. Preprocess
- Use VMD to write PDB file for each chain for multi-subunit protein;  
Because currently I am not able to figure out multimeric protein loop modeling in Modeller;

## 1. Modeller  
### 1.1 Align sequence and PDB structure sequence  
Use `/align/align.py` to generate the sequence alignment `two-component.ali`;  
This is going to guide the `loopmodel` module what residues to add for missing loops. Also it would be good to name both the PDB and the sequence `ali` file to both four-letter name, eg., "m1v2", "t1v2". Not sure if otherwise Modeller still works. "~/bin/modeller9.21/bin/mod9.21 xxx.py" to execute a Python script. 

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
- For a home-tetramer protein, the "two-alignment.ali" can be used for each chain. But small modification is required. We need to change the letter 'A' to designate letters like 'B', 'C', 'D'. 

File "two-component.ali" header (for a full view of the file, please jump to end): 
```
>P1;m1v2
structureX:m1v2.pdb:  76 :A:+605 :A:::-1.00:-1.00
```

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
- Result  
The result would be a number of log files and PDB files with names eg., "t1v2.BL00010001.pdb", "t1v2.BL00020001.pdb". Visualize the PDB files and check if there is broken chain. If some part is broken, you need to adjust the residue range to one or two residues. Also, make sure the residue range is given correctly given the missing N-terminal residues.  

### 1.3 Model the missing residues -- repeat for other monomers 

## 2. Concatenate the PDB files of monomers  
Use `cat` and `vim` to concatenate the PDB files. Add chain names to PDB file, using `ctrl+v` to do block selection.  

## 3. Coot processing   
After the monomers get concatenated together, there are knots and crashes. We need to fix them. Coot is a good tool.
Open PDB structure in Coot and do `Rotate and Translation` in Coot: select the loop residue range, shift the bars of x, y, z translation and rotation, also a bit manual drag on coot GUI. It might take a while to get a feel for the translation and rotation bars. But they work ideally great!  

If the structure looks good, then save the coordinates by adding a name with "coot" suffix. (Good naming habits are also appreciated.)  

## 4. CHARMM minimization  
After our juggling of the PDB structure, we need to make it more reasonable to feed to MD simulations. So we use the following CHARMM script to minimize the structure.  
### 4.1 Use CHARMM-GUI PDBReader to get PSF and CRD file  
Upload the structure to CHARMM-GUI's PDBReader (http://charmm-gui.org/?doc=input/pdbreader) and download the PSF and CRD file. Because we already have `toppar` parameter files on server, otherwise, also download the `toppar` files or the whole tar file.  

### 4.2 CHARMM minimization  
Use following script to fix other parts beside the missing loops and do two rounds of minimization. 
Code snippet: 
```
!
! Nonbonded Options [short distances and no pme just for image centering]
!

nbonds atom vatom vfswitch bycb -
       ctonnb 4.0 ctofnb 5.0 cutnb 6.0 cutim 6.0 -
       inbfrq -1 imgfrq -1 wmin 1.0 cdie eps 1.0 -
!        ewald pmew fftx @fftx ffty @ffty fftz @fftz  kappa .34 spline order 6
energy

define movable sele segid PRO* .and. ( ( resid 341 : 358 ) .or. -
        ( resid 485 : 518 ) ) end

cons fix sele .not. movable  end

mini sd nstep 100
mini abnr nstep 100
mini sd nstep 100
mini abnr nstep 100

open write unit 10 card name minimized.pdb
write coor unit 10 pdb
```

## 5. Assemble the system: Membrane Builder
We first upload it to OPM server ( https://opm.phar.umich.edu/ppm_server ) to predict the transmembrane domain and wait for a few minites to get the oriented PDB file. There is one problem with such previous processing -- the 'HIS' is named to 'HSD'. OPM thus named the 'HSD' residues to be 'HETATM', which later would confuse CHARMM-GUI and ask you to upload the parameters for 'HSD' residue. So use Vim to edit the 'HETATM' to 'ATOM' by typing `:%s/HETATM/ATOM  /g`.  

We then upload it to CHARMM-GUI Membrane Builder and select the PDB type as 'CHARMM'. Next steps are farmilar, but no need to do more orientations. 

__Hope your protein processing goes successfully!__ 


## Appendix
- "two-alignment.ali"  
```
>P1;m1v2
structureX:m1v2.pdb:  76 :A:+605 :A:::-1.00:-1.00
-DRDRLFSVVSRGVPEELTGLLEYLRWNSKYLTDSAYTEGSTGKTCLMKAVLNLQDGVNACIMPLLQIDKDSGNP
KLLVNAQCTDEFYQGHSALHIAIEKRSLQCVKLLVENGADVHLRACGRFFQKHQGTCFYFGELPLSLAACTKQWD
VVTYLLENPHQPASLEATDSLGNTVLHALVMIADNSPENSALVIHMYDGLLQMGARLCPTVQLEEISNHQGLTPL
KLAAKEGKIEIFRHILQREFSGPYQPLSRKFTEWCYGPVRVSLYDLSSVDSWEKNSVLEIIAFHCKSPNRHRMVV
LEPLNKLLQEKWDRLVSRFFFNFACYLVYMFIFTVVAYHQPG--------------ESMLLLGHILILLGGIYLL
LGQLWYFWRRRLFIWISFMDSYFEILFLLQALLTVLSQVLRFMETEWYLPLLVLSLVLGWLNLLYYTRGFQHTGI
YSVMIQKVILRDLLRFLLVYLVFLFGFAVALVSLSRY-----------------------------RSILDASLE
LFKFTIGMGELAFQEQLRFRGVVLLLLLAYVLLTYVLLLNMLIALMSETVNHVADNSWSIWKLQKAISVLEMENG
YWWCRRKKHREGRLLKVG------PDERWCFRVEEVNWAAWEKTLPTLSEDPSGP*

>P1;t1v2
sequence:t1v2:     : :     : ::: 0.00: 0.00
FDRDRLFSVVSRGVPEELTGLLEYLRWNSKYLTDSAYTEGSTGKTCLMKAVLNLQDGVNACIMPLLQIDKDSGNP
KLLVNAQCTDEFYQGHSALHIAIEKRSLQCVKLLVENGADVHLRACGRFFQKHQGTCFYFGELPLSLAACTKQWD
VVTYLLENPHQPASLEATDSLGNTVLHALVMIADNSPENSALVIHMYDGLLQMGARLCPTVQLEEISNHQGLTPL
KLAAKEGKIEIFRHILQREFSGPYQPLSRKFTEWCYGPVRVSLYDLSSVDSWEKNSVLEIIAFHCKSPNRHRMVV
LEPLNKLLQEKWDRLVSRFFFNFACYLVYMFIFTVVAYHQPSLDQPAIPSSKATFGESMLLLGHILILLGGIYLL
LGQLWYFWRRRLFIWISFMDSYFEILFLLQALLTVLSQVLRFMETEWYLPLLVLSLVLGWLNLLYYTRGFQHTGI
YSVMIQKVILRDLLRFLLVYLVFLFGFAVALVSLSREARSPKAPEDNNSTVTEQPTVGQEEEPAPYRSILDASLE
LFKFTIGMGELAFQEQLRFRGVVLLLLLAYVLLTYVLLLNMLIALMSETVNHVADNSWSIWKLQKAISVLEMENG
YWWCRRKKHREGRLLKVGTRGDGTPDERWCFRVEEVNWAAWEKTLPTLSEDPSGP*
```
