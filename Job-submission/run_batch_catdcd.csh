#!/usr/bin/csh

# list all the files ended with 'dcd' and awk the 9th column
# which are the dcd file names, save them to 'dcdlist'
set dcdlist = `ls -lh *dcd | awk '{print $9}'`

# A For loop to use Catdcd to save 1 out of every 5 frames;
# It writes '10frm-step7_1.dcd' for original 'step7_1.dcd';
foreach i ($dcdlist)
    echo "catdcd -o 10frm-$i -stride 5 $i"
    catdcd -o 10frm-$i -stride 5 $i
end
