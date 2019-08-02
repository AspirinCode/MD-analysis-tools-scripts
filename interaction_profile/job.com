#!/bin/csh -f
#

set type = om

foreach sys ( no1 no3 no4 no5 \
              no6 no7 no8 no9 \
              no10 no15 \
              no17 no18 no19 no20 \
            )

set ir = 6
set fr = 238

sbatch -J $sys --export type=${type},sys=${sys},ir=${ir},fr=${fr} combine.sh

end


