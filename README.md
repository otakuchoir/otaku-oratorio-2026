# Otaku Oratorio 2026

This is the visual novel that powers the Otaku Oratorio 2026 performance on Friday October 9. Created by the [Otaku Choir](https://www.otakuchoir.org/). Powered by [Ren'py](https://www.renpy.org/).

**Try the latest version: https://erosson.itch.io/otaku-oratorio-2026?secret=Ej4ArGlmXwr1HcR3SCoDkI4UyL8**

Tickets for the show: https://www.otakuchoir.org/upcoming-concerts

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
- Optional: open it in [vscode](https://code.visualstudio.com/) if you'll be programming a lot

If you're writing sprite code, this gallery might help: https://otaku-oratorio-2026-gallery.netlify.app/

Talk to Evan (@erosson on discord) if you get stuck.

## Copying art from our gdrive to git

    ./bin/pull-assets

Only Evan has the required auth for this script, but only Evan did the programming so that's okay. Never did figure out how to safely share this auth.

Please don't copy files to git from the gdrive by hand. Git must exactly match what's in the gdrive to avoid confusion, and it's too easy for copying things by hand to mess that up. Also, the script will overwrite manual changes.