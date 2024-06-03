#!/bin/bash

# Set the idle and lock thresholds in milliseconds
IDLE_THRESHOLD=270000
LOCK_THRESHOLD=300000

while true; do
    # Get the idle time in milliseconds
    IDLE_TIME=$(xprintidle | grep -o '[0-9]*' | head -n 1)

    # If the idle time surpasses the threshold
    if [ $IDLE_TIME -ge $IDLE_THRESHOLD ] && [ $IDLE_TIME -lt $LOCK_THRESHOLD ]; then
        # Set the brightness to 10%
        $HOME/.config/i3/brightness/idle_brightness.sh 4
        while [ $IDLE_TIME -ge $IDLE_THRESHOLD ] && [ $IDLE_TIME -lt $LOCK_THRESHOLD ]; do
            sleep .1
            IDLE_TIME=$(xprintidle | grep -o '[0-9]*' | head -n 1)
            # If the idle time is less than the idle threshold or greater than the lock threshold
            if [ $IDLE_TIME -le $IDLE_THRESHOLD ] || [ $IDLE_TIME -ge $LOCK_THRESHOLD ]; then
                # Set the brightness to the value saved in the text file
                $HOME/.config/i3/brightness/idle_brightness.sh 1
            fi
            # If the idle time surpasses the lock threshold
            if [ $IDLE_TIME -ge $LOCK_THRESHOLD ]; then
                # Lock the screen
                i3lock -i /home/chelmi/LoImportante/General/Fotos/Linux/Linux/Edits/lock.png
            fi
        done
    fi
    sleep 1
done
