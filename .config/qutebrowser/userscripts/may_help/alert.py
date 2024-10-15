#!/usr/bin/env python3

import os

def send_command_to_qute(command):
    with open(os.environ.get("QUTE_FIFO"), "w") as f:
        f.write(command)

def main():
    send_command_to_qute("message-info 'Guardado correctamente'")

if __name__ == "__main__":
    main()