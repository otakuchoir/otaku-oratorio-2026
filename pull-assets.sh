#!/bin/sh
# Copy art assets from OO2's google drive to git.
#
# To run this script, you must
# - install rclone: https://rclone.org
# - on a linux machine
# - configure it with a google drive endpoint named `otaku-oratorio-gdrive` that has access to our shared drive: https://rclone.org/drive/
# It might be simplest to ask Evan to update assets until he finds a solution that others can use more easily.

#rclone lsd --drive-shared-with-me otaku-oratorio-gdrive:2026_OO2
#rclone sync --drive-shared-with-me otaku-oratorio-gdrive:2026_OO2 assets -v
for src in assets/"Character Sprites"/*; do
    base="`basename "$src"`"
    dest="otaku-oratorio-2026/game/images/$base"
    ln -s "../../../$src" "$dest"
done