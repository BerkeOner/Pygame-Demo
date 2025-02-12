
import pygame, sys, random, os

sys.path.append("data/modules")

from SETTINGS import *
from SPRITES import *
from MAPS import *

# Pencereyi Ortala

os.environ['SDL_VIDEO_CENTERED'] = '1'

# PyGame

"Ayarla"
pygame.init()

"Ses Efektleri"
pygame.mixer.init()

"Muzik"
pygame.mixer.music.load(PATH_TO_SOUNDS+"muzik.wav")

"Muzik Sinirsiz Olsun"
pygame.mixer.music.play(-1)

# SES EFEKTLERI

"Oyuncu Hareketi"
SFX_Player_Move = pygame.mixer.Sound(PATH_TO_SOUNDS+"oyuncu_hareket.wav")

"Dortgen Hareketi"
SFX_Rectlange_Move = pygame.mixer.Sound(PATH_TO_SOUNDS+"dortgen_hareket.wav")

"Oldurme"
SFX_Kill = pygame.mixer.Sound(PATH_TO_SOUNDS+"alma.wav")

"Toplama"
SFX_Coin = pygame.mixer.Sound(PATH_TO_SOUNDS+"alma.wav")

"Seviye Gecme"
SFX_Clear = pygame.mixer.Sound(PATH_TO_SOUNDS+"seviye_gecme.wav")

"Kaybetme"
SFX_Defeat = pygame.mixer.Sound(PATH_TO_SOUNDS+"kaybetme.wav")

"Tıklama"
SFX_Click = pygame.mixer.Sound(PATH_TO_SOUNDS+"klik.wav")

# YAZI TIPLERI

"Buton"
BUTTON_FONT = pygame.font.Font(PATH_TO_FONTS+"Roboto.ttf", 25)

"Seviye Gecme"
CLEAR_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", 45)

"Kaybetme"
DEFEAT_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", 75)

"Seviye"
LEVEL_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", 30)

"Bilgi"
TIP_FONT = pygame.font.Font(PATH_TO_FONTS+"Roboto.ttf", 20)

"Isim Etiketleri"
NAMETAG_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", 35)

# Ana Pencere

