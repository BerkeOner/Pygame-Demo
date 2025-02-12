# HARITALAR

# 1, 2, 3: x128
# 4, 5, 6: x96
# 7, 8, 9: x64
# 10: x32

# Market-0, Market-1: x64

MAPS = {}

MAPS[1] = ["WWWWWWWWW",
           "W       W",
           "WWWWWWW W",
           "W     W W",
           "W       W",
           "WWWWWWWWW"]
MAPS[2] = ["WWWWWWWWW",
           "W     W W",
           "W W   W W",
           "W W   W W",
           "W W     W",
           "WWWWWWWWW"]
MAPS[3] = ["WWWWWWWWW",
           "WW     WW",
           "W   W   W",
           "W   W   W",
           "WW     WW",
           "WWWWWWWWW"]

MAPS[4] = ["WWWWWWWWWWWW",
           "W          W",
           "WWW WWWWWW W",
           "W W      W W",
           "W W      W W",
           "W WWWWWW WWW",
           "W          W",
           "WWWWWWWWWWWW"]
MAPS[5] = ["WWWWWWWWWWWW",
           "W          W",
           "WWWWW  WWWWW",
           "W   W  W   W",
           "W   W  W   W",
           "W  WW  WW  W",
           "W          W",
           "WWWWWWWWWWWW"]
MAPS[6] = ["WWWWWWWWWWWW",
           "WW        WW",
           "W          W",
           "W    WW    W",
           "W    WW    W",
           "W          W",
           "WW        WW",
           "WWWWWWWWWWWW"]

MAPS[7] = ["WWWWWWWWWWWWWWWWWW",
           "WWWWW        WWWWW",
           "WWW            WWW",
           "WW   WWWWWWWW   WW",
           "WW   W      W   WW",
           "W    W      W    W",
           "W    W      W    W",
           "WW   W      W   WW",
           "WW   WWW  WWW   WW",
           "WWW            WWW",
           "WWWWW        WWWWW",
           "WWWWWWWWWWWWWWWWWW"]
MAPS[8] = ["WWWWWWWWWWWWWWWWWW",
           "WW  W       WWW WW",
           "W            W   W",
           "W WWWWW      W   W",
           "W   W        W   W",
           "W  WWW       W   W",
           "W   W       WWW  W",
           "W   W        W   W",
           "W   W      WWWWW W",
           "W   W            W",
           "WW WWW       W  WW",
           "WWWWWWWWWWWWWWWWWW"]
MAPS[9] = ["WWWWWWWWWWWWWWWWWW",
           "W                W",
           "W WW WWWWWWWWWWW W",
           "W W   W        W W",
           "W W      WWWW WW W",
           "W WWWWWWWW     W W",
           "W W   W  W  WWWW W",
           "W W      W     W W",
           "W W   W        W W",
           "W WWWWWWWWWWW WW W",
           "W                W",
           "WWWWWWWWWWWWWWWWWW"]

MAPS[10] = ["WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "W                                  W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]

MAPS[11] = []

# Market: "Market-0", "Market-1"
# x64
MAPS["Market-0"] = ["WWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWW",
                    "WW   W   W   W   W",
                    "WW   W   W   W   W",
                    "WWWWWWWWWWWWWWWWWW",
                    "WWW WWW WWW WWW WW",
                    "WW               W",
                    "WW               W",
                    "W                W",
                    "WW             W W",
                    "WWWWWWWWWWWWWWWW W",
                    "WWWWWWWWWWWWWWWW W"]

MAPS["Market-1"] = ["WWWWWWWWWWWWWWWW W",
                    "WWWWWWWWWWWWWWWW W",
                    "W W            W W",
                    "WWWW           W W",
                    "W W              W",
                    "WWWW        WWWWWW",
                    "W W         W W  W",
                    "WWWW        WWWW W",
                    "W W         W W  W",
                    "WWWW        WWWW W",
                    "W W              W",
                    "WWWWWWWWWWWWWWWWWW"]

"""
MARKET = {}

# Market: "Market-0", "Market-1"
# x64
MARKET[1] = ["WWWWWWWWWWWWWWWWWW",
             "WWWWWWWWWWWWWWWWWW",
             "WW   W   W   W   W",
             "WW   W   W   W   W",
             "WWWWWWWWWWWWWWWWWW",
             "WWW WWW WWW WWW WW",
             "WW               W",
             "WW               W",
             "W                W",
             "WW             W W",
             "WWWWWWWWWWWWWWWW W",
             "WWWWWWWWWWWWWWWW W"]
MARKET[2] = ["WWWWWWWWWWWWWWWW W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "W                W",
             "WWWWWWWWWWWWWWWWWW"]
"""
