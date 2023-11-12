#!/bin/bash

option=$(printf "Shutdown\nReboot\nLock\nExit\nSwitch User\nSuspend\nHibernate" | dmenu -p "Power shortcut pressed: ")

case "$option" in
    "Lock")
        i3-msg exec i3exit lock, mode "default"
    ;;
    "Exit")
        i3-msg exec i3exit logout, mode "default"
    ;;
    "Switch User")
        i3-msg exec i3exit switch_user, mode "default"
    ;;
    "Suspend")
        i3-msg exec i3exit suspend, mode "default"
    ;;
    "Hibernate")
        i3-msg exec i3exit hibernate, mode "default"
    ;;
    "Reboot")
        i3-msg exec i3exit reboot, mode "default"
    ;;
    "Shutdown")
        i3-msg exec i3exit shutdown, mode "default"
    ;;
  *)
    echo "Opción no válida"
    ;;
esac
