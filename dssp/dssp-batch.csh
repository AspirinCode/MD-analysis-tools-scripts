#!/bin/csh

set cnt = 0
while ( $cnt < 2084 )
  # Use external mkdssp to process
  /home/shf317/bin/xssp-3.0.5/mkdssp -i pdb_dir/frame$cnt.pdb -o dssp_dir/raw/frame$cnt.dssp
  
  # delete the header
  sed '1,28d' dssp_dir/raw/frame$cnt.dssp > dssp_dir/tmp.dssp
  
  # extract only the 2nd structure summary column, delete TER's lines
  sed -e '/!/d' tmp.dssp > out.dssp
  cut -c17-17 out.dssp > extr/frame$cnt-extr.dssp

  @ cnt += 1
end
