from constants import *

def is_knee(engine):
    return engine in ENGINES_KNEE

def is_vert(engine):
    return engine in ENGINE_VERT

def is_hori(engine):
    return engine in ENGINES_HORI

def is_front(engine):
    return engine in ENGINE_FRONT

def is_middle(engine):
    return engine in ENGINE_MIDDLE

def is_rear(engine):
    return engine in ENGINE_REAR

def get_engine_type(engine):
    if is_knee(engine):
        return KNEE
    elif is_vert(engine):
        return VERT
    elif is_hori(engine):
        return HORI

def get_engine_zone(engine):
    if is_front(engine):
        return FRONT
    elif is_middle(engine):
        return MIDDLE
    elif is_rear(engine):
        return REAR

def get_engine_side(engine):
    if engine < 15:
        return RIGHT
    else:
        return LEFT

def get_engine_min_max(engine):
    engine_type = get_engine_type(engine)
    engine_zone = get_engine_zone(engine)
    engine_side = get_engine_side(engine)
    print(f"ICII {engine_type} {engine_zone} {engine_side}", MIN_MAX_ENGINES[engine_type][engine_zone][engine_side])

    return MIN_MAX_ENGINES[engine_type][engine_zone][engine_side]

def convert_angle(angle, engine):
    vals = get_engine_min_max(engine)
    print("Convert_angle : ", vals)
    return angle * (vals[1] - vals[0]) + vals[0]
