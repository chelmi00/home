#!/bin/bash

while true; do
  if pgrep i3lock > /dev/null; then
    feh -F /home/chelmi/LoImportante/General/Fotos/Linux/Linux/Edits/lock.png &
    feh_pid=$!
    sleep 3
    kill $feh_pid
    while pgrep i3lock > /dev/null; do
      sleep 1
    done
  fi
  sleep 1
done
