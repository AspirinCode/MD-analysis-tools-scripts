#!/bin/csh
#The file is for dumping and loading the correct firstTimeStep of each dcd file

set n = 801
set first = 5000
while ( $n <= 1000 )

    # Get the header of the DCD file and calculate should-be values;
    dumpdcd step7.${n}.dcd > temp.header
    @ first = 500000 * ( $n - 801 ) + 5000
    
    # Get the first column value of 2nd row
    set orig = `awk 'FNR == 2 {print}' temp.header | awk '{print $1}'`
    
    # Edit the value
    sed -i "2s/${orig}/${first}/" temp.header
    
    # Load into DCD files
    loaddcd step7.${n}.dcd < temp.header
    @ n += 1
end
