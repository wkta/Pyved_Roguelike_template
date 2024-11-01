# ------
# engine-related code, do not modify!
# --------

registry = set()
libname_to_alias_mapping = dict()

def get_alias(origin_lib_name):
    return libname_to_alias_mapping[origin_lib_name]

def has_registered(origin_lib_name):
    return origin_lib_name in libname_to_alias_mapping

def register_lib(alias, libname, value):  # handy for dependency injection
    global registry, libname_to_alias_mapping
    libname_to_alias_mapping[libname] = alias
    if alias in registry:
        raise KeyError(f'Cannot register lib "{alias}" more than once!')
    globals()[alias] = value
    registry.add(alias)


# ------
# custom code the gamedev added
# --------
gameover_msg = None
game_running = 0
font_obj = None

END_MSG = "Game over! Press space to restart"
CELL_SIZE_PX = 30  # in pixels
DELAY_INTER_MV = 0.15  # sec, the lower the value, the fastest the pace of the game
NB_COLUMNS = 25
NB_ROWS = 19
INIT_DIRECTION = 1
INIT_SNAKE_MODEL = ((7, 2), (7, 3), (7, 4))
