#set SOURCE = /share/ceph/woi216group-c2/shf317/trpv2/v2-cbd-rot-modloop-0805/lig-300k
#
#cp $SOURCE/toppar.str $SOURCE/recenter* $SOURCE/run_charmm* ./
#mkdir orig_dcd
#mkdir last_frame_dcd

# get last frame
set last = 2084
set inputdcd = v2-apo-vanilla-300k-500ns.dcd
catdcd -o last_frame_$inputdcd -first $last -last $last $inputdcd
mv last_frame_$inputdcd last_frame_dcd/

set dir = `pwd`
echo "scp sol:$dir/last_frame_$inputdcd ./"
