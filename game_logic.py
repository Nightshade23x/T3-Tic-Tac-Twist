import random
from tkinter import messagebox
import state
from questions import get_question
from chaos import shuffle_both_players
from state import root


# -----------------------------------
# WIN CHECKING
# -----------------------------------

def check_winner(p):
    for i in range(3):
        if all(state.board[i][j] == p for j in range(3)):
            return True
        if all(state.board[j][i] == p for j in range(3)):
            return True

    if all(state.board[i][i] == p for i in range(3)):
        return True

    if all(state.board[i][2 - i] == p for i in range(3)):
        return True

    return False


def is_draw():
    return all(
        state.board[i][j] != " "
        for i in range(3)
        for j in range(3)
    )


# -----------------------------------
# TILE RELOCATION
# -----------------------------------

def relocate_if_conflict(r, c, player):
    opponent = "O" if player == "X" else "X"

    if state.board[r][c] != opponent:
        return

    empties = [(i, j) for i in range(3) for j in range(3) if state.board[i][j] == " "]
    if not empties:
        return

    new_r, new_c = random.choice(empties)

    state.board[new_r][new_c] = opponent
    state.buttons[new_r][new_c].config(
        text=opponent,
        fg="#f54242" if opponent == "X" else "#4bf542",
        state="disabled"
    )

    state.board[r][c] = " "
    state.buttons[r][c].config(text=" ")


# -----------------------------------
# MAIN MOVE HANDLING
# -----------------------------------

def make_move(r, c):
    from ui import update_banks, update_turn_label, update_score

    # tile taken?
    if state.board[r][c] != " ":
        messagebox.showinfo("Iwe", "Spot already taken. Are you blind?")
        return

    # must answer question first
    result = ask_question()

    if result is None:
        return

    if result is False:
        switch_turn()
        return

    current_bank = state.bank_X if state.player == "X" else state.bank_O
    opponent = "O" if state.player == "X" else "X"

    # -------------------------
    # USE BANKED MOVE?
    # -------------------------
    if current_bank == 1 and not state.using_bank:
        action = messagebox.askquestion("Your Move", "You have a banked move.\nUse it now?")

        if action == "yes":
            state.using_bank = True

            if not state.shuffled_this_turn:
                shuffle_both_players()
                state.shuffled_this_turn = True

            relocate_if_conflict(r, c, state.player)
            state.board[r][c] = state.player
            state.buttons[r][c].config(
                text=state.player,
                fg="#f5f542" if state.player == "X" else "#42f5c5",
                state="disabled"
            )

            if state.player == "X":
                state.bank_X = 0
            else:
                state.bank_O = 0

            update_banks()

            messagebox.showinfo("Second Move", f"Player {state.player}, place your second marker")

            # handle second click
            def second_click(rr, cc):
                if state.board[rr][cc] in [" ", opponent]:
                    relocate_if_conflict(rr, cc, state.player)
                    state.board[rr][cc] = state.player
                    state.buttons[rr][cc].config(
                        text=state.player,
                        fg="#f5f542" if state.player == "X" else "#42f5c5",
                        state="disabled"
                    )

                    restore_main_commands()

                    if check_winner(state.player):
                        declare_winner(state.player)
                    else:
                        switch_turn()

                    state.shuffled_this_turn = False
                    state.using_bank = False
                else:
                    messagebox.showinfo("Invalid", "Spot is taken. Use your eyes please.")

            # override all buttons
            for i in range(3):
                for j in range(3):
                    state.buttons[i][j].config(command=lambda rr=i, cc=j: second_click(rr, cc))

            return

    # -------------------------
    # OFFER TO BANK MOVE
    # -------------------------
    if (state.player == "X" and state.bank_X == 0) or (
            state.player == "O" and state.bank_O == 0):

        choice = messagebox.askquestion("Your Move", "Do you want to bank this move for later?")

        if choice == "yes":
            if state.player == "X":
                state.bank_X = 1
            else:
                state.bank_O = 1

            update_banks()
            messagebox.showinfo("Banked", f"Player {state.player} banked their move.")
            switch_turn()
            return

    # -------------------------
    # NORMAL MOVE
    # -------------------------
    relocate_if_conflict(r, c, state.player)
    state.board[r][c] = state.player

    state.buttons[r][c].config(
        text=state.player,
        fg="#ffff99" if state.player == "X" else "#99ffff",
        state="disabled"
    )

    if check_winner(state.player):
        declare_winner(state.player)
        return

    if is_draw():
        messagebox.showinfo("Draw", "It's a draw!")
        state.score_X += 1
        state.score_O += 1
        update_score()

        again = messagebox.askyesno("Draw", "Play again?")
        if again:
            reset_board(state.player)
        else:
            root.destroy()
        return

    switch_turn()


