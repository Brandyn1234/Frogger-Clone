import pygame

# resolution / frames
WIDTH = 480
HEIGHT = 720
FPS = 60

font_name = pygame.font.match_font('arial')

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (148, 0, 211)
ORANGE = (230, 110, 25)
BLUE = (27, 36, 118)

# car variables 
POS_CARSPEED = 2
NEG_CARSPEED = -1
INSTANCE_COUNT = 0
BOX_WIDTH = 30

# spacing for cars/logs
SPACING = 60
SPACING_2 = 240
SPACING_3 = 120
SPACING_4 = 180

# logs width rows 1 & 2
LOG_WIDTH = 90

# logs width row 3
LOG_WIDTH2 = 160

# logs speed
NEG_LOGSPEED = -1
POS_LOGSPEED = 1
FAST_LOGSPEED = 3
