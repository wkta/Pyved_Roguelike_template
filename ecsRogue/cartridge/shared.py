from pathlib import Path

from . import glvars


GAME_VER = "1.1"
pyv = glvars.pyv
GameStates = pyv.enum(
    'TitleScreen', 'Explore'
)


# ----------------------------------
#   + All that is related to Monsters +
# ----------------------------------

# Below you'll find a nice example of how you can use the `pyv.enum_from_n` built-in function.
# Assuming you call it with the parameters below, then
# monster_types.inv_map would be:
# {8: 'Rat', 9: 'BossRat', ... }
monster_types = pyv.enum_from_n(
    8, 'Rat', 'BossRat', 'Dog',
    Goblin=16,
    MageGoblin=18,
    Scorpion=35,
    FireBeetle=42,
    Skeleton=48,
    ShroudedDeath=54,
    Ghost=57
)  # now, remember you can use monster_types.all_codes later on

monster_dmg_amount = {
    -1: 8,  # the default dmg amount is 8 HP, this is used only if the monster_type isnt found below
    monster_types.Rat: 2,
    monster_types.MageGoblin: 10,
    monster_types.FireBeetle: 12,
    monster_types.Scorpion: 15,
    monster_types.Ghost: 18,
    monster_types.ShroudedDeath: 24
}

monster_hitpoints = {
    -1: 10,  # default hp amount
    monster_types.Rat: 5,
    monster_types.Ghost: 25,
    monster_types.ShroudedDeath: 40
}

MAX_MONSTERS = 7
MONSTERS = None  # will store the spritesheet after game initialization


# print exceptions in GUI only in debug mode
# (useful for debugging highscore local web storage when there is no terminal)
IS_DEBUG = True  # check if we can use __debug__ with pyved and pygbag
show_input = False
user_name_input = None
user_name = None

fonts = {}
pixelart_font = None  # stores a special object pyv.gui.ImgBasedFont
TEXT_UPSCALING = True
FONT_SIZE_SMALL = 24
FONT_SIZE_MEDIUM = 38
FONT_SIZE_LARGE = 55
# Need a flag to handle differently when game is run in desktop mode or in a web browser
IS_WEB = False
# local storage in web version for high score table
if __import__("sys").platform == "emscripten":
    IS_WEB = True


# Highscore utils
# there are 3 implementations of highscore:
# 1. using GameJolt API for desktop mode
#    * unfortunately it doesn't work yet when run in the web browser
#    * API does the all heavy lifting
#    * scores are kept online and there is one common score board for all users no matter when the game is run
# 2. Local storage in web browser
#    * uses the build in Web browser functionality called 'local storage'
#    * highscore table is kept in your browser locally and bind to url (domain:port, eg.: pyvm.kata.games, localhost:8000, 127.0.0.1:8000) so it's decentralized
#    * it can be viewed and edited in browser (e.g. in Chrome: Developer Tools -> Applications -> Storage -> Local storage -> url)
# 3. Local storage stub
#    * stubs local storage to make it easier to debug
#    * when enabled, you can run game in desktop mode and still test it (view console, quick restart, etc.)
#    * the data is kept in global dictionary (HIGHSCORE_STUB) instead of actual browser local storage
#    * it's restored to original state with each game run

# Local storage stub for testing highscore in desktop mode
USE_HIGHSCORE_STUB = True
HIGHSCORE_STUB = {
    # "Ula": {"level": 3, "stored_timestamp": "1712989042.312", "game_ver": "0.9", "time_played": "n/a"},
    # "Hubi": {"level": 2, "stored_timestamp": "1712988963.14", "game_ver": "0.9", "time_played": "n/a"},
    # "Master": {"level": 4, "stored_timestamp": "1712989177.01", "game_ver": "0.9", "time_played": "n/a"},
    # "Noob": {"level": 2, "stored_timestamp": "1712989177.01", "game_ver": "0.9", "time_played": "n/a"},
    # "Ela": {"level": 1, "stored_timestamp": "1712989127.556", "game_ver": "0.9", "time_played": "n/a"},
    # "Ala": {"level": 1, "stored_timestamp": "1712988973.809", "game_ver": "0.9", "time_played": "n/a"},
}
if USE_HIGHSCORE_STUB:
    IS_WEB = True

# GameJolt API
# go to https://gamejolt.com/
# create account
# crate new game
GAME_ID = ""  # <YOUR_GAME_ID>
PRIVATE_KEY = ""  # <YOUR_KEY>
gamejoltapi = None
TEST_SCORE_TABLE_ID = 0  # create test score table and enter it's id here
PROD_SCORE_TABLE_ID = 0  # open default score table and enter it's id here
SCORE_TABLE = []
SCORES = {}
NO_TOP_SCORES = 10

