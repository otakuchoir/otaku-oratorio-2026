# Otaku Oratorio 2026

This is the visual novel that powers the Otaku Oratorio 2026 performance. Created by the [Otaku Choir](https://www.otakuchoir.org/). Powered by [Ren'py](https://www.renpy.org/).

**Try the latest version: https://erosson.itch.io/otaku-oratorio-2026?secret=Ej4ArGlmXwr1HcR3SCoDkI4UyL8**

Tickets for the show: https://www.otakuchoir.org/upcoming-concerts

Our artwork in google drive: https://drive.google.com/drive/folders/1z-uWiRzeMPX7-zC9o1mTezrn6EUNmGcA

The 2025 show's code: https://github.com/mienaikoe/otaku-oratorio

## See or run the project

**Try the latest version: https://erosson.itch.io/otaku-oratorio-2026?secret=Ej4ArGlmXwr1HcR3SCoDkI4UyL8**

[![continuous integration tests](https://github.com/erosson/otaku-oratorio-2026/actions/workflows/ci.yml/badge.svg)](https://github.com/erosson/otaku-oratorio-2026/actions/workflows/ci.yml)
[![build and release](https://github.com/erosson/otaku-oratorio-2026/actions/workflows/release.yml/badge.svg)](https://github.com/erosson/otaku-oratorio-2026/actions/workflows/release.yml)

The latest version of this VN is automatically uploaded to itch.io whenever developers change anything in git. If the badges above are green, things are working and itch.io should be up to date. You can also download windows/mac/linux versions from there.

## Develop the project

To build and run the project on your machine, for development:

- Download https://www.renpy.org/ 
- Start the Ren'py launcher and choose a project directory
- `git clone` this repository to the Ren'py project directory
- `git lfs pull` this repository to download large art files
- Optional: open it in [vscode](https://code.visualstudio.com/) if you'll be programming a lot

Talk to Evan (@erosson on discord) if you get stuck.

## Copying art from our gdrive to git

Ren'py can't access [our google drive](https://drive.google.com/drive/folders/1z-uWiRzeMPX7-zC9o1mTezrn6EUNmGcA), so we have a script that copies files from the gdrive into git. A copy of the gdrive is mirrored to the `./assets` directory, and files are copied/shortcutted to other places as needed.

    ./bin/pull-assets

This script currently requires a bunch of undocumented google drive authentication setup.o Evan's working on something easier to setup (probably a github action that does the auth for you). Until that's ready, it's probably easiest to ask Evan to update it for you.

Please don't copy files to git from the gdrive by hand. This script will overwrite them later.

Git doesn't like big non-text files, so our art is stored using [git large file storage](https://github.com/git-lfs/git-lfs). This means you'll need to run `git lfs pull` when cloning the repository, but otherwise it's mostly transparent. If you're seeing strange behavior and errors about invalid images, try `git lfs pull`.