# Automated Workflow for Loop Modelling 

This repo includes a number of C Shell scripts and Python scripts to build the missing loops in a protein. This protocol can deal with situations, e.g., 
- Long missing loops that ModLoop cannnot model;
- Modelled loop is buried in transmembrane domain;
- Multiple subunits;  

The use of C shell scripts is based on the rationale that we want to make things automated thus with less human error and easy to look back to check the details. 

## Overview of workflow 
1. Step 1  
Truncate other unnecessary residues e.g., `step1.1_truncate_nterm.pdb`, keep only the residues of interests and write each chain into different PDB files, `step1.2_chain-a.pdb` etc. 

2. Step 2  
Use Modeller to model the missing loops within specified region, which includes sequence alignment and model the loop with some refinement.  
`align.py`: align the model with sequence card;  
`mod-seg.py`: Call Modeller program to model the loop and refine;   
`step2.1_align_run.sh`: do the alignment and model building;  
`step3_concat.sh`: collected modelled protein in each subunit folder and compress into a `tar.gz` file. 

3. Step 3   
Download the file to local laptop folder and visualize the result. Pick up the best one for each subnit and assemble it into the tetramer format, adding the ligands and other peptides. 

4. Step 4 
If all the produced models have unsatisfactory loops, we can feed the model to implicit model in CHARMM-GUI module and manipulate it then follow it with some dynamics. As a case study, I had a model where the modelled loops were all located in the transmembrane region instead of extracellular region, which would later impact lipid packing during assembly building. Thus I flipped the peptide upward and ran minimization as well as dynamics to relax it. An alternative is to use MMFP force to pull the peptide upward. I did not successfully make that because in this case, part of the missing loop region was stuck in a-helices bundle which stopped it from freely moving to extracelullar region. 
