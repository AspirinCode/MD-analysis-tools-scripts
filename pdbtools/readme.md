# PDBtools 

PDBtools is a collection of script to post-process PDB file for various purposes. 

1. Renumber the residue IDs: [reindex_pdb.py](https://github.com/sha256feng/MD-analysis-tools-scripts/blob/master/pdbtools/reindex_pdb.py)




- Code details and purposes   
As can be seen below, the PDB residue ID starts from 2 but according to Uniprot FASTA sequence, it should be 76. The reason is because I modelled the missing loops in Modeller and I did not want to model the first 75 residues. So the output PDB file starts from residue 2. Also this is a PDB written from DCD trajectory in VMD, the chain IDs are all 'P'. We hope to assign chain ID 'A/B/C/D' for each segment. For CBD, which is a ligand, though they belong to different segment 'HETC' and 'HETD', still they share the same chain ID 'H', which I want them to be correspondingly 'C' and 'D'.  

So `reindex_pdb.py [increment-for-each-residue] input.pdb output.pdb` does this job.
```
ATOM      1  N   ASP P   2     141.602  48.856  29.129  1.00  0.00      PROA
ATOM      2  HT1 ASP P   2     142.534  48.457  29.359  1.00  0.00      PROA
ATOM      3  HT2 ASP P   2     141.556  49.753  29.654  1.00  0.00      PROA
ATOM      4  HT3 ASP P   2     141.684  49.135  28.130  1.00  0.00      PROA
ATOM      5  CA  ASP P   2     140.470  47.895  29.521  1.00  0.00      PROA
ATOM      6  HA  ASP P   2     140.735  47.003  28.972  1.00  0.00      PROA
ATOM      7  CB  ASP P   2     140.485  47.626  31.104  1.00  0.00      PROA
ATOM      8  HB1 ASP P   2     139.724  46.872  31.397  1.00  0.00      PROA
...

ATOM  42647  C10 CBD H1001      87.473 103.337  87.797  1.00  0.00      HETC
ATOM  42648  O2  CBD H1001      88.214 102.129  87.752  1.00  0.00      HETC
ATOM  42649  H30 CBD H1001      87.806 101.612  88.450  1.00  0.00      HETC
ATOM  42650  O1  CBD H1001      84.191 104.745  89.100  1.00  0.00      HETC
ATOM  42651  H29 CBD H1001      84.040 103.918  89.562  1.00  0.00      HETC
ATOM  42652  C15 CBD H1001     104.757  95.593  87.533  1.00  0.00      HETD
ATOM  42653  C13 CBD H1001     105.931  96.345  87.685  1.00  0.00      HETD
ATOM  42654  H15 CBD H1001     104.800  94.518  87.443  1.00  0.00      HETD
ATOM  42655  C16 CBD H1001     107.278  95.718  87.458  1.00  0.00      HETD
ATOM  42656  C18 CBD H1001     107.955  96.180  86.165  1.00  0.00      HETD
ATOM  42657  H16 CBD H1001     107.154  94.614  87.474  1.00  0.00      HETD
ATOM  42658  H17 CBD H1001     107.888  96.011  88.339  1.00  0.00      HETD
```
