import pygame
from pygame.locals import *
# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Tetris"
FPS = 25 # FRAME RATE

# SCREEN
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

# FRAME RATE MOVEMENT - HOLDING DOWN KEYS
MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

# PADDING LEFT, RIGHT, and TOP
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

# COLORS        R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

# BOARD GAME COLORS
BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) # each color must have light color


# ********* FONT *********
FONT_FILE = "tetris/assets/fonts/freesansbold.ttf"
FONT_SMALL = 18
FONT_LARGE = 100

# SOUND
TETRIS_0_MUSIC = "tetris/assets/sounds/0_tetris.mid"
TETRIS_1_MUSIC = "tetris/assets/sounds/1_tetris.mid"

# ********* TEXT *********
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# ********* KEYS *********
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# ********* SCENES *********
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# ********* LEVELS *********
BASE_LEVELS = 5


# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# ********* PHASES *********
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6


# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# ********* STATS *********
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# ********* HUD *********
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# Tetris SIZE
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

# Tetris - GEOMETRIC SHAPES
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]


Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]


I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]


O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]


J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]


L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]


T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]


SHAPES = {'S': S_SHAPE_TEMPLATE, 
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}


# ********* DIALOG *********
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"



pygame.font.init()
font = pygame.font
pygame.font.SysFont("freesansbold.ttf", 18)

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
