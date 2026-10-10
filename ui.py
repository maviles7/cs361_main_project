"""
command-line interface for the user to interact with the workkout app
"""

# constants

WO_FOCUS_LIST= ["strength", "cardio", "combo"]

MIN_MINUTES = 15
MAX_MINUTES = 60

BACK_COMMAND = "b"
QUIT_COMMAND = "q"

# helper functions 

def show_wo_focus_menu():
    """ 
        print the menu of workout focuses - numbered 
    """
    print("\nselect workout focus:")
    for i, option in enumerate(WO_FOCUS_LIST, start=1):
        print(f"{i}. {option}")

def get_wo_focus():
    """ 
        asks for user workout focus input until valid input is entered
        - returns the workout focus string corresponding to the user input (strength, cardio, or combo)
    """
    while True:
        show_wo_focus_menu()
        wo_choice = input("enter the number of your workout focus choice: ").strip()

        # validate user input - if input is a valid number and within the range of options, then return the corresponding workout focus
        if wo_choice.isdecimal() and 1 <= int(wo_choice) <= len(WO_FOCUS_LIST):
            wo_focus = WO_FOCUS_LIST[int(wo_choice) - 1]
            print(f"\nyou selected: {wo_focus}")
            return wo_focus

        print("invalid input. please enter a number corresponding to the workout focus options.")

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
            f"\nhow many minutes do you have available to workout?"
            f"\n enter a number between {MIN_MINUTES} and {MAX_MINUTES} (ex: 45)"
            f"\n enter '{BACK_COMMAND}' to go back to the workout focus menu or '{QUIT_COMMAND}' to quit the program."
        )

        time_input = input("minutes available: ").strip()

        if time_input == BACK_COMMAND:
            return BACK_COMMAND
        elif time_input == QUIT_COMMAND:
            return QUIT_COMMAND
        
        if time_input.isdecimal() and MIN_MINUTES <= int(time_input) <= MAX_MINUTES:
            minutes = int(time_input)
            print(f"\nyou have {minutes} minutes available to workout.")
            return minutes

        print("invalid input. please enter a whole number between 15 and 60, or 'b' to go back, or 'q' to quit.")
        

def main():
    while True:
        wo_focus = get_wo_focus()
        minutes = get_wo_duration()

        if minutes == BACK_COMMAND:
            continue
        elif minutes == QUIT_COMMAND:
            print("quitting program. goodbye!")
            return 

        print(f"\nworkout focus: {wo_focus}, duration: {minutes} minutes")
        return 


if __name__ == "__main__":
    main()