# PyMOL commands  

- Show sequence 
Go to 'Display'-->'Sequence' to show the sequence on the top panel.  
Click on sequence residues to select a range of residues. Right click to do some operations like renaming, shown as cartoons etc. 

- Rendering snapshot: 
```
png ~/Desktop/test.png, width=10cm, dpi=300, ray=1
```

- Delete molecules:
```
delete molname
```

- Generate crystallography symmetry  
```
fetch 1GVF
symexp sym,1GVF,(1GVF),1
symexp sym,1GVF,(1GVF),5
```

## Reference  
1. PyMol command reference: https://pymol.org/pymol-command-ref.html 
