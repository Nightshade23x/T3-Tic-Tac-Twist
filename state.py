import tkinter as tk

def init_state():
    global board, player, bank_X, bank_O, used_questions
    global score_X, score_O
    global shuffled_this_turn, using_bank
    global player_name, root, buttons
    global bank_x_label, bank_o_label, score_label, turn_label

    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    bank_X = 0
    bank_O = 0
    used_questions = set()
    score_X = 0
    score_O = 0
    shuffled_this_turn = False
    using_bank = False
    player_name = {"X": "Player X", "O": "Player O"}

    root = tk.Tk()
    buttons = []
    bank_x_label = None
    bank_o_label = None
    score_label = None
    turn_label = None
