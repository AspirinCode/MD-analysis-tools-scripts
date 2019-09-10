# Model-long-missing-loop
This repository contains code and examples to model multiple missing loops in tetrameric protein.

Modeller script is mainly based on following link: https://salilab.org/modeller/wiki/Missing%20residues 


|	Original resid	| Afterwards	| Original resid	|Afterwards |
|--- | --- | --- | --- |
|	561	| 561-74=487	| 589	| 589-74=515 |
|	416	|416-74=342	| 427	| 427-74=353 |
|	693	|693-74=618	| 698	| 698-74=624 |

`../../bin/mod9.21 mod-seg.py` to execute the python script for Modeller. `mod9.21` is an executable version of Python and Modeller.

	- Execute the loop modeling for each chain. Mutate the "A" letters in `two-alignment.ali` to "B"/"C"/"D" letters. And run them in separate folder, because the output PDB files have the same names. Later I visually checked each chain's modeling result and `cat` them together.
	List of output files as example:


	- Loop modeling results: loops forming a knot -- need to fix 
  Two segments have knotted structure of peptides. In order to prepare a cleaner version where there is no such problem, I use CHARMM script to solve this bad penetration issues. The program requires feeding of PSF and CRD files. So I generated PSF and CRD file firstly by CHARMM-GUI's PDBReader. Later I used following script to rotate the loops and did some minimization to avoid clash and bad angles.

# Solve ring penetration issue

**Read input structures**:  
&nbsp;&nbsp; - step1_pdbreader.psf  
&nbsp;&nbsp; - step1_pdbreader.crd  
  
**Processing CHARMM script**:  
&nbsp;&nbsp; - step2_pene_solve.inp

Principle:  
- Set some parts movable and others fixed;  
- Rotate, translate the movable part;  
- Local minimization first, then global minimization;
