import json

with open('Client/values.json') as json_file:
    data = json.load(json_file)
    pins = data["pins"]
    minMaxValues = data["minMaxValues"]

REAR_R_HORI = pins["rearRHori"]
REAR_R_VERT = pins["rearRVert"]
REAR_R_KNEE = pins["rearRKnee"]
REAR_L_HORI = pins["rearLHori"]
REAR_L_VERT = pins["rearLVert"]
REAR_L_KNEE = pins["rearLKnee"]
MIDD_R_HORI = pins["middRHori"]
MIDD_R_VERT = pins["middRVert"]
MIDD_R_KNEE = pins["middRKnee"]
MIDD_L_HORI = pins["middLHori"]
MIDD_L_VERT = pins["middLVert"]
MIDD_L_KNEE = pins["middLKnee"]
FRON_R_HORI = pins["fronRHori"]
FRON_R_VERT = pins["fronRVert"]
FRON_R_KNEE = pins["fronRKnee"]
FRON_L_HORI = pins["fronLHori"]
FRON_L_VERT = pins["fronLVert"]
FRON_L_KNEE = pins["fronLKnee"]

KNEE_VALUES = [
    [minMaxValues["maxLKnee"],
     minMaxValues["minLKnee"]
     ],
    [minMaxValues["maxRKnee"],
     minMaxValues["minRKnee"]
     ],
]

VERT_VALUES = [
    [minMaxValues["maxLVert"],
     minMaxValues["minLVert"]
     ],
    [minMaxValues["maxRVert"],
     minMaxValues["minRVert"]
     ],
]

HORI_VALUES = [
    [minMaxValues["maxLHori"],
     minMaxValues["minLHori"]
     ],
    [minMaxValues["maxRHori"],
     minMaxValues["minRHori"]
     ],
]

ENGINES_KNEE = [
    FRON_R_KNEE, FRON_L_KNEE,
    MIDD_R_KNEE, MIDD_L_KNEE,
    REAR_R_KNEE, REAR_L_KNEE
]

ENGINES_HORI = [
    FRON_R_HORI, FRON_L_HORI,
    MIDD_R_HORI, MIDD_L_HORI,
    REAR_R_HORI, REAR_L_HORI
]

ENGINE_VERT = [
    FRON_R_VERT, FRON_L_VERT,
    MIDD_R_VERT, MIDD_L_VERT,
    REAR_R_VERT, REAR_L_VERT
]

def is_knee(engine):
    return engine in ENGINES_KNEE

def is_vert(engine):
    return engine in ENGINE_VERT

def is_hori(engine):
    return engine in ENGINES_HORI

def get_engine_min_max(engine):
    index = int(engine < 15)

    if is_hori(engine):
        return HORI_VALUES[index]
    if is_vert(engine):
        return VERT_VALUES[index]
    if is_knee(engine):
        return KNEE_VALUES[index]

