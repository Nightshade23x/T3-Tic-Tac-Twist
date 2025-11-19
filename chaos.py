import random
from tkinter import messagebox

from state import board, buttons
  # safe circular import because function-only
   

def almost_winning(p):
    """Checks if a player is one move away from winning (for chaos mode)."""
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
    """Randomly relocates all X and O markers while avoiding auto-wins."""
    from state import shuffled_this_turn
    from logic import check_winner
    global shuffled_this_turn

    if shuffled_this_turn:
        return
    shuffled_this_turn = True

    players = ["X", "O"]

    # snapshot old board
    old_board = [row[:] for row in board]

    reshuffle_limit = 50
    attempt = 0

    while attempt < reshuffle_limit:
        attempt += 1

        # clear the board
        for i in range(3):
            for j in range(3):
                board[i][j] = " "

        # re-place markers randomly
        for p in players:
            markers = [(i, j) for i in range(3) for j in range(3) if old_board[i][j] == p]
            empties = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

            random.shuffle(markers)
            random.shuffle(empties)

            for (mr, mc), (er, ec) in zip(markers, empties):
                board[er][ec] = p

        # ensure chaos does NOT create instant wins
        if (not check_winner("X") and not check_winner("O")
            and not almost_winning("X") and not almost_winning("O")):
            break

    # repaint buttons according to new shuffled board
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
