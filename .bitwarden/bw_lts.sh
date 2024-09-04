#!/bin/bash

# Bitwarden-{año}.{versión}-x86_64.AppImage
dir="/home/chelmi/.bitwarden/"

lts_file=""
lts_v=0

for file in "$dir"Bitwarden-*.AppImage; do
    if [[ $file =~ Bitwarden-([0-9]+)\.([0-9]+\.[0-9]+)-x86_64\.AppImage ]]; then
        version_str="${BASH_REMATCH[1]}${BASH_REMATCH[2]}"

        # version_str to number
        if [[ $(bc <<< "$version_str > $lts_v") == 1 ]]; then
            lts_file="$file"
            lts_v="$version_str"
        fi
    fi
done

# Imprimir el resultado
if [[ -n "$lts_file" ]]; then
    $lts_file
fi