#!/bin/sh

# Usage: for mail update;
# Need to add this script to cron_tab

now="$(date +"%T")"
~/workdir/sys_master/job.ls > ~/workdir/sys_master/progress.txt
~/workdir/sys_master/err.chk >> ~/workdir/sys_master/progress.txt
mail -s "${now} update" shf317@lehigh.edu < ~/workdir/sys_master/progress.txt
