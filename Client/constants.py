from json_functions import load_config


"""
This file contains constants useful for interacting with the hardware
Changing constants may cause hard-to-debug problems
"""


"""
ENGINES PINS
IF YOU'RE WONDERING WHY THIS ORDER PLEASE READ :
lynxmotion_ssc-32u_usb_user_guide.pdf
"""
VERT_REAR_R   = 0
HORI_REAR_R   = 1
VERT_MIDDLE_R = 2
HORI_MIDDLE_R = 3
VERT_FRONT_R  = 4
HORI_FRONT_R  = 5
KNEE_REAR_R   = 6
KNEE_MIDDLE_R = 7
KNEE_FRONT_R  = 8
VERT_REAR_L   = 16
HORI_REAR_L   = 17
VERT_MIDDLE_L = 18
HORI_MIDDLE_L = 19
VERT_FRONT_L  = 20
HORI_FRONT_L  = 21
KNEE_REAR_L   = 22
KNEE_MIDDLE_L = 23
KNEE_FRONT_L  = 24


ENGINES_DICT_REVERSED = {
    VERT_REAR_R   : "VERT_REAR_R",
    HORI_REAR_R   : "HORI_REAR_R",
    VERT_MIDDLE_R : "VERT_MIDDLE_R",
    HORI_MIDDLE_R : "HORI_MIDDLE_R",
    VERT_FRONT_R  : "VERT_FRONT_R",
    HORI_FRONT_R  : "HORI_FRONT_R",
    KNEE_REAR_R   : "KNEE_REAR_R",
    KNEE_MIDDLE_R : "KNEE_MIDDLE_R",
    KNEE_FRONT_R  : "KNEE_FRONT_R",
    VERT_REAR_L   : "VERT_REAR_L",
    HORI_REAR_L   : "HORI_REAR_L",
    VERT_MIDDLE_L : "VERT_MIDDLE_L",
    HORI_MIDDLE_L : "HORI_MIDDLE_L",
    VERT_FRONT_L  : "VERT_FRONT_L",
    HORI_FRONT_L  : "HORI_FRONT_L",
    KNEE_REAR_L   : "KNEE_REAR_L",
    KNEE_MIDDLE_L : "KNEE_MIDDLE_L",
    KNEE_FRONT_L  : "KNEE_FRONT_L"
}


"""DO NOT CHANGE THOSE ARRAYS"""
ENGINES_KNEE = [
    KNEE_FRONT_R, KNEE_FRONT_L,
    KNEE_MIDDLE_R, KNEE_MIDDLE_L,
    KNEE_REAR_R, KNEE_REAR_L
]

ENGINES_HORI = [
    HORI_FRONT_R, HORI_FRONT_L,
    HORI_MIDDLE_R, HORI_MIDDLE_L,
    HORI_REAR_R, HORI_REAR_L
]

ENGINES_VERT = [
    VERT_FRONT_R, VERT_FRONT_L,
    VERT_MIDDLE_R, VERT_MIDDLE_L,
    VERT_REAR_R, VERT_REAR_L
]

ENGINES_FRONT = [
    VERT_FRONT_L, VERT_FRONT_R,
    HORI_FRONT_L, HORI_FRONT_R,
    KNEE_FRONT_L, KNEE_FRONT_R
]

ENGINES_MIDDLE = [
    VERT_MIDDLE_L, VERT_MIDDLE_R,
    HORI_MIDDLE_L, HORI_MIDDLE_R,
    KNEE_MIDDLE_L, KNEE_MIDDLE_R
]

ENGINES_REAR = [
    VERT_REAR_L, VERT_REAR_R,
    HORI_REAR_L, HORI_REAR_R,
    KNEE_REAR_L, KNEE_REAR_R
]

"""CONSTANTS TO IMPROVE READABILITY"""

"""ENGINE TYPE"""
KNEE    = 0
HORI    = 1
VERT    = 2

"""ENGINE ZONES"""
FRONT   = 0
MIDDLE  = 1
REAR    = 2

"""MIN/MAX OF THE ENGINE"""
MIN     = 0
MAX     = 1

"""SIDE"""
LEFT    = 0
RIGHT   = 1

ARR = load_config()

