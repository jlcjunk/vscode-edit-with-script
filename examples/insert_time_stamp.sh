#!/usr/bin/env bash

# output local time, MST time, UTC time, and a hash based on time
#     cut -c -31 = resolution of .1 second (keep from beginning to 31st character), -32 = .01 second

echo -n $(date +"%Y.%m.%d %H:%M:%S %Z (")
echo -n $(TZ=MST7 date +"%H:%M:%S %Z) (")
echo -n $(date --utc +"%H:%M:%S %Z) (")
for i in $(echo "ibase=10; obase=36; $(date --utc +'%s%N')" | cut -c -31 | bc)
do 
  (
  echo -n "$(expr substr '0123456789abcdefghijklmnopqrstuvwxyz' $i 1)"
  )
done
echo ")"
