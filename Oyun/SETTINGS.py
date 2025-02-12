
import pygame

# AYARLAR

RESOLUTION = (1152, 768)

# EKRAN

SCREEN = pygame.display.set_mode(RESOLUTION)#, pygame.FULLSCREEN)

# KONUMLAR

PATH_TO_DATA = "data/"
PATH_TO_ASSETS = PATH_TO_DATA + "assets/"
PATH_TO_FONTS = PATH_TO_ASSETS + "fonts/"
PATH_TO_SOUNDS = PATH_TO_ASSETS + "sounds/"
PATH_TO_THEMES = PATH_TO_ASSETS + "themes/"

# RENKLER

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 0)
CYAN = (0, 255, 255)
GRAY = (127, 127, 127)
DARK_GRAY = (63, 63, 63)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
