
import pygame, random

from SETTINGS import *
from MAPS import *

class PLAYER():
    def __init__(self, MAIN_WINDOW, SCREEN):
        self.MAIN_WINDOW = MAIN_WINDOW
        self.SCREEN = SCREEN

        self.ANIMATIONS = False
        self.NAMETAGS = False
        self.FONT_SIZE = 32
        self.USERNAME = "Oyuncu"

        self.DIRECTION = "RIGHT"
        self.x = 0
        self.y = 0
        self.DEAD = False

        self.IMAGE = pygame.transform.scale(pygame.image.load(PATH_TO_THEMES+"tema"+str(self.MAIN_WINDOW.SelectedTheme)+"/oyuncu.png").convert_alpha(), (self.MAIN_WINDOW.GRID, self.MAIN_WINDOW.GRID))
        self.PLAYER_RIGHT = pygame.transform.flip(self.IMAGE, False, False)
        self.PLAYER_LEFT = pygame.transform.flip(self.IMAGE, True, False)

    def UPDATE_SCALE(self, w, h):
        self.IMAGE = pygame.transform.scale(self.IMAGE, (w, h))
        self.PLAYER_RIGHT = pygame.transform.flip(self.IMAGE, False, False)
        self.PLAYER_LEFT = pygame.transform.flip(self.IMAGE, True, False)

    def MOVE(self, event):
        X = self.x//self.MAIN_WINDOW.GRID
        Y = self.y//self.MAIN_WINDOW.GRID
        C = self.MAIN_WINDOW.CURRENT_MAP
        G = self.MAIN_WINDOW.GRID

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and MAPS[C][Y-1][X] != "W":
                #self.DIRECTION = "UP"
                if self.ANIMATIONS == True:
                    self.ANIMATION(0, -1)
                else:
                    self.y -= G
                #SFX_Player_Move.play()
            if event.key == pygame.K_a and MAPS[C][Y][X-1] != "W":
                self.DIRECTION = "LEFT"
                if self.ANIMATIONS == True:
                    self.ANIMATION(-1, 0)
                else:
                    self.x -= G
                #SFX_Player_Move.play()
            if event.key == pygame.K_s and MAPS[C][Y+1][X] != "W":
                #self.DIRECTION = "DOWN"
                if self.ANIMATIONS == True:
                    self.ANIMATION(0, 1)
                else:
                    self.y += G
                #SFX_Player_Move.play()
            if event.key == pygame.K_d and MAPS[C][Y][X+1] != "W":
                self.DIRECTION = "RIGHT"
                if self.ANIMATIONS == True:
                    self.ANIMATION(1, 0)
                else:
                    self.x += G
                #SFX_Player_Move.play()

    def SHOW(self):

        if self.DIRECTION == "RIGHT":
            self.SCREEN.blit(self.PLAYER_RIGHT, (self.x, self.y))
        if self.DIRECTION == "LEFT":
            self.SCREEN.blit(self.PLAYER_LEFT, (self.x, self.y))

        if self.NAMETAGS == True:
            self.NAMETAG_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", self.FONT_SIZE)
            self.NAMETAG = self.NAMETAG_FONT.render(self.USERNAME, True, (255, 255, 255))
            self.SCREEN.blit(self.NAMETAG, (self.x+self.MAIN_WINDOW.GRID//2-self.NAMETAG.get_width()//2, self.y-self.MAIN_WINDOW.GRID//2))

    def ANIMATION(self, x, y):
        G = self.MAIN_WINDOW.GRID

        for i in range(0, G):
            self.x += x
            self.y += y
            self.SHOW()
            pygame.display.update()


class RECTLANGE():
    def __init__(self, MAIN_WINDOW, SCREEN):
        self.MAIN_WINDOW = MAIN_WINDOW
        self.SCREEN = SCREEN

        self.ANIMATIONS = False
        self.x = 0
        self.y = 0

        self.IMAGE = pygame.transform.scale(pygame.image.load(PATH_TO_THEMES+"tema"+str(self.MAIN_WINDOW.SelectedTheme)+"/dortgen.png").convert_alpha(), (self.MAIN_WINDOW.GRID, self.MAIN_WINDOW.GRID))
        self.RECTLANGE = self.IMAGE

    def UPDATE_SCALE(self, w, h):
        self.IMAGE = pygame.transform.scale(self.IMAGE, (w, h))
        self.RECTLANGE = self.IMAGE

    def MOVE(self, event):
        X = self.x//self.MAIN_WINDOW.GRID
        Y = self.y//self.MAIN_WINDOW.GRID
        C = self.MAIN_WINDOW.CURRENT_MAP
        G = self.MAIN_WINDOW.GRID

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and MAPS[C][Y-1][X] != "W":
                if self.ANIMATIONS == True:
                    self.ANIMATION(0, -1)
                else:
                    self.y -= G
                #SFX_Rectlange_Move.play()
            if event.key == pygame.K_LEFT and MAPS[C][Y][X-1] != "W":
                if self.ANIMATIONS == True:
                    self.ANIMATION(-1, 0)
                else:
                    self.x -= G
                #SFX_Rectlange_Move.play()
            if event.key == pygame.K_DOWN and MAPS[C][Y+1][X] != "W":
                if self.ANIMATIONS == True:
                    self.ANIMATION(0, 1)
                else:
                    self.y += G
                #SFX_Rectlange_Move.play()
            if event.key == pygame.K_RIGHT and MAPS[C][Y][X+1] != "W":
                if self.ANIMATIONS == True:
                    self.ANIMATION(1, 0)
                else:
                    self.x += G
                #SFX_Rectlange_Move.play()

    def SHOW(self):
        self.SCREEN.blit(self.RECTLANGE, (self.x, self.y))

    def ANIMATION(self, x, y):
        G = self.MAIN_WINDOW.GRID

        for i in range(0, G):
            self.x += x
            self.y += y
            self.SHOW()
            pygame.display.update()


class ENEMY():
    def __init__(self, MAIN_WINDOW, SCREEN):
        self.MAIN_WINDOW = MAIN_WINDOW
        self.SCREEN = SCREEN
        self.MAIN_WINDOW.ENEMY_COUNT += 1

        self.ANIMATIONS = False
        self.NAMETAGS = False
        self.FONT_SIZE = 32

        self.x = 0
        self.y = 0
        self.DEAD = True

        self.IMAGE = pygame.transform.scale(pygame.image.load(PATH_TO_THEMES+"tema"+str(self.MAIN_WINDOW.SelectedTheme)+"/dusman.png").convert_alpha(), (self.MAIN_WINDOW.GRID, self.MAIN_WINDOW.GRID))
        self.ENEMY = self.IMAGE

    def UPDATE_SCALE(self, w, h):
        self.IMAGE = pygame.transform.scale(self.IMAGE, (w, h))
        self.ENEMY = self.IMAGE

    def SHOW(self):
        self.SCREEN.blit(self.ENEMY, (self.x, self.y))

        if self.NAMETAGS == True:
            self.NAMETAG_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", self.FONT_SIZE)
            self.NAMETAG = self.NAMETAG_FONT.render("Dusman", True, (255, 255, 255))
            self.SCREEN.blit(self.NAMETAG, (self.x+self.MAIN_WINDOW.GRID//2-self.NAMETAG.get_width()//2, self.y-self.MAIN_WINDOW.GRID//2))

    def MOVE(self, event, RECTLANGE, PLAYER):
        X = self.x//self.MAIN_WINDOW.GRID
        Y = self.y//self.MAIN_WINDOW.GRID
        C = self.MAIN_WINDOW.CURRENT_MAP
        G = self.MAIN_WINDOW.GRID

        if event.type == pygame.KEYDOWN:
            if RECTLANGE.x == self.x and RECTLANGE.y == self.y:
                pass
            else:
                D = self.MAIN_WINDOW.DIFFICULTY
                R = random.randint(1, D)
                M = random.randint(1, 4)
                if R == 1:
                    if M == 1 and MAPS[C][Y-1][X] != "W":
                        if RECTLANGE.x == self.x and RECTLANGE.y == self.y-G:
                            pass
                        else:
                            self.y -= G
                    elif M == 2 and MAPS[C][Y][X-1] != "W":
                        if RECTLANGE.x == self.x-G and RECTLANGE.y == self.y:
                            pass
                        else:
                            self.x -= G
                    elif M == 3 and MAPS[C][Y+1][X] != "W":
                        if RECTLANGE.x == self.x and RECTLANGE.y == self.y+G:
                            pass
                        else:
                            self.y += G
                    elif M == 4 and MAPS[C][Y][X+1] != "W":
                        if RECTLANGE.x == self.x+G and RECTLANGE.y == self.y:
                            pass
                        else:
                            self.x += G
                else:
                    if PLAYER.y < self.y and MAPS[C][Y-1][X] != "W":
                        if self.x == RECTLANGE.x and self.y-G == RECTLANGE.y:
                            pass
                        else:
                            self.y -= G
                    elif PLAYER.x < self.x and MAPS[C][Y][X-1] != "W":
                        if self.x-G == RECTLANGE.x and self.y == RECTLANGE.y:
                            pass
                        else:
                            self.x -= G
                    elif PLAYER.y > self.y and MAPS[C][Y+1][X] != "W":
                        if self.x == RECTLANGE.x and self.y+G == RECTLANGE.y:
                            pass
                        else:
                            self.y += G
                    elif PLAYER.x > self.x and MAPS[C][Y][X+1] != "W":
                        if self.x+G == RECTLANGE.x and self.y == RECTLANGE.y:
                            pass
                        else:
                            self.x += G

class WALL():
    def __init__(self, x, y, MAIN_WINDOW, SCREEN):
        self.MAIN_WINDOW = MAIN_WINDOW
        self.SCREEN = SCREEN
        
        self.x = x * self.MAIN_WINDOW.GRID
        self.y = y * self.MAIN_WINDOW.GRID

        self.IMAGE = pygame.transform.scale(pygame.image.load(PATH_TO_THEMES+"tema"+str(self.MAIN_WINDOW.SelectedTheme)+"/duvar.png").convert_alpha(), (self.MAIN_WINDOW.GRID, self.MAIN_WINDOW.GRID))
        self.WALL = self.IMAGE

        self.SCREEN.blit(self.WALL, (self.x, self.y))

class WALL_UNDER():
    def __init__(self, x, y, MAIN_SCREEN, SCREEN):
        self.MAIN_WINDOW = MAIN_WINDOW
        self.SCREEN = SCREEN
        
        self.x = x * self.MAIN_WINDOW.GRID
        self.y = y * self.MAIN_WINDOW.GRID

        self.IMAGE = pygame.transform.scale(pygame.image.load(PATH_TO_THEMES+"tema"+str(self.MAIN_WINDOW.SelectedTheme)+"/duvar_alt.png").convert_alpha(), (self.MAIN_WINDOW.GRID, self.MAIN_WINDOW.GRID))
        self.WALL_UNDER = self.IMAGE

        self.SCREEN.blit(self.WALL_UNDER, (self.x, self.y))

class DIALOG():
    def __init__(self, FULL_TEXT, TEXT_COLOR, FONT, FONT_SIZE, BACKGROUND_COLOR, OUTLINE_COLOR, MAIN_WINDOW, SCREEN):
        self.MAIN_WINDOW = MAIN_WINDOW
        self.SCREEN = SCREEN
        self.FULL_TEXT = FULL_TEXT
        self.FONT = pygame.font.Font(PATH_TO_FONTS+FONT+".ttf", FONT_SIZE)
        self.BACKGROUND_COLOR = BACKGROUND_COLOR
        self.OUTLINE_COLOR = OUTLINE_COLOR
        self.TEXT_COLOR = TEXT_COLOR

        self.HEIGHT = 200
        self.PADDING = 5
        
        self.x = self.PADDING
        self.y = RESOLUTION[1]+self.PADDING-self.HEIGHT
        self.w = RESOLUTION[0]-self.PADDING*2
        self.h = self.HEIGHT-self.PADDING*2

        self.BOX = pygame.Rect(self.x, self.y, self.w, self.h)
        self.BOX_OUTLINE = pygame.Rect(0, RESOLUTION[1]-self.HEIGHT, RESOLUTION[0], self.HEIGHT)

        self.MAIN_WINDOW.TIP_COUNT += 1

    def SHOW(self, DELAY):
        x = 0
        while x < len(self.FULL_TEXT)+1:
            pygame.draw.rect(self.SCREEN, self.OUTLINE_COLOR, self.BOX_OUTLINE)
            pygame.draw.rect(self.SCREEN, self.BACKGROUND_COLOR, self.BOX)
            self.TEXT = self.FONT.render(self.FULL_TEXT[0:x], True, self.TEXT_COLOR)
            self.SCREEN.blit(self.TEXT, (self.PADDING*20, self.BOX.y+self.BOX.h//2-self.TEXT.get_height()//2))
            x += 1
            pygame.display.update()
            pygame.time.delay(DELAY)


class BUTTON():
    def __init__(self, TEXT, FONT, FONT_SIZE, BUTTON_COMMAND, BUTTON_WIDTH, BUTTON_HEIGHT, COLOR_1, COLOR_2, LINE_X, LINE_Y, MAIN_WINDOW, SCREEN):
        self.SCREEN = SCREEN
        self.MAIN_WINDOW = MAIN_WINDOW
        self.BUTTON_COMMAND = BUTTON_COMMAND
        self.BUTTON_WIDTH = BUTTON_WIDTH
        self.BUTTON_HEIGHT = BUTTON_HEIGHT
        self.PAD_X = BUTTON_WIDTH + BUTTON_WIDTH / 4
        self.PAD_Y = BUTTON_HEIGHT + BUTTON_HEIGHT / 4
        self.COLOR_1 = COLOR_1
        self.COLOR_2 = COLOR_2

        self.LINE_X = LINE_X
        self.LINE_Y = LINE_Y

        self.FONT = pygame.font.Font(PATH_TO_FONTS+FONT+".ttf", FONT_SIZE)

        self.COLOR = self.COLOR_1
        self.RECT = pygame.Rect(RESOLUTION[0]//2-self.BUTTON_WIDTH//2+self.PAD_X*self.LINE_X, RESOLUTION[1]//2-self.BUTTON_HEIGHT//2+self.PAD_Y*self.LINE_Y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.TEXT = self.FONT.render(TEXT, True, (255, 255, 255))

    def SHOW(self):
        pygame.draw.rect(self.SCREEN, self.COLOR, self.RECT)
        self.SCREEN.blit(self.TEXT, (RESOLUTION[0]//2-self.TEXT.get_width()//2+self.PAD_X*self.LINE_X, RESOLUTION[1]//2-self.TEXT.get_height()//2+self.PAD_Y*self.LINE_Y))

    def COLLIDE(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.RECT.collidepoint(event.pos):
                self.COLOR = self.COLOR_2
            else:
                self.COLOR = self.COLOR_1

    def COMMAND(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(event.pos):
            self.BUTTON_COMMAND()


class MENU():
    def __init__(self, TITLE, MESSAGE, COLOR_1, COLOR_2, MAIN_WINDOW, SCREEN, BACKGROUND=False):
        self.SCREEN = SCREEN
        self.MAIN_WINDOW = MAIN_WINDOW
        self.BACKGROUND = BACKGROUND

        self.TITLE_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", 75)
        self.MESSAGE_FONT = pygame.font.Font(PATH_TO_FONTS+"Roboto.ttf", 20)

        self.TITLE = self.TITLE_FONT.render(TITLE, True, COLOR_1)
        self.MESSAGE = self.MESSAGE_FONT.render(MESSAGE, True, COLOR_2)

    def CREATE_BUTTONS(self, ID, TEXT, FONT, FONT_SIZE, WIDTH, HEIGHT, COLOR_1, COLOR_2, LINE_X, LINE_Y, MAIN_WINDOW):
        self.BUTTON_COUNT = len(TEXT)
        for i in range(0, self.BUTTON_COUNT):
            vars(self)["BUTTON_"+str(i+1)] = BUTTON(ID[i], TEXT[i], FONT[i], FONT_SIZE[i], WIDTH[i], HEIGHT[i], COLOR_1[i], COLOR_2[i], LINE_X[i], LINE_Y[i], self.MAIN_WINDOW, self.SCREEN)

    def SHOW(self):
        if self.BACKGROUND == False:
            self.SCREEN.fill(BLACK)

        self.SCREEN.blit(self.TITLE, (RESOLUTION[0]//2-self.TITLE.get_width()//2, 128))
        self.SCREEN.blit(self.MESSAGE, (RESOLUTION[0]//2-self.MESSAGE.get_width()//2, 214))

        try:
            for i in range(0, self.BUTTON_COUNT):
                vars(self)["BUTTON_"+str(i+1)].SHOW()
        except:
            pass

        pygame.display.update()

        event = pygame.event.wait()

        try:
            for i in range(0, self.BUTTON_COUNT):
                vars(self)["BUTTON_"+str(i+1)].COLLIDE(event)
        except:
            pass

        try:
            for i in range(0, self.BUTTON_COUNT):
                vars(self)["BUTTON_"+str(i+1)].COMMAND(event)
        except:
            pass

        pygame.display.update()