class MainWindow():
    def __init__(self):
        # Ayarlar

        "Tile Boyutu"
        self.GRID = 128

        "Ilk Acildiginda Yeniden Baslat"
        self.RESTART = True

        "Animasyonlar"
        self.Animations = False

        "Izgara"
        self.GRIDisON = False

        "Secili Tema"
        self.SelectedTheme  = 0

        """Oyun Modu
            0: Isim Yaz
            1: Oyunda
            2: Ana Menu
            3: Market
            4: Ayarlar
            5: Seviyeler"""
        self.GAMEMODE = 1

        "Yeniden Baslatmadan Sonra Menuyu Ac"
        self.ToggleMenu = 0

        "Dusman Miktari"
        self.ENEMY_COUNT = 0

        "Suanki Harita"
        self.CURRENT_MAP = 1

        "Uygulama Calisiyor"
        self.APP_RUN = True

        "FPS"
        self.FPS = pygame.time.Clock()

        "Zorluk"
        self.DIFFICULTY = 1

        "Alt Bilgi Mesajlari Goster"
        self.SHOW_TIPS = True

        "Alt Bilgi Mesajlari Miktari"
        self.TIP_COUNT = 0

        "."
        
        try:
            f = open(PATH_TO_DATA+"coins.txt", "r")
            self.Score = int(f.read())
            f.close()
        except:
            f = open(PATH_TO_DATA+"coins.txt", "w+")
            self.Score = 250
            f.write(str(self.Score))
            f.close()

        "Class Spriteları"
        self.SPRITES()

        "Resim Spriteları"
        self.Sprites()

        "Oyuncu Adi"
        self.P1.USERNAME = "Oyuncu"

        "Seviyeyi Hazirla"
        self.SetLevel()

        "Butonlar Ve Menüler"
        self.Buttons()

        "Başlat"
        self.Main()

    def SPRITES(self):
        self.P1 = PLAYER(self, SCREEN)
        self.R1 = RECTLANGE(self, SCREEN)

        self.E1 = ENEMY(self, SCREEN)
        self.E2 = ENEMY(self, SCREEN)
        self.E3 = ENEMY(self, SCREEN)
        self.E4 = ENEMY(self, SCREEN)
        self.E5 = ENEMY(self, SCREEN)
        self.E6 = ENEMY(self, SCREEN)
        self.E7 = ENEMY(self, SCREEN)
        self.E8 = ENEMY(self, SCREEN)
        self.E9 = ENEMY(self, SCREEN)
        self.E10 = ENEMY(self, SCREEN)

    def SetLevel(self):
        try: self.SELECTABLE()
        except: pass
        self.Once_Lvl_Up = 0
        self.C1_Taken = False
        self.C1x = 0
        self.C1y = 0
        self.P1.DIRECTION = "RIGHT"
        if 0 < self.CURRENT_MAP < 2: # Tutorial: 1
            self.DIFFICULTY = 1
            self.GRID = 128
            self.P1.x = self.GRID
            self.P1.y = self.GRID
            self.R1.x = self.GRID
            self.R1.y = self.GRID
            for i in range(0, self.ENEMY_COUNT):
                setattr(getattr(self, "E"+str(i+1)), "x", 0)
                setattr(getattr(self, "E"+str(i+1)), "y", 0)
                setattr(getattr(self, "E"+str(i+1)), "DEAD", True)
            self.E1.x = self.GRID*2
            self.E1.y = self.GRID*4
            self.E1.DEAD = False
        if 1 < self.CURRENT_MAP < 3: # Tutorial: 2
            self.DIFFICULTY = 1
            self.GRID = 128
            self.P1.x = self.GRID
            self.P1.y = self.GRID*4
            self.R1.x = self.GRID
            self.R1.y = self.GRID*4
            for i in range(0, self.ENEMY_COUNT):
                setattr(getattr(self, "E"+str(i+1)), "x", 0)
                setattr(getattr(self, "E"+str(i+1)), "y", 0)
                setattr(getattr(self, "E"+str(i+1)), "DEAD", True)
            self.E1.x = self.GRID*4
            self.E1.y = self.GRID*3
            self.E1.DEAD = False
            self.E2.x = self.GRID*7
            self.E2.y = self.GRID
            self.E2.DEAD = False
        if 2 < self.CURRENT_MAP < 4: # Tutorial: 3
            self.DIFFICULTY = 1
            self.GRID = 128
            self.P1.x = self.GRID*4
            self.P1.y = self.GRID*4
            self.R1.x = self.GRID*4
            self.R1.y = self.GRID*4
            for i in range(0, self.ENEMY_COUNT):
                setattr(getattr(self, "E"+str(i+1)), "x", 0)
                setattr(getattr(self, "E"+str(i+1)), "y", 0)
                setattr(getattr(self, "E"+str(i+1)), "DEAD", True)
            self.E1.x = self.GRID*2
            self.E1.y = self.GRID
            self.E1.DEAD = False
            self.E2.x = self.GRID*6
            self.E2.y = self.GRID
            self.E2.DEAD = False
        if 3 < self.CURRENT_MAP < 7: # Beginner: 4, 5, 6
            self.DIFFICULTY = 2
            self.GRID = 96
            if self.CURRENT_MAP == 4 or self.CURRENT_MAP == 5:
                self.P1.x = self.GRID*2
                self.P1.y = self.GRID
                self.R1.x = self.GRID*2
                self.R1.y = self.GRID
            if self.CURRENT_MAP == 6:
                self.P1.x = self.GRID*2
                self.P1.y = self.GRID*2
                self.R1.x = self.GRID*2
                self.R1.y = self.GRID*2
            for i in range(0, self.ENEMY_COUNT):
                setattr(getattr(self, "E"+str(i+1)), "x", 0)
                setattr(getattr(self, "E"+str(i+1)), "y", 0)
                setattr(getattr(self, "E"+str(i+1)), "DEAD", True)
            self.E1.x = 0
            self.E1.y = 0
            self.E1.DEAD = False
            self.E2.x = 0
            self.E2.y = 0
            self.E2.DEAD = False
            self.E3.x = 0
            self.E3.y = 0
            self.E3.DEAD = False
            self.E4.x = 0
            self.E4.y = 0
            self.E4.DEAD = False
        if 6 < self.CURRENT_MAP < 10: # Advanced: 7, 8, 9
            self.DIFFICULTY = 3
            self.GRID = 64
            if self.CURRENT_MAP == 7:
                self.P1.x = self.GRID*7
                self.P1.y = self.GRID*5
                self.R1.x = self.GRID*7
                self.R1.y = self.GRID*5
            if self.CURRENT_MAP == 8:
                self.P1.x = self.GRID*2
                self.P1.y = self.GRID*8
                self.R1.x = self.GRID*2
                self.R1.y = self.GRID*8
            if self.CURRENT_MAP == 9:
                self.P1.x = self.GRID*3
                self.P1.y = self.GRID*7
                self.R1.x = self.GRID*3
                self.R1.y = self.GRID*7
            for i in range(0, self.ENEMY_COUNT):
                setattr(getattr(self, "E"+str(i+1)), "x", 0)
                setattr(getattr(self, "E"+str(i+1)), "y", 0)
                setattr(getattr(self, "E"+str(i+1)), "DEAD", True)
            self.E1.x = 0
            self.E1.y = 0
            self.E1.DEAD = False
            self.E2.x = 0
            self.E2.y = 0
            self.E2.DEAD = False
            self.E3.x = 0
            self.E3.y = 0
            self.E3.DEAD = False
            self.E4.x = 0
            self.E4.y = 0
            self.E4.DEAD = False
            self.E5.x = 0
            self.E5.y = 0
            self.E5.DEAD = False
        if 9 < self.CURRENT_MAP: # Master: >10
            self.DIFFICULTY = 3
            self.GRID = 32
            self.P1.x = self.GRID
            self.P1.y = self.GRID
            self.R1.x = self.GRID
            self.R1.y = self.GRID
            for i in range(0, self.ENEMY_COUNT):
                setattr(getattr(self, "E"+str(i+1)), "x", 0)
                setattr(getattr(self, "E"+str(i+1)), "y", 0)
                setattr(getattr(self, "E"+str(i+1)), "DEAD", False)

        self.P1.UPDATE_SCALE(self.GRID, self.GRID)
        self.R1.UPDATE_SCALE(self.GRID, self.GRID)
        for i in range(0, self.ENEMY_COUNT):
            E = getattr(self, "E"+str(i+1))
            E.UPDATE_SCALE(self.GRID, self.GRID)
        self.Sprites()

    def ShowMap(self):
        x=y=0
        for row in MAPS[self.CURRENT_MAP]:
            for col in row:
                if col == "W":
                    SCREEN.blit(self.wall, (self.GRID*x, self.GRID*y))
                if col == " ":
                    SCREEN.blit(self.floor, (self.GRID*x, self.GRID*y))
                if MAPS[self.CURRENT_MAP][y-1][x] == " " and MAPS[self.CURRENT_MAP][y-2][x] == "W":
                    SCREEN.blit(self.wall_under, (self.GRID*x, self.GRID*(y-1)))
                x += 1
            y += 1
            x = 0

    def Sprites(self):
        self.BACKGROUND = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+"background.png"), (RESOLUTION[0], RESOLUTION[1]))
        path = PATH_TO_THEMES+"tema"+str(self.SelectedTheme)+"/"

        self.grid_piece = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+"grid.png").convert_alpha(), (self.GRID, self.GRID))

        self.PopUpTheme0 = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+"tema0goster.png").convert_alpha(), (self.GRID*3, self.GRID*3))
        self.PopUpTheme1 = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+"tema1goster.png").convert_alpha(), (self.GRID*3, self.GRID*3))
        self.PopUpTheme2 = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+"tema2goster.png").convert_alpha(), (self.GRID*3, self.GRID*3))
        self.PopUpTheme3 = pygame.transform.scale(pygame.image.load(PATH_TO_ASSETS+"tema0goster.png").convert_alpha(), (self.GRID*3, self.GRID*3))

        self.P1.IMAGE = pygame.transform.scale(pygame.image.load(path+"oyuncu.png").convert_alpha(), (self.GRID, self.GRID))
        self.P1.PLAYER_RIGHT = pygame.transform.flip(self.P1.IMAGE, False, False)
        self.P1.PLAYER_LEFT = pygame.transform.flip(self.P1.IMAGE, True, False)

        self.R1.IMAGE = pygame.transform.scale(pygame.image.load(path+"dortgen.png").convert_alpha(), (self.GRID, self.GRID))
        self.R1.RECTLANGE = self.R1.IMAGE

        for i in range(0, self.ENEMY_COUNT):
            vars(vars(self)["E"+str(i+1)])["IMAGE"] = pygame.transform.scale(pygame.image.load(path+"dusman.png").convert_alpha(), (self.GRID, self.GRID))
            vars(vars(self)["E"+str(i+1)])["ENEMY"] = vars(vars(self)["E"+str(i+1)])["IMAGE"]

        self.wall = pygame.transform.scale(pygame.image.load(path+"duvar.png").convert_alpha(), (self.GRID, self.GRID))
        self.floor = pygame.transform.scale(pygame.image.load(path+"yer.png").convert_alpha(), (self.GRID, self.GRID))
        self.coin = pygame.transform.scale(pygame.image.load(path+"para.png").convert_alpha(), (self.GRID, self.GRID))
        self.wall_under = pygame.transform.scale(pygame.image.load(path+"duvar_alt.png").convert_alpha(), (self.GRID, self.GRID))
        self.monster_under = pygame.transform.scale(pygame.image.load(path+"dusman_alt.png").convert_alpha(), (self.GRID, self.GRID))
        self.rectlange_under = pygame.transform.scale(pygame.image.load(path+"dortgen_alt.png").convert_alpha(), (self.GRID, self.GRID))

        pygame.display.set_icon(self.E1.IMAGE)
        pygame.display.set_caption('Oyun')

    def AddCoin(self, coins):
        f = open(PATH_TO_DATA+"coins.txt", "r")
        self.Score = int(f.read()) + int(coins)
        f.close()
        f = open(PATH_TO_DATA+"coins.txt", "w")
        f.write(str(self.Score))
        f.close()

    def CENTER_TEXT(self, txt):
        self.CENTERED = (RESOLUTION[0]//2-txt.get_width()//2, RESOLUTION[1]//2-txt.get_height()//2)

    def SET_PAGE(self, title, message):
        self.TITLE_FONT = pygame.font.Font(PATH_TO_FONTS+"Andy.ttf", 75)
        self.MESSAGE_FONT = pygame.font.Font(PATH_TO_FONTS+"Roboto.ttf", 20)

        self.TITLE = self.TITLE_FONT.render(title, True, (127, 127, 127))
        self.MESSAGE = self.MESSAGE_FONT.render(message, True, (127, 127, 127))

    def Buttons(self):
        self.BUTTON_4 = BUTTON("Geri", "Roboto", 25, lambda: (SCREEN.fill(BLACK), self.SET_GAMEMODE(2), SFX_Click.play()), 168, 64, ORANGE, CYAN, -2.3, -4.3, self, SCREEN)

        self.BUTTON_8 = BUTTON("Tamam", "Roboto", 25, lambda: (SCREEN.fill(BLACK), self.SET_GAMEMODE(2), SFX_Click.play()), 168, 64, ORANGE, PURPLE, 0, 1, self, SCREEN)

        self.BANNER = DEFEAT_FONT.render("OYUNUN ADI", True, (0, 255, 255))
        self.NICKNAMEBANNER = DEFEAT_FONT.render(self.P1.USERNAME, True, (255, 255, 255))

        self.PAGE_SETTINGS = MENU("Ayarlar", "Ayarlar Sayfasi", GRAY, GRAY, self, SCREEN)
        self.PAGE_SETTINGS.CREATE_BUTTONS(
                                         ("Animasyonlar", "İsim Etiketleri", "Izgara", "GERI"),
                                         ("Roboto", "Roboto", "Roboto", "Roboto"),
                                         (25, 25, 25, 25),
                                         (lambda: (SCREEN.fill(BLACK), self.SET_GAMEMODE(2), self.SET_ANIMATIONS(), SFX_Click.play()),
                                          lambda: (SCREEN.fill(BLACK), self.SET_GAMEMODE(2), self.SET_NAMETAGS(), SFX_Click.play()),
                                          lambda: (SCREEN.fill(BLACK), self.SET_GAMEMODE(2), self.SET_GRID_TOGGLE(), SFX_Click.play()),
                                          lambda: (SCREEN.fill(BLACK), self.SET_GAMEMODE(2), SFX_Click.play())),
                                         (256, 256, 256, 256),
                                         (64, 64, 64, 64),
                                         (ORANGE, ORANGE, ORANGE, ORANGE),
                                         (CYAN, CYAN, CYAN, CYAN),
                                         (0, 0, 0, 0),
                                         (-1, 0, 1, 2.5),
                                         self)

        self.PAGE_LEVELS_1 = MENU("Seviyeler", "Seviye Sayfasi", WHITE, WHITE, self, SCREEN)
        self.PAGE_LEVELS_1.CREATE_BUTTONS(
                                         ("Geri", "1", "2", "3", "4", "5", "6", "7", "8", "9", "<-", "->"),
                                         ("Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Andy", "Andy"),
                                         (20, 32, 32, 32, 32, 32, 32, 32, 32, 32, 20, 20),
                                         (lambda: (self.SET_GAMEMODE(2), SFX_Click.play()),
                                          lambda: (self.START_FROM_LEVEL(1), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(2), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(3), SFX_Click.play()),
                                          lambda: (self.START_FROM_LEVEL(4), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(5), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(7), SFX_Click.play()),
                                          lambda: (self.START_FROM_LEVEL(7), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(8), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(9), SFX_Click.play()),
                                          lambda: (SFX_Click.play()), lambda: (self.SET_GAMEMODE(5.2), SFX_Click.play())),
                                         (64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64),
                                         (64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64),
                                         (BLUE, RED, RED, RED, RED, RED, RED, RED, RED, RED, DARK_GRAY, BLUE),
                                         (CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, GRAY, CYAN),
                                         (-2, -1, 0, 1, -1, 0, 1, -1, 0, 1, -2, 2),
                                         (-2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2),
                                         self)

        self.PAGE_LEVELS_2 = MENU("Seviyeler", "Seviye Sayfasi", WHITE, WHITE, self, SCREEN)
        self.PAGE_LEVELS_2.CREATE_BUTTONS(
                                         ("Geri", "10", "11", "12", "13", "14", "15", "16", "17", "18", "<-", "->"),
                                         ("Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Roboto", "Andy", "Andy"),
                                         (20, 32, 32, 32, 32, 32, 32, 32, 32, 32, 20, 20),
                                         (lambda: (self.SET_GAMEMODE(2), SFX_Click.play()),
                                          lambda: (self.START_FROM_LEVEL(10), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(11), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(12), SFX_Click.play()),
                                          lambda: (self.START_FROM_LEVEL(13), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(14), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(15), SFX_Click.play()),
                                          lambda: (self.START_FROM_LEVEL(16), SFX_Click.play()), lambda: (self.START_FROM_LEVEL(17)), SFX_Click.play(), lambda: (self.START_FROM_LEVEL(18), SFX_Click.play()),
                                          lambda: (self.SET_GAMEMODE(5.1), SFX_Click.play()), lambda: (SFX_Click.play())),
                                         (64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64),
                                         (64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64),
                                         (BLUE, RED, RED, RED, RED, RED, RED, RED, RED, RED, BLUE, DARK_GRAY),
                                         (CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, CYAN, GRAY),
                                         (-2, -1, 0, 1, -1, 0, 1, -1, 0, 1, -2, 2),
                                         (-2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2),
                                         self)

        self.PAGE_MENU = MENU("OYUNUN ADI", "Ana Menüye Hosgeldin "+self.P1.USERNAME+"!", CYAN, CYAN, self, SCREEN, True)
        self.PAGE_MENU.CREATE_BUTTONS(
                                     ("OYNA", "MARKET", "AYARLAR", "KAPAT"),
                                     ("Roboto", "Roboto", "Roboto", "Roboto"),
                                     (25, 25, 25, 25),
                                     (lambda: (SCREEN.fill(BLACK),
                                               self.SET_GAMEMODE(5.1), SFX_Click.play()),
                                      lambda: (self.SET_GAMEMODE(3),
                                               self.SET_GRID(64),
                                               self.UPDATE_SCALE(self.P1, self.GRID, self.GRID,
                                                                 self.R1, self.GRID, self.GRID,
                                                                 "E", self.GRID, self.GRID),
                                               self.SET_CUR("Market-0"),
                                               self.SET_PLAYER_LOC(self.GRID, self.GRID*8),
                                               self.SET_RECTLANGE_LOC(self.GRID, self.GRID*8),
                                               SCREEN.fill(BLACK), SFX_Click.play()),
                                      lambda: (self.SET_GAMEMODE(4), SFX_Click.play()),
                                      lambda: (self.STOP_GAME(), SFX_Click.play())),
                                     (168, 168, 168, 168),
                                     (64, 64, 64, 64),
                                     (GREEN, ORANGE, DARK_GRAY, RED),
                                     (CYAN, CYAN, GRAY, ORANGE),
                                     (0, 0, 0, 0),
                                     (-1, 0, 1, 2),
                                     self)

    def SET_GAMEMODE(self, x):
        self.GAMEMODE = x

    def SET_GRID_TOGGLE(self):
        if self.GRIDisON == True:
            self.GRIDisON = False
        else:
            self.GRIDisON = True

    def UPDATE_SCALE(self, PLAYER, w1, h1,
                           RECTLANGE, w2, h2,
                           ENEMIES, w3, h3):
        PLAYER.UPDATE_SCALE(w1, h1)
        RECTLANGE.UPDATE_SCALE(w2, h2)
        for i in range(0, self.ENEMY_COUNT):
            getattr(self, ENEMIES+str(i+1)).UPDATE_SCALE(w3, h3)

    def SET_ANIMATIONS(self):
        if self.P1.ANIMATIONS == False:
            self.P1.ANIMATIONS = True
            self.R1.ANIMATIONS = True
            for i in range(0, self.ENEMY_COUNT):
                getattr(self, "E"+str(i+1)).ANIMATIONS = True
        else:
            self.P1.ANIMATIONS = False
            self.R1.ANIMATIONS = False
            for i in range(0, self.ENEMY_COUNT):
                getattr(self, "E"+str(i+1)).ANIMATIONS = False

    def SET_NAMETAGS(self):
        if self.P1.NAMETAGS == False:
            self.P1.NAMETAGS = True
            self.R1.NAMETAGS = True
            for i in range(0, self.ENEMY_COUNT):
                getattr(self, "E"+str(i+1)).NAMETAGS = True
        else:
            self.P1.NAMETAGS = False
            self.R1.NAMETAGS = False
            for i in range(0, self.ENEMY_COUNT):
                getattr(self, "E"+str(i+1)).NAMETAGS = False

    def START_FROM_LEVEL(self, x):
        SCREEN.fill(BLACK)
        self.SET_GAMEMODE(1)
        self.SET_CUR(x)
        self.SET_PLAYER_LOC(self.GRID, self.GRID)
        self.SET_RECTLANGE_LOC(self.GRID, self.GRID)
        self.START_GAME()
        self.SELECTABLE()
        self.SetLevel()

    def START_GAME(self):
       for i in range(1, len(MAPS)-2):
           if getattr(self, "Lvl"+str(i)+"_Clear") == True and self.CURRENT_MAP == i:
               if i < len(MAPS)-2-1:
                   setattr(self, "Lvl"+str(i+1)+"_Ready", False)
                   self.CURRENT_MAP = i+1

    def SET_GRID(self, x):
        self.GRID = x

    def SET_PLAYER_LOC(self, x, y):
        self.P1.x = x
        self.P1.y = y

    def SET_RECTLANGE_LOC(self, x, y):
        self.R1.x = x
        self.R1.y = y

    def SET_CUR(self, x):
        self.CURRENT_MAP = x

    def STOP_GAME(self):
        self.APP_RUN = False

    def ToggleGRID(self):
        x=y=0
        for row in MAPS[self.CURRENT_MAP]:
            for col in row:
                SCREEN.blit(self.grid_piece, (self.GRID*x, self.GRID*y))
                x += 1
            y += 1
            x = 0

    def PRESS_ENTER_TO_CONTINUE(self):
        while True:
            KEY = pygame.event.wait()
            if KEY.type == pygame.KEYDOWN and KEY.key == pygame.K_RETURN:
                break

    def SELECTABLE(self):
        for i in range(2, len(MAPS)):
            if self.CURRENT_MAP == i-1 and vars(self)["Lvl"+str(i-1)+"_Clear"] != True:
                if i-1 < 10:
                    setattr(getattr(self.PAGE_LEVELS_1, "BUTTON_"+str(i)), "COLOR_1", ORANGE)
                if 9 < i-1 < 19:
                    setattr(getattr(self.PAGE_LEVELS_2, "BUTTON_"+str(i-9)), "COLOR_1", ORANGE)
            if self.CURRENT_MAP == i and vars(self)["Lvl"+str(i-1)+"_Clear"] == True:
                if i-1 < 10:
                    setattr(getattr(self.PAGE_LEVELS_1, "BUTTON_"+str(i)), "COLOR_1", GREEN)
                if 9 < i-1 < 19:
                    setattr(getattr(self.PAGE_LEVELS_2, "BUTTON_"+str(i-9)), "COLOR_1", GREEN)

    def Main(self):
        while self.APP_RUN:
            self.FPS.tick(60)
            if self.ToggleMenu == 1:
                self.SELECTABLE()
            if self.GAMEMODE == 0:

                SCREEN.fill(BLACK)
                self.SET_PAGE("Adin ne?", "Adini yaz ve oyuna basla.")

                SCREEN.blit(self.TITLE, (RESOLUTION[0]//2-self.TITLE.get_width()//2, 128))
                SCREEN.blit(self.MESSAGE, (RESOLUTION[0]//2-self.MESSAGE.get_width()//2, 214))

                self.NICKNAMEBANNER = DEFEAT_FONT.render(self.P1.USERNAME, True, (255, 255, 255))
                SCREEN.blit(self.NICKNAMEBANNER, (RESOLUTION[0]//2-self.NICKNAMEBANNER.get_width()//2, RESOLUTION[1]//2-self.NICKNAMEBANNER.get_height()))

                self.BUTTON_8.SHOW()

                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.P1.USERNAME += "A"
                    if event.key == pygame.K_b:
                        self.P1.USERNAME += "B"
                    if event.key == pygame.K_c:
                        self.P1.USERNAME += "C"
                    if event.key == pygame.K_d:
                        self.P1.USERNAME += "D"
                    if event.key == pygame.K_e:
                        self.P1.USERNAME += "E"
                    if event.key == pygame.K_f:
                        self.P1.USERNAME += "F"
                    if event.key == pygame.K_g:
                        self.P1.USERNAME += "G"
                    if event.key == pygame.K_h:
                        self.P1.USERNAME += "H"
                    if event.key == pygame.K_i:
                        self.P1.USERNAME += "I"
                    if event.key == pygame.K_j:
                        self.P1.USERNAME += "J"
                    if event.key == pygame.K_k:
                        self.P1.USERNAME += "K"
                    if event.key == pygame.K_l:
                        self.P1.USERNAME += "L"
                    if event.key == pygame.K_m:
                        self.P1.USERNAME += "M"
                    if event.key == pygame.K_n:
                        self.P1.USERNAME += "N"
                    if event.key == pygame.K_o:
                        self.P1.USERNAME += "O"
                    if event.key == pygame.K_p:
                        self.P1.USERNAME += "P"
                    if event.key == pygame.K_q:
                        self.P1.USERNAME += "Q"
                    if event.key == pygame.K_r:
                        self.P1.USERNAME += "R"
                    if event.key == pygame.K_s:
                        self.P1.USERNAME += "S"
                    if event.key == pygame.K_t:
                        self.P1.USERNAME += "T"
                    if event.key == pygame.K_u:
                        self.P1.USERNAME += "U"
                    if event.key == pygame.K_v:
                        self.P1.USERNAME += "V"
                    if event.key == pygame.K_w:
                        self.P1.USERNAME += "W"
                    if event.key == pygame.K_x:
                        self.P1.USERNAME += "X"
                    if event.key == pygame.K_y:
                        self.P1.USERNAME += "Y"
                    if event.key == pygame.K_z:
                        self.P1.USERNAME += "Z"
                    if event.key == pygame.K_RETURN:
                        SCREEN.fill((0,0,0))
                        self.GAMEMODE = 2
                        SFX_Click.play()
                    if event.key == pygame.K_BACKSPACE:
                        try: self.P1.USERNAME = self.P1.USERNAME[0:-1]
                        except: pass

                self.BUTTON_8.COLLIDE(event)
                self.BUTTON_8.COMMAND(event)

                pygame.display.update()


            if self.GAMEMODE == 1:
                if self.RESTART == True:
                    if self.ToggleMenu == 0:
                        for i in range(1, len(MAPS)-2):
                            setattr(self, "Lvl"+str(i)+"_Clear", False)
                        for i in range(1, len(MAPS)-2):
                            setattr(self, "Lvl"+str(i)+"_Ready", None)
                        self.CURRENT_MAP = 1
                        self.Lvl1_Ready = True
                    self.Once_Lvl_Up = 0
                    self.Once_Defeat = 0
                    self.C1_Taken = False
                    self.RESTART = False
                    self.P1.DIRECTION = "RIGHT"
                    self.P1.DEAD = False
                    self.SetLevel()
                    SCREEN.fill((0, 0, 0))
                    pygame.display.update()
                    if self.ToggleMenu == 0:
                        self.GAMEMODE = 0
                        self.ToggleMenu = 1
                    self.SELECTABLE()


                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    self.APP_RUN = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.GAMEMODE = 2

                if self.GAMEMODE != 2 or self.GAMEMODE != 0:
                    if self.P1.DEAD == False:
                        self.P1.MOVE(event)
                        self.R1.MOVE(event)


                    for i in range(1, len(MAPS)-2):
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and getattr(self, "Lvl"+str(i)+"_Clear") == True and self.CURRENT_MAP == i:
                                if i < len(MAPS)-2-1:
                                    setattr(self, "Lvl"+str(i+1)+"_Ready", False)
                                    self.CURRENT_MAP = i+1
                                SFX_Click.play()

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.P1.DEAD == True:
                        SFX_Click.play()
                        self.RESTART = True

                    for i in range(1, len(MAPS)-2):
                        if self.CURRENT_MAP == i and getattr(self, "Lvl"+str(i)+"_Ready") == False:
                            setattr(self, "Lvl"+str(i)+"_Ready", True)
                            self.SetLevel()

                    # bu alttaki için

                    for i in range(0, self.ENEMY_COUNT):
                        E = getattr(self, "E"+str(i+1))
                        E.MOVE(event, self.R1, self.P1) # aslında r1 ve p1 de self.mainwindow.p1 r1 felan olabilir.
                    # ^+++ * * * büyük sorun çözüldü^^^^^^^^^^^^
                    self.ShowMap()

                    if self.GRIDisON == True:
                        self.ToggleGRID()

                    for i in range(0, self.ENEMY_COUNT):
                        X, Y, D = getattr(getattr(self, "E"+str(i+1)), "x"), getattr(getattr(self, "E"+str(i+1)), "y"), getattr(getattr(self, "E"+str(i+1)), "DEAD")
                        if self.P1.x == self.R1.x == X and self.P1.y == self.R1.y == Y and D == False:
                            setattr(getattr(self, "E"+str(i+1)), "DEAD", True)
                            self.AddCoin(5)
                            SFX_Coin.play()

                    for i in range(0, self.ENEMY_COUNT):
                        X, Y, D = getattr(getattr(self, "E"+str(i+1)), "x"), getattr(getattr(self, "E"+str(i+1)), "y"), getattr(getattr(self, "E"+str(i+1)), "DEAD")
                        if self.P1.x == X and self.P1.y == Y and D == False:
                            self.P1.DEAD = True
                    """
                    for i in range(0, self.ENEMY_COUNT):
                        X, Y, D = getattr(getattr(self, "E"+str(i+1)), "x"), getattr(getattr(self, "E"+str(i+1)), "y"), getattr(getattr(self, "E"+str(i+1)), "DEAD")
                        if D == False and MAPS[self.CURRENT_MAP][Y//self.GRID+1][X//self.GRID] != "W":
                            SCREEN.blit(self.monster_under, (X, Y+self.GRID))"""

                    if self.P1.DEAD == False:
                        try:
                            if MAPS[self.CURRENT_MAP][self.R1.y//self.GRID+1][self.R1.x//self.GRID] != "W":
                                SCREEN.blit(self.rectlange_under, (self.R1.x, self.R1.y+self.GRID))
                        except:
                            pass

                    if self.P1.DEAD == False:
                        self.P1.SHOW()

                    for i in range(0, self.ENEMY_COUNT):
                        X, Y, D = getattr(getattr(self, "E"+str(i+1)), "x"), getattr(getattr(self, "E"+str(i+1)), "y"), getattr(getattr(self, "E"+str(i+1)), "DEAD")
                        if D == False:
                            if MAPS[self.CURRENT_MAP][Y//self.GRID][X//self.GRID] != " ":
                                setattr(getattr(self, "E"+str(i+1)), "x", random.randint(1, len(MAPS[self.CURRENT_MAP][:-2]))*self.GRID)
                                setattr(getattr(self, "E"+str(i+1)), "y", random.randint(1, len(MAPS[self.CURRENT_MAP][:-2]))*self.GRID)
                                if D == False and MAPS[self.CURRENT_MAP][Y//self.GRID+1][X//self.GRID] != "W":
                                    SCREEN.blit(self.monster_under, (X, Y+self.GRID))
                                pygame.display.update()
                            getattr(self, "E"+str(i+1)).SHOW()

                    if self.P1.DEAD == False:
                        self.R1.SHOW()

                    if self.P1.DEAD == True:
                        self.TXT_Defeat = DEFEAT_FONT.render("KAYBETTIN!", True, (255, 0, 0))
                        SCREEN.blit(self.TXT_Defeat, (RESOLUTION[0]-(self.TXT_Defeat.get_width()+32), RESOLUTION[1]-(self.TXT_Defeat.get_height()+32)))
                        if self.Once_Defeat == 0:
                            self.Once_Defeat = 1
                            SFX_Defeat.play()

                    x=0
                    for i in range(0, self.ENEMY_COUNT):
                        D = getattr(getattr(self, "E"+str(i+1)), "DEAD")
                        if D == True:
                            x += 1
                        if x == self.ENEMY_COUNT:
                            setattr(self, "Lvl"+str(self.CURRENT_MAP)+"_Clear", True)

                    for i in range(1, len(MAPS)-2):
                        if self.CURRENT_MAP == i and getattr(self, "Lvl"+str(i)+"_Clear") == True:
                            if self.Once_Lvl_Up == 0:
                                self.Once_Lvl_Up = 1
                                SFX_Clear.play()
                            self.TXT_Clear1 = CLEAR_FONT.render("KAZANDIN!",                True, (255, 255, 255))
                            self.TXT_Clear2 = CLEAR_FONT.render("YENI SEVIYE ICIN [ENTER]", True, (255, 255, 255))
                            SCREEN.blit(self.TXT_Clear1, (32, 32))
                            SCREEN.blit(self.TXT_Clear2, (32, 96))

                    if self.C1x == self.P1.x and self.C1y == self.P1.y and self.C1_Taken == False and self.P1.DEAD == False:
                        self.C1_Taken = True
                        self.AddCoin(10)
                        SFX_Coin.play()

                    self.TXT_Scores = LEVEL_FONT.render("Altin: "+str(self.Score), True, (255, 215, 0))
                    SCREEN.blit(self.TXT_Scores, (RESOLUTION[0]//2-self.TXT_Scores.get_width()//2, 16))

                    if self.C1_Taken == False:
                        if MAPS[self.CURRENT_MAP][self.C1y//self.GRID][self.C1x//self.GRID] != " ":
                            self.C1x, self.C1y = random.randint(1, len(MAPS[self.CURRENT_MAP][:-2]))*self.GRID, random.randint(1, len(MAPS[self.CURRENT_MAP][:-2]))*self.GRID
                        SCREEN.blit(self.coin, (self.C1x, self.C1y))

                    self.Level_Text = LEVEL_FONT.render("Seviye: "+str(self.CURRENT_MAP), True, (191, 191, 191))
                    SCREEN.blit(self.Level_Text, (RESOLUTION[0]-self.Level_Text.get_width()-32, 16))

                    if self.SHOW_TIPS == True and self.TIP_COUNT == 0 and self.CURRENT_MAP == 1 and self.GAMEMODE == 1:
                        Dialog = DIALOG("Oyuna hosgeldin "+self.P1.USERNAME+"! Bas [Enter] ve devam et.", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 255), self, SCREEN)
                        Dialog.SHOW(100)

                        self.PRESS_ENTER_TO_CONTINUE()

                        Dialog = DIALOG("Canavarlari yok etmek icin yon tuslariyla canavara git ve...", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 255), self, SCREEN)
                        Dialog.SHOW(75)

                        Dialog = DIALOG("... wasd tuslariyla canavari yakala.", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 255), self, SCREEN)
                        Dialog.SHOW(75)

                        self.PRESS_ENTER_TO_CONTINUE()

                    if self.SHOW_TIPS == True and self.TIP_COUNT == 3 and self.CURRENT_MAP == 2:
                        Dialog = DIALOG("Canavarlar gitgide zorlasir. Bunun icin...", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 0, 0), self, SCREEN)
                        Dialog.SHOW(75)

                        Dialog = DIALOG("... Dortgeni, Oyuncudan cok uzaklastirma.", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 255, 0), self, SCREEN)
                        Dialog.SHOW(75)

                        self.PRESS_ENTER_TO_CONTINUE()

                        Dialog = DIALOG("Ayrıca, Ayarlar'i ve Market'i ziyaret etmeyi unutma.", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 255), self, SCREEN)
                        Dialog.SHOW(75)

                        self.PRESS_ENTER_TO_CONTINUE()

                    if self.SHOW_TIPS == True and self.TIP_COUNT == 6 and self.CURRENT_MAP == 3:
                        Dialog = DIALOG("Canavarlar Dortgenden gecemez.", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 255, 0), self, SCREEN)
                        Dialog.SHOW(100)

                        self.PRESS_ENTER_TO_CONTINUE()

                        Dialog = DIALOG("Yani Dortgeni hareketli duvar olarak (canavarları sıkıstırarak) ...", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 255, 0), self, SCREEN)
                        Dialog.SHOW(125)

                        Dialog = DIALOG("... kullanabilirsin.", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 255, 0), self, SCREEN)
                        Dialog.SHOW(75)

                        self.PRESS_ENTER_TO_CONTINUE()

                        Dialog = DIALOG("Ayrica soylemeyi unuttum. Seviyeler her 3 seviyede bir büyür...", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 255), self, SCREEN)
                        Dialog.SHOW(100)

                        Dialog = DIALOG("... Bu seviyeyi gecince farkedeceksin.", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 255), self, SCREEN)
                        Dialog.SHOW(75)

                        self.PRESS_ENTER_TO_CONTINUE()

                    if self.SHOW_TIPS == True and self.TIP_COUNT == 11 and self.CURRENT_MAP == 4:
                        Dialog = DIALOG("[ ! ] Onemli: Yaninda birden fazla canavar varsa, bir tane kalana kadar...", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 0), self, SCREEN)
                        Dialog.SHOW(100)

                        Dialog = DIALOG("... [Bosluk] tusuna basarak turu pas gec.", (255, 255, 255), "Andy", 40, (0, 0, 0), (0, 255, 0), self, SCREEN)
                        Dialog.SHOW(75)

                        self.PRESS_ENTER_TO_CONTINUE()

                        Dialog = DIALOG("Yapmazsan...", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 0, 0), self, SCREEN)
                        Dialog.SHOW(150)

                        Dialog = DIALOG("...Olebilirsin...", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 0, 0), self, SCREEN)
                        Dialog.SHOW(150)

                        Dialog = DIALOG("Bu yuzden dikkatli ol!", (255, 255, 255), "Andy", 40, (0, 0, 0), (255, 255, 255), self, SCREEN)
                        Dialog.SHOW(50)

                        self.PRESS_ENTER_TO_CONTINUE()

            if self.GAMEMODE == 2:
                SCREEN.blit(self.BACKGROUND, (0, 0))
                try:
                    self.PAGE_MENU.SHOW()
                except: pass

            if self.GAMEMODE == 3:
                self.Sprites()
                self.ShowMap()
                self.P1.SHOW()

                if self.CURRENT_MAP == "Market-0":
                    SCREEN.blit(self.E1.IMAGE, (self.GRID*4, self.GRID*2))
                    SCREEN.blit(self.monster_under, (self.GRID*4, self.GRID*3))
                    SCREEN.blit(self.P1.IMAGE, (self.GRID*2, self.GRID*2))
                    SCREEN.blit(self.R1.IMAGE, (self.GRID*3, self.GRID*2))
                    SCREEN.blit(self.rectlange_under, (self.GRID*3, self.GRID*3))
                    SCREEN.blit(self.coin, (self.GRID*3, self.GRID*3))

                    SCREEN.blit(self.E1.IMAGE, (self.GRID*8, self.GRID*2))
                    SCREEN.blit(self.monster_under, (self.GRID*8, self.GRID*3))
                    SCREEN.blit(self.P1.IMAGE, (self.GRID*6, self.GRID*2))
                    SCREEN.blit(self.R1.IMAGE, (self.GRID*7, self.GRID*2))
                    SCREEN.blit(self.rectlange_under, (self.GRID*7, self.GRID*3))
                    SCREEN.blit(self.coin, (self.GRID*7, self.GRID*3))

                    SCREEN.blit(self.E1.IMAGE, (self.GRID*12, self.GRID*2))
                    SCREEN.blit(self.monster_under, (self.GRID*12, self.GRID*3))
                    SCREEN.blit(self.P1.IMAGE, (self.GRID*10, self.GRID*2))
                    SCREEN.blit(self.R1.IMAGE, (self.GRID*11, self.GRID*2))
                    SCREEN.blit(self.rectlange_under, (self.GRID*11, self.GRID*3))
                    SCREEN.blit(self.coin, (self.GRID*11, self.GRID*3))

                    SCREEN.blit(self.E1.IMAGE, (self.GRID*16, self.GRID*2))
                    SCREEN.blit(self.monster_under, (self.GRID*16, self.GRID*3))
                    SCREEN.blit(self.P1.IMAGE, (self.GRID*14, self.GRID*2))
                    SCREEN.blit(self.R1.IMAGE, (self.GRID*15, self.GRID*2))
                    SCREEN.blit(self.rectlange_under, (self.GRID*15, self.GRID*3))
                    SCREEN.blit(self.coin, (self.GRID*15, self.GRID*3))

                    SCREEN.blit(self.R1.IMAGE, (self.GRID*3, self.GRID*5))
                    Price = NAMETAG_FONT.render("0", True, (255, 191, 0))
                    SCREEN.blit(Price, (self.GRID*3+self.GRID//2-Price.get_width()//2, self.GRID*4.5))
                    SCREEN.blit(self.rectlange_under, (self.GRID*3, self.GRID*6))

                    SCREEN.blit(self.R1.IMAGE, (self.GRID*7, self.GRID*5))
                    Price = NAMETAG_FONT.render("500", True, (255, 191, 0))
                    SCREEN.blit(Price, (self.GRID*7+self.GRID//2-Price.get_width()//2, self.GRID*4.5))
                    SCREEN.blit(self.rectlange_under, (self.GRID*7, self.GRID*6))

                    SCREEN.blit(self.R1.IMAGE, (self.GRID*11, self.GRID*5))
                    Price = NAMETAG_FONT.render("1000", True, (255, 191, 0))
                    SCREEN.blit(Price, (self.GRID*11+self.GRID//2-Price.get_width()//2, self.GRID*4.5))
                    SCREEN.blit(self.rectlange_under, (self.GRID*11, self.GRID*6))

                    SCREEN.blit(self.R1.IMAGE, (self.GRID*15, self.GRID*5))
                    Price = NAMETAG_FONT.render("0", True, (255, 191, 0))
                    SCREEN.blit(Price, (self.GRID*15+self.GRID//2-Price.get_width()//2, self.GRID*4.5))
                    SCREEN.blit(self.rectlange_under, (self.GRID*15, self.GRID*6))

                if self.CURRENT_MAP == "Market-0":
                    if self.P1.x == self.GRID*3 and self.P1.y == self.GRID*5:
                        SCREEN.blit(self.PopUpTheme0, (self.GRID*2, self.GRID*1))
                    if self.P1.x == self.GRID*7 and self.P1.y == self.GRID*5:
                        SCREEN.blit(self.PopUpTheme1, (self.GRID*6, self.GRID*1))
                    if self.P1.x == self.GRID*11 and self.P1.y == self.GRID*5:
                        SCREEN.blit(self.PopUpTheme2, (self.GRID*10, self.GRID*1))
                    if self.P1.x == self.GRID*15 and self.P1.y == self.GRID*5:
                        SCREEN.blit(self.PopUpTheme3, (self.GRID*14, self.GRID*1))

                if self.CURRENT_MAP == "Market-1":
                    for i in range(1, 6):
                        SCREEN.blit(self.R1.IMAGE, (self.GRID*3, self.GRID*i*2))
                    SCREEN.blit(self.R1.IMAGE, (self.GRID*15, self.GRID*6))
                    SCREEN.blit(self.R1.IMAGE, (self.GRID*15, self.GRID*8))

                self.TXT_Scores = LEVEL_FONT.render("Altin: "+str(self.Score), True, (255, 215, 0))
                SCREEN.blit(self.TXT_Scores, (RESOLUTION[0]-self.TXT_Scores.get_width()*1.5, 16))

                self.BUTTON_4.SHOW()

                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.GAMEMODE = 2

                if self.GAMEMODE != 2:
                    self.P1.MOVE(event)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if self.P1.x == self.GRID*3 and self.P1.y == self.GRID*5 and self.Score >= 0:
                                self.SelectedTheme = 0
                                SFX_Click.play()
                                self.AddCoin(0)
                                self.Sprites()
                            if self.P1.x == self.GRID*7 and self.P1.y == self.GRID*5 and self.Score >= 500:
                                self.SelectedTheme = 1
                                SFX_Click.play()
                                self.AddCoin(-500)
                                self.Sprites()
                            if self.P1.x == self.GRID*11 and self.P1.y == self.GRID*5 and self.Score >= 1000:
                                self.SelectedTheme = 2
                                SFX_Click.play()
                                self.AddCoin(-1000)
                                self.Sprites()
                            if self.P1.x == self.GRID*15 and self.P1.y == self.GRID*5 and self.Score >= 0:
                                self.SelectedTheme = 3
                                SFX_Click.play()
                                self.AddCoin(0)
                                self.Sprites()

                    self.BUTTON_4.COLLIDE(event)
                    self.BUTTON_4.COMMAND(event)

                    if self.P1.x == self.GRID*16 and self.P1.y == self.GRID*11 and self.CURRENT_MAP == "Market-0":
                        self.CURRENT_MAP = "Market-1"
                        self.P1.x, self.P1.y = self.GRID*16, self.GRID*1
                        self.R1.x, self.R1.y = self.GRID*4, self.GRID*4

                    if self.P1.x == self.GRID*16 and self.P1.y == self.GRID*0 and self.CURRENT_MAP == "Market-1":
                        self.CURRENT_MAP = "Market-0"
                        self.P1.x, self.P1.y = self.GRID*16, self.GRID*10
                        self.R1.x, self.R1.y = self.GRID*4, self.GRID*4

            if self.GAMEMODE == 4:
                self.PAGE_SETTINGS.SHOW()

            if 5 <= self.GAMEMODE < 6:
                if self.GAMEMODE == 5.1:
                    self.PAGE_LEVELS_1.SHOW()
                if self.GAMEMODE == 5.2:
                    self.PAGE_LEVELS_2.SHOW()

            pygame.display.update()

MAIN_WINDOW = MainWindow()

pygame.quit()
exit()

"""

     1152 x 768
 32    36 x 24
 64    18 x 12
 96    12 x 8
128     9 x 6

"""