# -----------------------------------
# TURN SWITCHING
# -----------------------------------

def switch_turn():
    from ui import update_turn_label
    state.player = "O" if state.player == "X" else "X"
    update_turn_label()


def restore_main_commands():
    for i in range(3):
        for j in range(3):
            state.buttons[i][j].config(command=lambda r=i, c=j: make_move(r, c))


# -----------------------------------
# DECLARE WINNER
# -----------------------------------

def declare_winner(p):
    from ui import update_score, update_banks, update_turn_label, big_yes_no, highlight_winning_line
    highlight_winning_line(p)

    if p == "X":
        state.score_X += 1
    else:
        state.score_O += 1

    highlight_winning_line(p)
    root.update()

    state.bank_X = 0
    state.bank_O = 0
    update_score()
    update_banks()

    again = big_yes_no(
        "Winner winner chicken dinner",
        f"{state.player_name[p]} ({p}) wins!\n\nPlay again?"
    )

    if not again:
        root.destroy()
        return

    starter = big_yes_no(
        "Who starts?",
        f"{state.player_name[p]} won.\nShould they start the next round?"
    )

    next_player = p if starter else ("O" if p == "X" else "X")
    reset_board(next_player)


# -----------------------------------
# RESET BOARD
# -----------------------------------

def reset_board(starting_player):
    from ui import update_banks, update_turn_label

    state.board[:] = [[" " for _ in range(3)] for _ in range(3)]
    state.bank_X = 0
    state.bank_O = 0
    state.shuffled_this_turn = False
    state.using_bank = False
    state.player = starting_player

    for i in range(3):
        for j in range(3):
            state.buttons[i][j].config(
                text=" ",
                fg="white",
                state="normal",
                command=lambda r=i, c=j: make_move(r, c)
            )

    update_banks()
    update_turn_label()


# -----------------------------------
# ASK QUESTION
# -----------------------------------

def ask_question():
    q, a = get_question()

    timed_out = False

    import tkinter as tk
    question_window = tk.Toplevel(root)
    question_window.title(f"Question for Player {state.player}")
    question_window.geometry("700x400")
    question_window.config(bg="#222222")

    def on_close():
        nonlocal timed_out
        choice = messagebox.askyesno(
            "Exit Detected",
            "Quit the game? (Yes = Quit, No = Pick another spot)"
        )
        if choice:
            root.destroy()
        else:
            question_window.destroy()
            timed_out = "retry"

    question_window.protocol("WM_DELETE_WINDOW", on_close)

    label_q = tk.Label(question_window, text=q, wraplength=350,
                       fg="white", bg="#222222", font=("Arial", 12))
    label_q.pack(pady=20)

    timer_label = tk.Label(question_window, text="Time left: 20",
                           fg="red", bg="#222222",
                           font=("Arial", 14, "bold"))
    timer_label.pack(pady=5)

    answer_var = tk.StringVar()
    entry = tk.Entry(question_window, textvariable=answer_var,
                     font=("Arial", 12), width=30)
    entry.pack(pady=10)
    entry.focus()

    time_left = 20

    def countdown():
        nonlocal time_left, timed_out
        time_left -= 1

        if time_left <= 0:
            timed_out = True
            timer_label.config(text="Time left: 0")
            messagebox.showinfo("Time's Up!", "You ran out of time! Wrong answer.")
            question_window.destroy()
            return

        timer_label.config(text=f"Time left: {time_left}")
        question_window.after(1000, countdown)

    countdown()

    def submit():
        question_window.destroy()

    tk.Button(question_window, text="Submit", command=submit,
              font=("Arial", 11)).pack(pady=10)

    root.wait_window(question_window)

    if timed_out == "retry":
        return None
    if timed_out:
        return False

    ans = answer_var.get().strip().lower()
    if ans == "":
        return False

    if isinstance(a, list):
        correct = any(ans == x.strip().lower() for x in a)
        correct_display = ", ".join([x.title() for x in a])
    else:
        correct = ans == a.strip().lower()
        correct_display = a.title()

    if correct:
        messagebox.showinfo("Correct!!!", "Marker earned!")
        return True

    messagebox.showinfo("Wrong", f"Incorrect. The correct answer was: {correct_display}")
    return False
