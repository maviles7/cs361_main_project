# command-line interface for the user to interact with the workkout app

WO_FOCUS_LIST= ["strength", "cardio", "combo"]

# helper functions 

def show_wo_focus_menu():
    # print the menu of workout focuses
    print("\nselect workout focus:")
    for i, option in enumerate(WO_FOCUS_LIST, start=1):
        print(f"{i}. {option}")

def get_wo_focus():
    # asks for user input and returns the selected workout focus
    while True:
        show_wo_focus_menu()
        wo_choice = input("enter the number of your workout focus choice: ").strip()

        # validate user input - if input is a valid number and within the range of options, then return the corresponding workout focus
        if wo_choice.isdecimal() and 1 <= int(wo_choice) <= len(WO_FOCUS_LIST):
            wo_focus = WO_FOCUS_LIST[int(wo_choice) - 1]
            print(f"\nyou selected: {wo_focus}")
            return wo_focus

        print("invalid input. please enter a number corresponding to the workout focus options.")

def main():
    get_wo_focus()

if __name__ == "__main__":
    main()