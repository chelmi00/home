#!/bin/bash

while true; do
  lid_state=$(cat /proc/acpi/button/lid/LID0/state | awk '{print $2}')
  state=$(cat /proc/acpi/button/lid/LID0/state | awk '{print $1}')
  if [ "$lid_state" == "closed" ]; then
    i3lock -i $HOME/LoImportante/General/Fotos/More/linux_bg/lock.png
  fi
  if [ "$state" == "nixstate" ]; then
    i3lock -c 000000 -i $HOME/LoImportante/General/Fotos/More/linux_bg/notWindows.png
  fi 
  sleep 5
done
