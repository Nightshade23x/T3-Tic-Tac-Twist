import tkinter as tk
from ui import start_menu_ui, start_game_ui, show_instructions_ui
from state import root, init_state
init_state()
from ui import set_player_names

if __name__ == "__main__":
    init_state()      # sets globals
    start_menu_ui()   # opens main menu
    root.mainloop()
