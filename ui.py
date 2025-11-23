import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# SAFE: import state as module (never copy variables!)
import state
from game_logic import make_move, reset_board
from questions import instructions


# ---------------------------------------
# ROOT SETUP
# ---------------------------------------

root = state.root
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
# GAME START WRAPPER (Fix for double triggers)
# ---------------------------------------

def begin_game():
    set_player_names()
    start_game_ui()


# ---------------------------------------
# COIN TOSS
# ---------------------------------------

def coin_toss_animation():
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
        if count < 15:
            toss_label.config(text=random.choice(results))
            toss_window.after(80, animate, count + 1)
        else:
            toss_label.config(
                text=f"{state.player_name[state.player]} ({state.player}) starts!",
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
        begin_game()

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
        begin_game()

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
    win = tk.Toplevel(root)
    win.title("Enter Player Names")
    win.configure(bg="#111111")   # dark theme

    # Larger, cleaner window size
    win.geometry("450x350")
    win.resizable(False, False)
    win.grab_set()
    win.focus_force()

    # Center the window on screen
    win.update_idletasks()
    x = (win.winfo_screenwidth() - win.winfo_reqwidth()) // 2
    y = (win.winfo_screenheight() - win.winfo_reqheight()) // 3
    win.geometry(f"+{x}+{y}")

    title_font = ("Arial", 16, "bold")
    label_font = ("Arial", 14)
    entry_font = ("Arial", 14)
    button_font = ("Arial", 14, "bold")

    # ------- Player X ---------
    lbl_x = tk.Label(
        win, text="Player X Name:",
        fg="white", bg="#111111",
        font=label_font
    )
    lbl_x.pack(pady=(25, 5))

    entry_x = tk.Entry(
        win,
        font=entry_font,
        width=20,
        justify="center"
    )
    entry_x.pack(pady=(0, 20))

    # ------- Player O ---------
    lbl_o = tk.Label(
        win, text="Player O Name:",
        fg="white", bg="#111111",
        font=label_font
    )
    lbl_o.pack(pady=(10, 5))

    entry_o = tk.Entry(
        win,
        font=entry_font,
        width=20,
        justify="center"
    )
    entry_o.pack(pady=(0, 25))

    # ------- Start Button -------
    def submit():
        nx = entry_x.get().strip() or "Player X"
        no = entry_o.get().strip() or "Player O"

        state.player_name["X"] = nx
        state.player_name["O"] = no

        win.destroy()   # close the window

    btn = tk.Button(
        win, text="Start",
        font=button_font,
        width=10,
        bg="#eeeeee",
        fg="black",
        command=submit
    )
    btn.pack(pady=10)

    # 🔥 CRITICAL FIX: block execution until this window is closed
    root.wait_window(win)



# ---------------------------------------
# GAME UI
# ---------------------------------------

def start_game_ui():
    coin_toss_animation()

    root.deiconify()
    root.overrideredirect(False)

    state.turn_label = tk.Label(
        root,
        text=f"{state.player_name[state.player]} ({state.player}) — it's your turn!",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#222222",
        pady=10
    )
    state.turn_label.pack(fill="x")

    state.score_label = tk.Label(
        root,
        text="Score — X: 0 | O: 0",
        font=("Arial", 13),
        fg="white",
        bg="#121212"
    )
    state.score_label.pack()

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

    frame = tk.Frame(root, bg="#121212")
    frame.pack(pady=10)

    for i in range(3):
        for j in range(3):
            state.buttons[i][j] = None

    for i in range(3):
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
            state.buttons[i][j] = b

    update_banks()
    update_turn_label()


# ---------------------------------------
# UPDATE LABELS
# ---------------------------------------

def update_banks():
    state.bank_x_label.config(text=f"Player X Banked: {'✅' if state.bank_X else '❌'}")
    state.bank_o_label.config(text=f"Player O Banked: {'✅' if state.bank_O else '❌'}")


def update_turn_label():
    state.turn_label.config(
        text=f"{state.player_name[state.player]} ({state.player}) — it's your turn!",
        bg="#330000" if state.player == "X" else "#001a33",
        fg="white"
    )


def update_score():
    state.score_label.config(text=f"Score — X: {state.score_X} | O: {state.score_O}")


def highlight_winning_line(p):
    from state import buttons, board, root
    import tkinter as tk

    frame = buttons[0][0].master
    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height(),
                       highlightthickness=0, bg="#121212", bd=0)
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame.update_idletasks()

    cell_size = buttons[0][0].winfo_width() + 10
    gap = 5

    winning_coords = None

    for i in range(3):
        if all(board[i][j] == p for j in range(3)):
            y = i * (cell_size + gap) + cell_size // 2
            winning_coords = (0, y, 3 * cell_size, y)
            break

    for j in range(3):
        if all(board[i][j] == p for i in range(3)):
            x = j * (cell_size + gap) + cell_size // 2
            winning_coords = (x, 0, x, 3 * cell_size)
            break

    if all(board[i][i] == p for i in range(3)):
        winning_coords = (0, 0, 3 * cell_size, 3 * cell_size)
    elif all(board[i][2-i] == p for i in range(3)):
        winning_coords = (3 * cell_size, 0, 0, 3 * cell_size)

    if winning_coords:
        x1, y1, x2, y2 = winning_coords
        color = "#f54242" if p == "X" else "#4bf542"

        steps = 25
        for step in range(steps + 1):
            canvas.delete("line")
            x_end = x1 + (x2 - x1) * (step / steps)
            y_end = y1 + (y2 - y1) * (step / steps)
            canvas.create_line(x1, y1, x_end, y_end,
                               width=8, fill=color, tags="line")
            canvas.update()
            canvas.after(20)

        root.after(1200, canvas.destroy)


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
