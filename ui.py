# command-line interface for the user to interact with the workkout app

WO_FOCUS_LIST= ["strength", "cardio", "combo"]

def show_wo_focus_menu():
    # print the menu of workout focuses
    print("\nselect workout focus:")
    for i, option in enumerate(WO_FOCUS_LIST, start=1):
        print(f"{i}. {option}")


def main():
    show_wo_focus_menu()

if __name__ == "__main__":
    main()