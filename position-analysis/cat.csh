#!/bin/csh

set a1 = 500ns
set a2 = 501-1000ns
set a3 = 1001-1500ns
set a4 = 1501-2000ns
set a5 = 2001-3000ns
set a6 = 3001-4000ns
set a7 = 4001-5000ns
set a8 = 5001-6000ns

set list = ( $a1 $a2 $a3 $a4 $a5 $a6 $a7 $a8 )
set i = 1
while ( $i <= 8 )
    echo ${list[$i]}
    if ( $i == 1 ) then
        cat c11-position-${list[$i]}.plo > c11-position.plo
        cat c8-position-${list[$i]}.plo > c8-position.plo
    else
        cat c11-position-${list[$i]}.plo >> c11-position.plo
        cat c8-position-${list[$i]}.plo >> c8-position.plo
    endif
    @ i += 1
end
