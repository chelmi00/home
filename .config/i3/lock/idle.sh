#!/bin/bash

# Set the idle threshold in milliseconds
IDLE_THRESHOLD=270000

while true; do
    # Get the idle time in milliseconds
    IDLE_TIME=$(xprintidle | grep -o '[0-9]*' | head -n 1)

    # If the idle time surpasses the threshold
    if [ $IDLE_TIME -ge $IDLE_THRESHOLD ]; then
        # Set the brightness to 10%
        $HOME/.config/i3/brightness/idle_brightness.sh 4
        while [ $IDLE_TIME -ge $IDLE_THRESHOLD ]; do
            IDLE_TIME=$(xprintidle | grep -o '[0-9]*' | head -n 1)
            # If the idle time is less than the threshold
            if [ $IDLE_TIME -le $IDLE_THRESHOLD ]; then
                # Set the brightness to the value saved in the text file
                $HOME/.config/i3/brightness/idle_brightness.sh 1
            fi
            sleep 1
        done
    fi
    sleep 10
done