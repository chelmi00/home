#!/bin/bash

while true; do
  if [ "$(sh ../i3blocks/wifi.sh)" == "" ]; then
    while [ "$(sh ../i3blocks/wifi.sh)" == "" ]; do
      sleep 1
    done
    i3lock -c 337744
  fi
  sleep 1
done
