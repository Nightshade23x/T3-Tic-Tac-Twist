import random
from tkinter import messagebox

import state
import game_logic


def almost_winning(p):
    """Checks if a player is one move away from winning (for chaos mode)."""
    board = state.board

    for i in range(3):
        row = [board[i][j] for j in range(3)]
        col = [board[j][i] for j in range(3)]
        if row.count(p) == 2 and row.count(" ") == 1:
            return True
        if col.count(p) == 2 and col.count(" ") == 1:
            return True

    diag1 = [board[i][i] for i in range(3)]
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag1.count(p) == 2 and diag1.count(" ") == 1:
        return True
    if diag2.count(p) == 2 and diag2.count(" ") == 1:
        return True

    return False


def shuffle_both_players():
    """Randomly relocates all markers while avoiding auto-wins."""

    # Do not reshuffle twice in one turn
    if state.shuffled_this_turn:
        return
    state.shuffled_this_turn = True

    board = state.board
    buttons = state.buttons

    # -------------------------
    # SAFETY CHECK (avoids crash)
    # -------------------------
    if board is None:
        print("WARNING: shuffle_both_players() called before init_state()")
        state.init_state()
        board = state.board

    # make a deep copy of board
    old_board = [row[:] for row in board]

    players = ["X", "O"]
    reshuffle_limit = 50

    for _ in range(reshuffle_limit):

        # wipe board
        for i in range(3):
            for j in range(3):
                board[i][j] = " "

        for p in players:
            markers = [(i, j) for i in range(3) for j in range(3) if old_board[i][j] == p]
            empties = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

            random.shuffle(markers)
            random.shuffle(empties)

            for (mr, mc), (er, ec) in zip(markers, empties):
                board[er][ec] = p

        # no instant win + no almost-wins allowed
        if (
            not game_logic.check_winner("X")
            and not game_logic.check_winner("O")
            and not almost_winning("X")
            and not almost_winning("O")
        ):
            break

    # repaint UI
    for i in range(3):
        for j in range(3):
            cell = board[i][j]
            if cell == " ":
                buttons[i][j].config(text=" ", state="normal")
            else:
                buttons[i][j].config(
                    text=cell,
                    fg="#f54242" if cell == "X" else "#4bf542",
                    state="disabled"
                )

    messagebox.showinfo("CHAOS TIME", "Markers shuffled! Prepare for chaosss")
