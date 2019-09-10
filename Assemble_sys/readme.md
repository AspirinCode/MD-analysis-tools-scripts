# Assemble the system


## Generate PDB for a protein sequence  
Use the `prot_config_gene.inp` and modify the input sequence to desired ones. The results give four files:  
- 'xx_xplor.psf': initial psf file;  
- 'xx_setup.pdb': initial IC Build result;  
- 'xx_mini.pdb': after 500sd + 500abnr minimization;    
- 'xx_random.pdb': after 40,000 steps dynamics;


## Need to mutate K<sup>+</sup> to Ca<sup>2+</sup> ions
The intuition is to use text editing tools to mutate the ions. However, due to calcium ions are divalent while pottasium ions are monovalent, we need to delete some K<sup>+</sup> ions at first. For example, if we want to mutate 4 K<sup>+</sup> ions to 4 Ca<sup>2+</sup> ions, we need to delete 4 K<sup>+</sup> ions first to count for the extra valence in Ca<sup>2+</sup> ions. Essentially we can do that by deleting 4 rows of K<sup>+</sup> in Vim, yet that can cause the atom number to be not consecutive. So we delete the ions via CHARMM.

- Use CHARMM script to delete 4 K<sup>+</sup> ions (assume want to mutate 4 K<sup>+</sup> to 4 Ca2+)  
  &ensp;&ensp; See `step5.1_rename.inp`.  
  &ensp;&ensp; Inputs:   
      &ensp;&ensp;&ensp;&ensp; step5_assembly.psf  
      &ensp;&ensp;&ensp;&ensp; step5_assembly.crd  
  &ensp;&ensp; Outputs:  
      &ensp;&ensp;&ensp;&ensp; step5.1_assembly.psf  
      &ensp;&ensp;&ensp;&ensp; step5.1_assembly.crd  
      
- Text-edit **'POT'** to **'CAL'**, also change the mass and charge accordingly  
  &ensp;&ensp; Perform test editing in `step5.1_assembly.psf` and `step5.1_assembly.crd`. Change resname 'POT' to 'CAL' but keep the segname still 'POT'.   
  
  &ensp;&ensp; In `step5.1_assembly.psf` file:  
  &ensp;&ensp; Before:
  ```
    599210 POT      468      POT      POT      POT       1.00000       39.0983           0   0.00000     -0.301140E-02
    599211 POT      469      POT      POT      POT       1.00000       39.0983           0   0.00000     -0.301140E-02
    599212 POT      470      POT      POT      POT       1.00000       39.0983           0   0.00000     -0.301140E-02
    599213 POT      471      POT      POT      POT       1.00000       39.0983           0   0.00000     -0.301140E-02
  ```
  
    &ensp;&ensp; After:
  ```
    599210 POT      468      CAL      CAL      CAL       2.00000       40.0800           0   0.00000     -0.301140E-02
    599211 POT      469      CAL      CAL      CAL       2.00000       40.0800           0   0.00000     -0.301140E-02
    599212 POT      470      CAL      CAL      CAL       2.00000       40.0800           0   0.00000     -0.301140E-02
    599213 POT      471      CAL      CAL      CAL       2.00000       40.0800           0   0.00000     -0.301140E-02
  ```
  
  &ensp;&ensp; In `step5.1_assembly.crd` file:  
  &ensp;&ensp; Before:
  ```
    599210    147852  POT       POT            10.2238013000      -21.3232687000      -77.2359248000  POT       468             0.0000000000
    599211    147853  POT       POT           -43.0740676000      -80.3456990000      -94.4507039000  POT       469             0.0000000000
    599212    147854  POT       POT            81.0987125000      -84.4845251000       67.5789246000  POT       470             0.0000000000
    599213    147855  POT       POT            48.9741087000      -94.2898129000       29.6778919000  POT       471             0.0000000000
  ```
  
    &ensp;&ensp; After:
  ```
    599210    147852  CAL       CAL            10.2238013000      -21.3232687000      -77.2359248000  POT       468             0.0000000000
    599211    147853  CAL       CAL           -43.0740676000      -80.3456990000      -94.4507039000  POT       469             0.0000000000
    599212    147854  CAL       CAL            81.0987125000      -84.4845251000       67.5789246000  POT       470             0.0000000000
    599213    147855  CAL       CAL            48.9741087000      -94.2898129000       29.6778919000  POT       471             0.0000000000
  ```

- Generate inputs for simulation program, use OpenMM for example  
      &ensp;&ensp; Because of OpenMM's high performance, we mainly use OpenMM for large system simulations these days (6/2019). `step5.1_input.inp` prepare the system for OpenMM simulations.  
  &ensp;&ensp; Inputs:   
      &ensp;&ensp;&ensp;&ensp; step5.1_assembly.psf  
      &ensp;&ensp;&ensp;&ensp; step5.1_assembly.crd  
  &ensp;&ensp; Outputs:  
      &ensp;&ensp;&ensp;&ensp; step5_charmm2omm.psf  
      &ensp;&ensp;&ensp;&ensp; step5_charmm2omm.oldpsf 
      &ensp;&ensp;&ensp;&ensp; step5_charmm2omm.crd  
      &ensp;&ensp;&ensp;&ensp; step5_charmm2omm.pdb   
      &ensp;&ensp;&ensp;&ensp; step5_charmm2omm.str   
      &ensp;&ensp;&ensp;&ensp; step5_charmm2omm.crd  
      
 &ensp;&ensp; `step5_charmm2omm.str`:  
 ```
* BOXLX    = @A
* BOXLY    = @B
* BOXLZ    = @C
*
 ```
 
 ## Place certain lipids at specific positions  
 In step3, first visualize "step3_packing.pdb" to see which pairs of lipids to exchange the position. At step3, lipids are only pseudo-atoms and thus can be mutated to desired lipid type easily. Picking up the pairs for exchange, we then text modify "step3_packing_head.psf" and "step3_packing_head.crd" to exchange the lipid positions. Remember also to modify the related charges in PSF file.
 
 ## Ring penetration test
 Since cholesterol and sugar all have rings, we want to avoid such ring penetration in the system. We use the following script `pentest.py` and `findrings.py` to detect the penetration. The periodic boudary parameters are also provided to help detect the penetration between primary and image boxes. `Qhull` is needed for detecting ring penetration on proteins.
 

 ```
module load anaconda/python2
python pentest.py -xtl rect -pbc x_len y_len **.psf **.crd
 ```

 For solving ring penetration issues, one can re-assemble the system or use the script here to orient/translate the molecule and residues to avoid the ring penetraion. Sometimes peptides are modelled by Modeller or other softwares. Since some of they are very long, these programs cannot automatically detect and solve this. 
 
 https://github.com/sha256feng/Model-long-missing-loop
