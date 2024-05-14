#!/bin/bash

if [ "$(printf "yes\nno" | dmenu -p "You pressed the shutdown shortcut. Do you really want to shutdown your computer? ")" == "yes" ]; then
  shutdown -h +0
fi

