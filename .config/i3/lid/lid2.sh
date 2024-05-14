#!/bin/bash

sleep 10

if [ "$(cat /proc/acpi/button/lid/LID0/state)" == "state:      open" ] && [ "$(sh ../i3blocks/wifi.sh)" == "" ]; then
  echo "No hay wifi"
  while true; do
      if [ "$(cat /proc/acpi/button/lid/LID0/state)" == "state:      closed" ]; then
        echo "Se ha cerrado"
        while [ "$(cat /proc/acpi/button/lid/LID0/state)" == "state:      closed" ]; do
          sleep 1
        done
        echo "Se ha abierto"
        i3lock -c 334477
      fi
    sleep 1
  done
fi

if [ "$(cat /proc/acpi/button/lid/LID0/state)" == "state:      open" ] && [ "$(sh ../i3blocks/wifi.sh)" != "" ]; then
  echo "Hay wifi"
  while true; do
    if [ "$(sh ../i3blocks/wifi.sh)" == "" ]; then
      i3lock -c 337744
      while [ "$(sh ../i3blocks/wifi.sh)" == "" ]; do
        sleep 1
      done
    fi
    sleep 1
  done
fi
