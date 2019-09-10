## Align the PDB sequence and Uniprot sequence

The PDB sequence has some missing loops (gaps) while the Uniprot sequence contains all the residues. 

Here, `m1v2.pdb` is a subunit of TRPV2, `t1v2.ali` is a sequence file of TRPV2. The `ali` file was generated using website which convert Uniprot 3-codon amino acid lists to 1-codon amino acid list, with each line having 40 amini acids.

Running job: `../../bin/mod9.21 align.py`. Generate `two-alignment.ali` and `two-alignment.pap` two files and a log file `align.log`.
