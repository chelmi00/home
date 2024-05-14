#!/bin/bash

rm /tmp/screenshot.png
scrot /tmp/screenshot.png
convert /tmp/screenshot.png -blur 0x20 /tmp/screenshotblur.png
convert /tmp/screenshotblur.png $HOME/LoImportante/General/Fotos/Linux/Linux/png/Linux_X.png -gravity center -composite -matte /tmp/screenlock.png
i3lock -i /tmp/screenlock.png
