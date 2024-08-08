from main_first import main_first_window
from main_second import main_second_window
from main_third import main_third_window

def navigate_to(window, target):
    window.destroy()
    target()

if __name__ == "__main__":
    main_first_window()
