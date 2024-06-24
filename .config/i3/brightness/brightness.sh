#!/bin/bash

# Check if input argument is provided
if [ -z "$1" ]; then
  echo "Error, missing argument"
  exit 1
fi

# Get the current brightness
current_brightness=$(xrandr --verbose --current | grep Brightness | awk '{print $2}')

# Parse the input
input=$1
delta=$(echo "$input" | bc)

# Calculate the target brightness
target_brightness=$(echo "$current_brightness + $delta" | bc -l)

# When lowering brightness, maximum is 1
if (( $(echo "$target_brightness > 1" | bc -l) )) && (( $(echo "$delta < 0" | bc -l) )); then
  target_brightness=1
fi

# Clamp the brightness value between 0 and $max
max=1.7
if (( $(echo "$target_brightness > $max" | bc -l) )); then
  target_brightness=$max
elif (( $(echo "$target_brightness < 0" | bc -l) )); then
  target_brightness=0
fi

# If the target brightness is not a multiple of 0.05, round it to the nearest multiple
extra=$(echo "($target_brightness * 100) % 5" | bc)
if (( $(echo "$extra != 0" | bc -l) )); then
  if (( $(echo "$delta < 0" | bc -l) )); then
    target_brightness=$(echo "$target_brightness + ((5 - $extra) / 100)" | bc -l)
  else
    target_brightness=$(echo "$target_brightness - ($extra / 100)" | bc -l)
  fi
fi

# Set the brightness using xrandr
xrandr --output "$(xrandr | grep " connected" | awk '{print $1}')" --brightness "$target_brightness"

# Save brightness to text file
echo "$target_brightness" > $HOME/.config/i3/brightness/brightness_value.txt

# Redshift gets stopped, so this reactivates it
if (( $(echo "$target_brightness < 1" | bc -l) )); then
  redshift -o -l 40.441468:-3.628227 -t 6500:3500
fi