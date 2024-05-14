#!/bin/bash

if [ $(/usr/share/i3blocks/volume 5 pulse) == "0%" ]; then
	pactl set-sink-mute @DEFAULT_SINK@ toggle
	exit 0
elif [ $(/usr/share/i3blocks/volume 5 pulse) == "MUTE" ]; then
	exit 0
fi
pactl set-sink-volume @DEFAULT_SINK@ -5%
$refresh_i3status
