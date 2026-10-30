"""
command-line interface for the user to interact with the workkout app
"""

from workout import pick_workout, display_workout
from info_pages.about_app import about_app
from info_pages.about_wo import about_wo

# constants

WO_FOCUS_LIST= ["strength", "cardio", "combo"]

# strength workout labels 
STRENGTH_LABELS = {
    "strength_bw": "strength (body-weight)",
    "strength_weight": "strength (weight-training)",
}

MIN_MINUTES = 15
MAX_MINUTES = 60

BACK_COMMANDS = ("b", "back")
QUIT_COMMANDS = ("q", "quit")
START_COMMANDS = ("y", "yes")
INFO_COMMANDS = ("i", "info")
CONFIRM_COMMANDS = ("y", "yes")

BACK = "back"
QUIT = "quit"
START = "start"
CONFIRM = "confirm"

# helper functions 
def get_started():
    """
        initiates program
        - prints menu option of getting started, learning more, or quitting program
    """
    print(
        "No Brain Cell Energy\n"
        "A workout that matches your training focus, no brain cell required.\n"
        "This is a free app - no sign-in & your info is never stored.\n"
        "Workout is generated in less 60 seconds."
        "\nHow it Works:\n"
        "1.) select your workout focus (strength, cardio, combo)\n"
        "2.) enter the time you have available to complete a workout in minutes\n"
        "3.) confirm your selections & get your workout\n"  
        )

    while True:
        print("\ny: yes, let's get started!")
        print("i: more info on app")
        print("q: quit\n")
 
        user_input = input("shall we get started? ").strip().lower()
 
        if user_input in START_COMMANDS:
            return START
        if user_input in INFO_COMMANDS:
            about_app()
            while True:
                info_input = input("enter option: ").strip().lower()
                if info_input in BACK_COMMANDS:
                    break
                elif info_input in QUIT_COMMANDS:
                    return QUIT
                print("invalid input. please enter b or q.")
            continue 
        if user_input in QUIT_COMMANDS:
            return QUIT
 
        print("invalid input. please enter y or q.")

def show_wo_focus_menu():
    """ 
        print the menu of workout focuses - numbered 
    """
    print("\nstep 1) select workout focus:")
    # generating numbered list
    for i, option in enumerate(WO_FOCUS_LIST, start=1):
        print(f"{i}. {option}")

    print(f"\ni: info on workout types")
    print(f"q: quit\n")

def get_wo_focus():
    """ 
        asks for user workout focus input until valid input is entered
        - returns the workout focus string corresponding to the user input (strength, cardio, or combo)
        - QUIT - user wants to quit program
    """
    while True:
        show_wo_focus_menu()
        wo_choice = input("your workout focus: ").strip().lower()

        if wo_choice in QUIT_COMMANDS:
            return QUIT
        if wo_choice in INFO_COMMANDS:
            about_wo()
            while True:
                info_input = input("enter option: ").strip().lower()
                if info_input in BACK_COMMANDS:
                    break
                elif info_input in QUIT_COMMANDS:
                    return QUIT
                print("invalid input. please enter b or q.")
            continue

        # validate user input - if input is a valid number and within the range of options, then return the corresponding workout focus
        if wo_choice.isdecimal() and 1 <= int(wo_choice) <= len(WO_FOCUS_LIST):
            wo_focus = WO_FOCUS_LIST[int(wo_choice) - 1]
            print(f"\nyou selected: {wo_focus}")
            return wo_focus

        print("invalid input. please enter 1, 2, 3, 4, or q.")

