#!/bin/sh

# Get the name of the connected WiFi network
WIFI_NAME=$(nmcli device wifi list | grep '*' | awk '{print $3}')

# Output the name of the connected WiFi network
echo $WIFI_NAME

