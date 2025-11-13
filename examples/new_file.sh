#!/usr/bin/env bash

# simple script to create a file with a unique name in a selected location for an editor
#   it's designed to compensate for some editors not being able to create files in desired location or that are savable without renaming and/ or manual saves
#     needs to be called <path_to_script><script_name> <command_for_editor>
#     ex. $HOME/bin/ide_new_file.sh code



new_file_dir="$HOME/mnt/data/ide/instant_files"
new_file_prefix='ide_'
new_file_suffix=''
line_1=$(echo -n $(date +"%Y.%m.%d %H:%M:%S %Z (")
echo -n $(date --utc +"%H:%M:%S %Z) (")
for i in $(echo "ibase=10; obase=36; $(date --utc +'%s%N')" | cut -c -31 | bc)
do 
  (
  echo -n "$(expr substr '0123456789abcdefghijklmnopqrstuvwxyz' $i 1)"
  )
done
echo ")")


new_file_sn=$(for i in $(echo "ibase=10; obase=36; $(date --utc +'%s%N')" | cut -c -32 | bc); do echo -n "$(expr substr '0123456789abcdefghijklmnopqrstuvwxyz' $i 1)"; done)

touch "$new_file_dir/$new_file_prefix$new_file_sn$new_file_suffix"

echo "$line_1




















" >> "$new_file_dir/$new_file_prefix$new_file_sn$new_file_suffix"

$1 "$new_file_dir/$new_file_prefix$new_file_sn$new_file_suffix"