INDEX_TO_ENGINE_NAME = [
    "MIN_KNEE_FRONT_LEFT",
    "MAX_KNEE_FRONT_LEFT",
    "MIN_KNEE_FRONT_RIGHT",
    "MAX_KNEE_FRONT_RIGHT",
    "MIN_KNEE_MIDDLE_LEFT",
    "MAX_KNEE_MIDDLE_LEFT",
    "MIN_KNEE_MIDDLE_RIGHT",
    "MAX_KNEE_MIDDLE_RIGHT",
    "MIN_KNEE_REAR_LEFT",
    "MAX_KNEE_REAR_LEFT",
    "MIN_KNEE_REAR_RIGHT",
    "MAX_KNEE_REAR_RIGHT",
    "MIN_HORI_FRONT_LEFT",
    "MAX_HORI_FRONT_LEFT",
    "MIN_HORI_FRONT_RIGHT",
    "MAX_HORI_FRONT_RIGHT",
    "MIN_HORI_MIDDLE_LEFT",
    "MAX_HORI_MIDDLE_LEFT",
    "MIN_HORI_MIDDLE_RIGHT",
    "MAX_HORI_MIDDLE_RIGHT",
    "MIN_HORI_REAR_LEFT",
    "MAX_HORI_REAR_LEFT",
    "MIN_HORI_REAR_RIGHT",
    "MAX_HORI_REAR_RIGHT",
    "MIN_VERT_FRONT_LEFT",
    "MAX_VERT_FRONT_LEFT",
    "MIN_VERT_FRONT_RIGHT",
    "MAX_VERT_FRONT_RIGHT",
    "MIN_VERT_MIDDLE_LEFT",
    "MAX_VERT_MIDDLE_LEFT",
    "MIN_VERT_MIDDLE_RIGHT",
    "MAX_VERT_MIDDLE_RIGHT",
    "MIN_VERT_REAR_LEFT",
    "MAX_VERT_REAR_LEFT",
    "MIN_VERT_REAR_RIGHT",
    "MAX_VERT_REAR_RIGHT",
]

MIN_MAX_ENGINES = [
    [  # KNEE
        [
            [ARR["MIN_KNEE_FRONT_LEFT"], ARR["MAX_KNEE_FRONT_LEFT"]],       # FRONT LEFT
            [ARR["MIN_KNEE_FRONT_RIGHT"], ARR["MAX_KNEE_FRONT_RIGHT"]]      # FRONT RIGHT
        ],
        [
            [ARR["MIN_KNEE_MIDDLE_LEFT"], ARR["MAX_KNEE_MIDDLE_LEFT"]],     # MIDDLE LEFT
            [ARR["MIN_KNEE_MIDDLE_RIGHT"], ARR["MAX_KNEE_MIDDLE_RIGHT"]]    # MIDDLE RIGHT
        ],
        [
            [ARR["MIN_KNEE_REAR_LEFT"], ARR["MAX_KNEE_REAR_LEFT"]],         # REAR LEFT
            [ARR["MIN_KNEE_REAR_RIGHT"], ARR["MAX_KNEE_REAR_RIGHT"]],       # REAR RIGHT
        ]
    ],
    [ # HORI
        [
            [ARR["MIN_HORI_FRONT_LEFT"], ARR["MAX_HORI_FRONT_LEFT"]],       # FRONT LEFT
            [ARR["MIN_HORI_FRONT_RIGHT"], ARR["MAX_HORI_FRONT_RIGHT"]]      # FRONT RIGHT
        ],
        [
            [ARR["MIN_HORI_MIDDLE_LEFT"], ARR["MAX_HORI_MIDDLE_LEFT"]],     # MIDDLE LEFT
            [ARR["MIN_HORI_MIDDLE_RIGHT"], ARR["MAX_HORI_MIDDLE_RIGHT"]]    # MIDDLE RIGHT
        ],
        [
            [ARR["MIN_HORI_REAR_LEFT"], ARR["MAX_HORI_REAR_LEFT"]],         # REAR LEFT
            [ARR["MIN_HORI_REAR_RIGHT"], ARR["MAX_HORI_REAR_RIGHT"]]        # REAR RIGHT
        ]
    ],
    [  # VERT
        [
            [ARR["MIN_VERT_FRONT_LEFT"], ARR["MAX_VERT_FRONT_LEFT"]],       # FRONT LEFT
            [ARR["MIN_VERT_FRONT_RIGHT"], ARR["MAX_VERT_FRONT_RIGHT"]],     # FRONT RIGHT
        ],
        [
            [ARR["MIN_VERT_MIDDLE_LEFT"], ARR["MAX_VERT_MIDDLE_LEFT"]],     # MIDDLE LEFT
            [ARR["MIN_VERT_MIDDLE_RIGHT"], ARR["MAX_VERT_MIDDLE_RIGHT"]],   # MIDDLE RIGHT
        ],
        [
            [ARR["MIN_VERT_REAR_LEFT"], ARR["MAX_VERT_REAR_LEFT"]],         # REAR LEFT
            [ARR["MIN_VERT_REAR_RIGHT"], ARR["MAX_VERT_REAR_RIGHT"]],       # REAR RIGHT
        ]
    ]
]
"""
Example :
If you want to access max knee middle left:
MIN_MAX_ENGINES[KNEE][MIDDLE][LEFT][MAX]
"""
