# Pyved_Roguelike_template

Sample project based on [Pyved engine](https://github.com/pyved-solution/pyved-engine) using ECS Roguelike template

![screenshot](/screenshots/screenshot.png)

The project you see now is basically a spin-off from one of many game templates you can find in the [General game templates index](https://github.com/pyved-solution/game-templates-index).

Try the game online, in your browser!
[PLAY!](https://pyvm.kata.games/play/ecsRogue)

## Features

* from original project
  * random map generation
  * A* path finding for monsters
  * player's line of sight
  * implemented using **Entity Component System (ECS)**
* EXTRA features
  * simple UI
    * status bar
    * help panel
    * action log
  * difficulty progression (with each level +1 monster)
  * highscore list
  * random tiles for walls and floor
  * some debug tools
    * show exit
    * show potions with it's type
    * show all monsters
    * activate all monsters
    * show monster paths
    * take screenshot

## Known bugs

* 2 or more monsters sometimes occupy the same location
* after loading a new level, sometimes player starts on monster position
* monsters hit 2 times per one player turn
* action log is not cleared as expected when new game starts

## Ideas for future

* ✅ ~~Highscore table~~
* ✅ ~~use walls tiles from `tileset.png` instead of black rectangle~~
* ✅ ~~add more monster types~~
* make fight more entertaining
* switch font to monospace pixel art
* add sounds (music and sfx)
* make UI more appealing (icons, colors, menus)

## Install the project

```bash
# create venv
python3 -m venv .venv

# activate the venv
# on Linux/MacOS:
source .venv/bin/activate
# on Windows:
.venv\Scripts\activate
```
Once done, you have to install the dependency (game engine), you will probably need the latest (dev build) version of the game engine, not the version that can be found via PyPI.
```bash
# let us clone the latest version of pyved-engine, install it
cd ..
git clone https://github.com/pyved-solution/pyved-engine.git
cd pyved-engine
pip install -e .

# go back to the folder where your game is stored
cd ../Pyved_Roguelike_template
```

## Run

Local execution:

```bash
# using pyved command line tools
pyv-cli play ecsRogue
```

If there is a problem with the built-in command line tool (`pyv-cli`) you may also run the launcher script:

```bash
cd ecsRogue
python launch_game.py
```
These two commands are equivalent.

## Deploying using a web/cloud service

### To [kata.games](https://kata.games/)

Warning: that step may require fixing, as it doen't always working with the latest pyved-engine version. In the near future we will ensure that only stable versions of `pyved-engine` are used to write demos and that these versions are supported by our cloud player solution.

```bash
pyv-cli share ecsRogue
```

## Credits

Code:
- [moonbak](https://github.com/wkta/)
- [HubertReX](https://github.com/HubertReX/)

Assets created by:
- [Pixel-boy](https://pixel-boy.itch.io/)
- [AAA](https://www.instagram.com/challenger.aaa/?hl=fr)

and:
[@JoeCreates](https://x.com/JoeCreates) for monsters.

Patreon:<br>
[https://www.patreon.com/pixelarchipel](https://www.patreon.com/pixelarchipel)
