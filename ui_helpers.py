import tkinter as tk
from tkinter import ttk

def custom_popup(root, title, message, mode="ok"):
    """
    mode = "ok"    -> OK button
    mode = "yesno" -> Yes / No buttons
    Returns:
        True  = Yes
        False = No
        None  = OK
    """

    # ----------------------------
    # Create popup window
    # ----------------------------
    win = tk.Toplevel(root)
    win.title(title)
    win.resizable(False, False)
    win.grab_set()

    # Purple gradient background simulation
    GRADIENT_TOP = "#2B0033"      # deep purple
    GRADIENT_BOTTOM = "#110019"   # darker shade

    # Canvas to paint gradient
    canvas = tk.Canvas(win, width=380, height=250, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Draw gradient line-by-line
    for i in range(250):
        r1 = 43 + int((17 - 43) * (i / 250))
        g1 = 0
        b1 = 51 + int((25 - 51) * (i / 250))
        hex_color = f"#{r1:02x}{g1:02x}{b1:02x}"
        canvas.create_line(0, i, 380, i, fill=hex_color)

    # ----------------------------
    # Center window
    # ----------------------------
    win.update_idletasks()
    w, h = 380, 250
    x = (win.winfo_screenwidth() // 2) - w // 2
    y = (win.winfo_screenheight() // 2) - h // 2
    win.geometry(f"{w}x{h}+{x}+{y}")

    # ----------------------------
    # Title label
    # ----------------------------
    

    # ----------------------------
    # MESSAGE LOGIC
    # Supports:
    # 1) Correct answer highlight (red)
    # 2) Winner highlight (red + bold)
    # 3) Normal message
    # ----------------------------

    if "Correct answer:" in message:
        # WRONG ANSWER POPUP
        parts = message.split("Correct answer:")
        main_text = parts[0].strip()
        answer_text = parts[1].strip()

        msg_main = tk.Label(
            win,
            text=main_text,
            fg="#F2E6FF",
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12, "bold")
        )
        canvas.create_window(190, 80, window=msg_main)

        msg_answer = tk.Label(
            win,
            text=f"Correct answer: {answer_text}",
            fg="#FF4040",      # 🔴 RED
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12, "bold")
        )
        canvas.create_window(190, 140, window=msg_answer)

    elif "wins!" in message:
        # WINNER POPUP (from big_yes_no)
        lines = message.split("\n")

        top_line = lines[0].strip()
        winner_line = lines[1].strip()
        bottom_line = lines[2].strip() if len(lines) > 2 else ""

        msg_top = tk.Label(
            win,
            text=top_line,
            fg="#F2E6FF",
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 14, "bold")
        )
        canvas.create_window(190, 70, window=msg_top)

        msg_winner = tk.Label(
            win,
            text=winner_line,
            fg="#FF3030",      # 🔥 RED winner highlight
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 15, "bold")
        )
        canvas.create_window(190, 110, window=msg_winner)

        msg_bottom = tk.Label(
            win,
            text=bottom_line,
            fg="#F2E6FF",
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12)
        )
        canvas.create_window(190, 145, window=msg_bottom)

    else:
        # NORMAL POPUP
        msg_label = tk.Label(
            win,
            text=message,
            fg="#F2E6FF",
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12, "bold")
        )
        canvas.create_window(190, 110, window=msg_label)

    # ----------------------------
    # Button styling (makes them visible)
    # ----------------------------
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "Purple.TButton",
        font=("Segoe UI", 11, "bold"),
        padding=8,
        foreground="white",
        background="#6A0DAD",
        borderwidth=0
    )

    style.map(
        "Purple.TButton",
        background=[("active", "#8B1BCC")]
    )

    result = {"value": None}

    def set_value(v):
        result["value"] = v
        win.destroy()

    # ----------------------------
    # Buttons
    # ----------------------------
    if mode == "yesno":
        btn_yes = ttk.Button(
            win, text="Yes", style="Purple.TButton",
            command=lambda: set_value(True)
        )
        btn_no = ttk.Button(
            win, text="No", style="Purple.TButton",
            command=lambda: set_value(False)
        )

        canvas.create_window(120, 200, window=btn_yes)
        canvas.create_window(260, 200, window=btn_no)

    else:
        btn_ok = ttk.Button(
            win, text="OK", style="Purple.TButton",
            command=lambda: set_value(None)
        )
        canvas.create_window(190, 200, window=btn_ok)

    win.wait_window()
    return result["value"]
