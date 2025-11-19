import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# IMPORTANT: Never import player_name or turn_label at top (keeps stale values)
from state import root, board, player, bank_X, bank_O, score_X, score_O, shuffled_this_turn, using_bank, buttons
from logic import make_move, reset_board
from questions import instructions


# ---------------------------------------
# ROOT SETUP
# ---------------------------------------

root.overrideredirect(True)
root.withdraw()
root.title("T3: Tic Tac Twist")
root.configure(bg="#121212")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
app_width = int(screen_width * 0.8)
app_height = int(screen_height * 0.8)
x_pos = (screen_width // 2) - (app_width // 2)
y_pos = (screen_height // 2) - (app_height // 2)
root.geometry(f"{app_width}x{app_height}+{x_pos}+{y_pos}")


# ---------------------------------------
# COIN TOSS
# ---------------------------------------

def coin_toss_animation():
    from state import player, player_name   # <-- pull fresh names

    toss_window = tk.Toplevel(root)
    toss_window.title("Coin Toss")
    toss_window.geometry("400x200")
    toss_window.configure(bg="#111111")

    toss_label = tk.Label(
        toss_window,
        text="Flipping...",
        font=("Arial", 20, "bold"),
        fg="white",
        bg="#111111"
    )
    toss_label.pack(expand=True)

    results = ["Heads", "Tails"]

    def animate(count=0):
        from state import player, player_name  # fresh inside loop

        if count < 15:
            toss_label.config(text=random.choice(results))
            toss_window.after(80, animate, count + 1)
        else:
            # FIX: player_name now always valid
            toss_label.config(
                text=f"{player_name[player]} ({player}) starts!",
                fg="#00ff66"
            )
            toss_window.after(1200, toss_window.destroy)

    animate()
    root.wait_window(toss_window)


# ---------------------------------------
# MAIN MENU
# ---------------------------------------

def start_menu_ui():
    menu = tk.Toplevel(root)
    menu.title("T3: Tic Tac Twist — Main Menu")
    menu.geometry("500x350")
    menu.configure(bg="#111111")
    menu.grab_set()
    menu.focus_force()

    tk.Label(menu,
             text="T3: TIC TAC TWIST",
             font=("Arial", 24, "bold"),
             fg="#00ff99",
             bg="#111111").pack(pady=30)

    def start_game():
        menu.destroy()
        set_player_names()   # MUST HAPPEN BEFORE COIN TOSS
        start_game_ui()

    def show_rules():
        menu.destroy()
        show_instructions_ui()

    tk.Button(menu, text="Start Game", font=("Arial", 16, "bold"),
              width=15, bg="#00cc66", fg="black", command=start_game).pack(pady=20)

    tk.Button(menu, text="Instructions", font=("Arial", 14),
              width=15, bg="#444444", fg="white", command=show_rules).pack(pady=10)

    tk.Button(menu, text="Quit", font=("Arial", 14),
              width=15, bg="#cc3333", fg="white",
              command=lambda: root.destroy()).pack(pady=10)

    root.wait_window(menu)


# ---------------------------------------
# INSTRUCTIONS
# ---------------------------------------

def show_instructions_ui():
    inst = tk.Toplevel(root)
    inst.title("READ THIS SHIT")
    inst.configure(bg="#111111")
    inst.geometry("800x600")
    inst.grab_set()
    inst.focus_force()

    frame = tk.Frame(inst, bg="#111111")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    text = tk.Text(frame, wrap="word", font=("Arial", 13),
                   fg="white", bg="#111111", relief="flat", padx=10, pady=10)
    text.insert("1.0", instructions)
    text.config(state="disabled")
    text.pack(fill="both", expand=True)

    def start_game():
        inst.destroy()
        set_player_names()
        start_game_ui()

    tk.Button(inst, text="OK, LET'S PLAY", font=("Arial", 14, "bold"),
              bg="#00cc66", fg="black", width=15,
              command=start_game).pack(pady=15)

    root.wait_window(inst)


# ---------------------------------------
# NAME ENTRY
# ---------------------------------------

def ask_player_names():
    name_window = tk.Toplevel(root)
    name_window.title("Enter Player Names")
    name_window.geometry("400x250")
    name_window.configure(bg="#222222")
    name_window.grab_set()

    tk.Label(name_window, text="Player X Name:",
             fg="white", bg="#222222").pack(pady=10)
    name_x_var = tk.StringVar()
    tk.Entry(name_window, textvariable=name_x_var).pack()

    tk.Label(name_window, text="Player O Name:",
             fg="white", bg="#222222").pack(pady=10)
    name_o_var = tk.StringVar()
    tk.Entry(name_window, textvariable=name_o_var).pack()

    result = {"X": "Player X", "O": "Player O"}

    def submit_names():
        result["X"] = name_x_var.get().strip() or "Player X"
        result["O"] = name_o_var.get().strip() or "Player O"
        name_window.destroy()

    tk.Button(name_window, text="Start",
              command=submit_names).pack(pady=20)

    root.wait_window(name_window)
    return result


def set_player_names():
    from state import player_name
    # FIX: update the existing dict instead of replacing it
    player_name.update(ask_player_names())


# ---------------------------------------
# GAME UI
# ---------------------------------------

def start_game_ui():
    import state
    from state import player

    coin_toss_animation()

    root.deiconify()
    root.overrideredirect(False)

    # TURN LABEL — correctly assigned to global state
    state.turn_label = tk.Label(
        root,
        text=f"{state.player_name[player]} ({player}) — it's your turn!",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#222222",
        pady=10
    )
    state.turn_label.pack(fill="x")

    # SCORE LABEL — correct global storage
    state.score_label = tk.Label(
        root,
        text="Score — X: 0 | O: 0",
        font=("Arial", 13),
        fg="white",
        bg="#121212"
    )
    state.score_label.pack()

    # BANK LABELS — correct
    status_frame = tk.Frame(root, bg="#121212")
    status_frame.pack(pady=5)

    state.bank_x_label = tk.Label(
        status_frame, text="Player X Banked: ❌",
        font=("Arial", 12),
        fg="#ff6666", bg="#121212"
    )
    state.bank_x_label.grid(row=0, column=0, padx=10)

    state.bank_o_label = tk.Label(
        status_frame, text="Player O Banked: ❌",
        font=("Arial", 12),
        fg="#66b3ff", bg="#121212"
    )
    state.bank_o_label.grid(row=0, column=1, padx=10)

    # GAME BOARD
    frame = tk.Frame(root, bg="#121212")
    frame.pack(pady=10)

    buttons.clear()
    for i in range(3):
        row = []
        for j in range(3):
            b = tk.Button(
                frame,
                text=" ",
                font=("Arial", 22, "bold"),
                width=5, height=2,
                bg="#1f1f1f", fg="white",
                activebackground="#444444",
                relief="ridge", bd=3,
                command=lambda r=i, c=j: make_move(r, c)
            )
            b.grid(row=i, column=j, padx=5, pady=5)
            row.append(b)
        buttons.append(row)

    update_banks()
    update_turn_label()



# ---------------------------------------
# UPDATE LABELS
# ---------------------------------------

def update_banks():
    from state import bank_X, bank_O, bank_x_label, bank_o_label
    bank_x_label.config(text=f"Player X Banked: {'✅' if bank_X else '❌'}")
    bank_o_label.config(text=f"Player O Banked: {'✅' if bank_O else '❌'}")


def update_turn_label():
    from state import player, player_name, turn_label
    turn_label.config(
        text=f"{player_name[player]} ({player}) — it's your turn!",
        bg="#330000" if player == "X" else "#001a33",
        fg="white"
    )


def update_score():
    from state import score_X, score_O, score_label
    score_label.config(text=f"Score — X: {score_X} | O: {score_O}")


# ---------------------------------------
# BIG YES/NO
# ---------------------------------------

def big_yes_no(title, message):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("420x180")
    win.configure(bg="#222222")
    win.grab_set()

    tk.Label(win, text=message, font=("Arial", 14),
             fg="white", bg="#222222", wraplength=380).pack(pady=20)

    btn_frame = tk.Frame(win, bg="#222222")
    btn_frame.pack()

    result = {"answer": None}

    def choose(val):
        result["answer"] = val
        win.destroy()

    tk.Button(btn_frame, text="Yes", width=10,
              command=lambda: choose(True)).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="No", width=10,
              command=lambda: choose(False)).grid(row=0, column=1, padx=10)

    win.wait_window()
    return result["answer"]
