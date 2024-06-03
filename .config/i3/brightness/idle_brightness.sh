#!/bin/bash

# Check if input argument is provided
if [ -z "$1" ]; then
  echo "Error, missing argument"
  exit 1
fi

current_brightness=$(cat $HOME/.config/i3/brightness/brightness_value.txt)

# Parse the input
input=$1
delta=$(echo "$input" | bc)

target_brightness=$(echo "$current_brightness / $delta" | bc -l)

# Set the brightness using xrandr
xrandr --output "$(xrandr | grep " connected" | awk '{print $1}')" --brightness "$target_brightness"

# Redshift gets stopped, so this reactivates it
redshift -o -l 40.441468:-3.628227 -t 6500:3500