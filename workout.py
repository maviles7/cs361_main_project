"""
selects & displays workout

- workouts are selected by users input & time constraint
- input time is rounded down to the neart quarter of an hour (ensures WO never exceeds time constraint)
"""

from workouts import cardio, combo, strength_weight

WORKOUTS = {
    "strength": {
        15: strength_weight.strength_wo_15,
        30: strength_weight.strength_wo_30,
        45: strength_weight.strength_wo_45,
        60: strength_weight.strength_wo_60,
    },
    "cardio": {
        15: cardio.cardio_wo_15,
        30: cardio.cardio_wo_30,
        45: cardio.cardio_wo_45,
        60: cardio.cardio_wo_60,
    },
    "combo": {
        15: combo.combo_wo_15,
        30: combo.combo_wo_30,
        45: combo.combo_wo_45,
        60: combo.combo_wo_60,
    },
}

def pick_workout(focus, minutes):
    """
    return (length, workout): the longest workout that fits within minutes inputed
    """    
    workout_focus = WORKOUTS[focus]

    best_length = None
    for length in workout_focus:
        # validating user's time constraint
        if length <= minutes:
            if best_length is None or length > best_length:
                # keep longest length 
                best_length = length 

    if best_length is None:
        raise ValueError(f"No workout fits within {minutes} minutes.")

    return best_length, workout_focus[best_length]

def display_workout(focus, minutes, length, workout):
    """
    print workout title & each part on it's own line
    """
    print(f"your {focus} workout, estimated time to complete: {minutes}")
    for entry in workout:
        for title, description in entry.items(): 
            print(f"\n {title.upper()}")
            for part in description.split(";"):
                print(f" - {part.strip()}")