#!/bin/bash

if [ "$(printf "yes\nno" | dmenu -p "You pressed the exit shortcut. Do you really want to exit i3? This will end your X session. ")" == "yes" ]; then
  i3-msg exit
fi

