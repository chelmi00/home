#!/bin/bash

brightness=$(xrandr --verbose --current | grep Brightness | awk '{print $2}')
brightness_percent=$(echo "$brightness * 100" | bc)
echo "$brightness_percent%"

