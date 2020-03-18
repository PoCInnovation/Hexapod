from constants import *


def is_knee(engine):
    return engine in ENGINES_KNEE


def is_vert(engine):
    return engine in ENGINES_VERT


def is_hori(engine):
    return engine in ENGINES_HORI


def is_front(engine):
    return engine in ENGINES_FRONT


def is_middle(engine):
    return engine in ENGINES_MIDDLE


def is_rear(engine):
    return engine in ENGINES_REAR


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
    return RIGHT if engine < 15 else LEFT


def get_engine_min_max(engine):
    engine_type = get_engine_type(engine)
    engine_zone = get_engine_zone(engine)
    engine_side = get_engine_side(engine)
    # print(f"ICII {engine_type} {engine_zone} {engine_side}", MIN_MAX_ENGINES[engine_type][engine_zone][engine_side])

    return MIN_MAX_ENGINES[engine_type][engine_zone][engine_side]


def set_engine_min_max(engine, new_min, new_max):
    engine_type = get_engine_type(engine)
    engine_zone = get_engine_zone(engine)
    engine_side = get_engine_side(engine)
    MIN_MAX_ENGINES[engine_type][engine_zone][engine_side][MIN] = new_min
    MIN_MAX_ENGINES[engine_type][engine_zone][engine_side][MAX] = new_max


def convert_angle(angle, engine):
    """ Converts a ratio (0 -> 1) to an engine angle """
    vals = get_engine_min_max(engine)
    return angle * (vals[MAX] - vals[MIN]) + vals[MIN]


def angle_to_ratio(angle, engine):
    """ Converts an engine angle to a ratio (0 -> 1)  """
    vals = get_engine_min_max(engine)
    return (angle - vals[MAX]) / (vals[MIN] - vals[MAX])