def get_strength_wo_type():
    """
        asks user for what kind of strength workout they would like to reciever - with weights or bodyweight
        - returns: 
            - BACK: user wants to return to focus menu
            - QUIT: user wants to quit program
    """
    while True: 
        print("\nstep 1) select strength type:\n")
        print("1) bodyweight strengthening - no equipment needed\n")
        print("2) weight-training strengthing - barbell, dumbbells, kettlebells, etc needed\n")

        print("b: back")
        print("q: quit")

        strength_input = input("strength workout type: ").strip().lower()

        if strength_input in BACK_COMMANDS:
            return BACK
        if strength_input in QUIT_COMMANDS:
            return QUIT

        if strength_input == "1":
            print("\nyou selected: bodyweight strengthning")
            return "strength_bw"
        if strength_input == "2":
            print("\nyou selected: weight-training strengthening")
            return "strength_weight"

        print("invalid input. please enter 1,2,b, or q.")

def get_wo_duration():
    """
        asks for user for how many minutes they have available to workout until valid input is entered
        - returns
            - int: number of minutes user has to workout out (15-60 min)
            - BACK: user wants to return to focus menu
            - QUIT: user wants to quit the program
    """
    while True:
        print(
            f"\nstep 2) how much time do you have to complete a workout?"
            f"\nenter a number of minutes between {MIN_MINUTES} and {MAX_MINUTES}"
            f"\nex. 43\n"
            f"\nb: back"
            f"\nq: quit\n"
        )

        # get minutes from user
        time_input = input("minutes available: ").strip()

        if time_input in BACK_COMMANDS:
            return BACK
        elif time_input in QUIT_COMMANDS:
            return QUIT

        # if min is within range, return minutes
        if time_input.isdecimal() and MIN_MINUTES <= int(time_input) <= MAX_MINUTES:
            minutes = int(time_input)
            print(f"\nyou have {minutes} minutes available to workout.")
            return minutes

        print("invalid input. please enter a whole number between 15 and 60, 'b', or 'q'.")

def choice_confirmation(wo_focus, minutes, length):
    """
        asks user to confirm choices 
        - returns training focus, minutes available, & esitmated time to comlpete 
    """
    while True:
        print(
            f"\nstep 3) confirm your selection:"
            f"\nworkout focus - {wo_focus}"
            f"\ntime available - {minutes} minutes"
            f"\nyour workout will be {length} minutes, the longest workout that fits within your time.\n"
            f"\ny: get my workout"
            f"\nb: back to change my time"
            f"\nq: quit\n"
        )

        confirm_input = input("confirm: ").strip().lower()
 
        if confirm_input in CONFIRM_COMMANDS:
            return CONFIRM
        if confirm_input in BACK_COMMANDS:
            return BACK
        if confirm_input in QUIT_COMMANDS:
            return QUIT
 
        print("invalid input. please enter y, b, or q.")
        

def main():
    # welcome screen is displayed before the loop ("back" will never returns to it)
    if get_started() == QUIT:
        print("the program has been quit. goodbye!")
        return
 
    while True:
        wo_focus = get_wo_focus()
 
        if wo_focus == QUIT:
            print("the program has been quit. goodbye!")
            return

        # workout_key = name of workout.py will use to find wo
        workout_key = wo_focus
        # focus_label = what the user will see to confirm selections
        focus_label = wo_focus

        if wo_focus == "strength":
            strength_type = get_strength_wo_type()

            if strength_type == BACK:
                continue
            if strength_type == QUIT:
                print("the program has been quit. goodbye!")
                return

        workout_key = strength_type
        focus_label = STRENGTH_LABELS[strength_type]
 
        # time prompt + confirm screen
        while True:
            minutes = get_wo_duration()
 
            if minutes == BACK:
                break  # leave the loop --> back to the focus menu
            if minutes == QUIT:
                print("the program has been quit. goodbye!")
                return
 
            length, workout = pick_workout(workout_key, minutes)
            choice = choice_confirmation(focus_label, minutes, length)
 
            if choice == BACK:
                continue  # back to the time prompt
            if choice == QUIT:
                print("the program has been quit. goodbye!")
                return
 
            # choice == CONFIRM: show the workout
            display_workout(wo_focus, length, workout)
            return

if __name__ == "__main__":
    main()