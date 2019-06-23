#!/bin/csh
#The file is for dumping and loading the correct firstTimeStep of each dcd file

set n = 1
set first = 5000
while ( $n <= 999 )
	dumpdcd step7.${n}.dcd > temp.header
	@ first = 500000 * ( $n - 1 ) + 5000
	sed -i "2s/0/${first}/" temp.header
	sed -i "3s/1/5000/" temp.header
	sed -i "4s/100/500000/" temp.header
	loaddcd step7.${n}.dcd < temp.header
	@ n += 1
end
