## This folder tries to solve the ring penetration issue and peptide knot produced in Modeler modeling.

**Read input structures**:  
&nbsp;&nbsp; - step1_pdbreader.psf  
&nbsp;&nbsp; - step1_pdbreader.crd  
  
**Processing CHARMM script**:  
&nbsp;&nbsp; - step2_pene_solve.inp

Principle:  
- Set some parts movable and others fixed;  
- Rotate, translate the movable part;  
- Local minimization first, then global minimization;
