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
    canvas = tk.Canvas(win, width=380, height=220, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Draw gradient (vertical stripes)
    for i in range(220):
        r1 = 43 + int((17 - 43) * (i / 220))
        g1 = 0  + int((0 - 0) * (i / 220))
        b1 = 51 + int((25 - 51) * (i / 220))
        hex_color = f"#{r1:02x}{g1:02x}{b1:02x}"
        canvas.create_line(0, i, 380, i, fill=hex_color)

    # ----------------------------
    # Center window
    
    win.update_idletasks()
    w, h = 380, 220
    x = (win.winfo_screenwidth() // 2) - w // 2
    y = (win.winfo_screenheight() // 2) - h // 2
    win.geometry(f"{w}x{h}+{x}+{y}")

    # ----------------------------
    # Add text on top of canvas
    # ----------------------------
    title_label = tk.Label(
        win,
        text=title,
        fg="white",
        bg=GRADIENT_TOP,
        font=("Segoe UI", 16, "bold")
    )
    canvas.create_window(190, 40, window=title_label)

    # ----------------------------
# MESSAGE (supports bold + red highlights)
# ----------------------------

# Determine if message contains a "Correct answer:" part
    if "Correct answer:" in message:
        parts = message.split("Correct answer:")
        main_text = parts[0].strip()
        answer_text = parts[1].strip()

        # Main message
        msg_main = tk.Label(
            win,
            text=main_text,
            fg="#F2E6FF",       # soft white-purple
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12, "bold")
        )
        canvas.create_window(190, 90, window=msg_main)

        # Correct answer (highlighted)
        msg_answer = tk.Label(
            win,
            text=f"Correct answer: {answer_text}",
            fg="#FF4C4C",       # 🔴 RED highlight
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12, "bold")
        )
        canvas.create_window(190, 120, window=msg_answer)

    else:
        # Normal popup text (bold)
        msg_label = tk.Label(
            win,
            text=message,
            fg="#F2E6FF",
            bg=GRADIENT_TOP,
            wraplength=330,
            justify="center",
            font=("Segoe UI", 12, "bold")
        )
        canvas.create_window(190, 100, window=msg_label)


    # ----------------------------
    # Custom ttk style (fix blank buttons)
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
            win,
            text="Yes",
            style="Purple.TButton",
            command=lambda: set_value(True)
        )
        btn_no = ttk.Button(
            win,
            text="No",
            style="Purple.TButton",
            command=lambda: set_value(False)
        )

        canvas.create_window(120, 170, window=btn_yes)
        canvas.create_window(260, 170, window=btn_no)

    else:  # mode="ok"
        btn_ok = ttk.Button(
            win,
            text="OK",
            style="Purple.TButton",
            command=lambda: set_value(None)
        )
        canvas.create_window(190, 170, window=btn_ok)

    win.wait_window()
    return result["value"]