screen = None
is_game_over = False
status_label = None  # deprecated
status_info = None  # line of text that will be displayed at the top, when playing

game_over_msgs_hs = [
    "Game Over",
    'You reached level : {level_count}',
    'Provide your name for highscore table',
    'Press [ESC] to cancel or [ENTER] to accept',
    'Name:'
]
game_over_msgs = [
    "Game Over",
    'You reached level: {level_count}',
    'Press {exit}[SPACE] to restart'.format(exit=('' if IS_WEB or USE_HIGHSCORE_STUB else '[ESC] to quit or ')),
]

help_msgs = []
help_msgs.append("[ARROWS] - to move")
help_msgs.append("[s] - show highscore")
if not IS_WEB or USE_HIGHSCORE_STUB:
    help_msgs.append('[F12] - screenshot')
    help_msgs.append('[ESC], [q] - exit')
help_msgs.append("")
help_msgs.append("*** CHEATS/DEBUG ***")
help_msgs.append("[SPACE] - new maze")
help_msgs.append("[m] - show enemies")
help_msgs.append("[a] - activate enemies")
help_msgs.append("[p] - show enemies path")
help_msgs.append("[e] - show exit")
help_msgs.append("[o] - show potions")

SCREENSHOT_FOLDER = Path("..") / "screenshots"

VISION_RANGE: int = 4
fov_computer = None

random_maze = None
game_state = {
    "visibility_m": None,
    "enemies_pos2type": dict(),
    # "equipped_spell": None,
    # "owned_spells": set()
}

CELL_SIDE = 32  # px
MAZE_SIZE = (22, 22)
WALL_COLOR = (8, 8, 24)
HIDDEN_CELL_COLOR = (24, 24, 24)
# user_name input label colors
COLOR_INACTIVE = 'yellow4'  # shared.HIDDEN_CELL_COLOR # pygame.Color('lightskyblue3')
COLOR_ACTIVE = 'yellow'  # pygame.Color('dodgerblue2')

SCR_WIDTH = 960
SCR_HEIGHT = 720

# extra const
GRID_REZ = (CELL_SIDE, CELL_SIDE)

AVATAR = None

PLAYER_DMG = 10
PLAYER_HP = 100

TILESET = None
# two glvars for a quick n dirty bugfix (js web cxt)
joker_tile = None
pot_tile = None
exit_tile = None

FLOOR_TILE_RANKS = [898, 905, 912, 326, 334, 335]
FLOOR_TILE_RANK = 898
EXIT_TILE_RANK = 1092
UNKNOWN_TILE_RANK = 811
POISON_TILE_RANK = 810
HEAL_TILE_RANK = 783
wall_type = "big_wall"
WALLS_TERRAIN_SETS = {
    "big_fence": {
        "0000": 53,
        "1000": 22,
        "0100": 21,
        "0010": 22,
        "0001": 49,
        "1100": 47,
        "0110": 19,
        "0011": 20,
        "1001": 48,
        "1010": 22,
        "0101": 50,
        "1110": 23,
        "0111": 24,
        "1011": 52,
        "1101": 51,
        "1111": 53
    },
    "small_fence": {
        "0000": 109,
        "1000": 78,
        "0100": 77,
        "0010": 78,
        "0001": 105,
        "1100": 103,
        "0110": 75,
        "0011": 76,
        "1001": 104,
        "1010": 78,
        "0101": 106,
        "1110": 79,
        "0111": 80,
        "1011": 108,
        "1101": 107,
        "1111": 109
    },
    "big_wall": {
        "0000": 165,
        "1000": 134,
        "0100": 133,
        "0010": 134,
        "0001": 161,
        "1100": 159,
        "0110": 131,
        "0011": 132,
        "1001": 160,
        "1010": 134,
        "0101": 162,
        "1110": 135,
        "0111": 136,
        "1011": 164,
        "1101": 163,
        "1111": 165
    }
}
POTION_DMG = 20
MAX_POTIONS = 4
SHOW_HELP = False
SHOW_HIGHSCORE = False
# CHEATS/DEBUG
EXIT_VISIBLE = False
ALL_POTIONS_VISIBLE = False
ALL_MONSTERS_VISIBLE = False
ALL_MONSTERS_PATH_VISIBLE = False
# if any of the above features is used, highscore won't be saved
CHEAT_USED = False

walkable_cells = []  # List to store walkable cells
level_count = 1
messages = []

sys_iterator = 0
