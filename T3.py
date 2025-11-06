import random
import tkinter as tk
from tkinter import messagebox, simpledialog

questions = [
    ("What is the capital of Namibia", "windhoek"),
    ("Who painted the Mona Lisa", ["leonardo da vinci","da vinci"]),
    ("Who made this game", "samar"),
    ("What is the capital of Canada", "ottawa"),
    ("What is the longest river in the world", "nile"),
    ("What is the capital of Switzerland", "bern"),
    ("Who wrote the play Romeo and Juliet", ["william shakespeare","shakespeare"]),
    ("Which planet is known as the Red Planet", "mars"),
    ("What is the largest ocean on Earth",[ "pacific ","pacific ocean"]),
    ("Who was the first president of Zambia", ["kenneth kaunda","kaunda"]),
    ("Which gas do plants absorb from the atmosphere", ["carbon dioxide","CO2"]),
    ("What is the hardest natural substance on Earth", "diamond"),
    ("Which flag does not have 4 sides", "nepal"),
    ("How many continents are there in the world",[ "seven","7"]),
    ("Which element has the chemical symbol K", "potassium"),
    ("Who discovered gravity", ["isaac newton","newton"]),
    ("What is the name of the largest waterfall by height ", ["angel falls","angel"]),
    ("Which is the largest desert in the world", ["antarctic","antarctic desert"]),
    ("In which country were the Olympic Games invented", "greece"),
    ("Who was the first man to walk on the moon", ["neil armstrong","armstrong"]),
    ("Which is the largest mammal in the world", "blue whale"),
    ("What is the smallest prime number", ["2","two"]),
    ("What is the currency of the United Kingdom", ["pound","pound sterling"]),
    ("Who developed the theory of relativity", ["albert einstein","einstein"]),
    ("Which is the tallest mountain in the world", ["mount everest","mt everest","everest"]),
    ("How many colors are there in a rainbow", ["7","seven"]),
    ("Which planet is closest to the Sun", "mercury"),
    ("Who invented the telephone", ["alexander graham bell","graham bell"]),
    ("What is the national animal of India", ["bengal tiger","tiger"]),
    ("Which language has the most native speakers worldwide", "mandarin"),
    ("Which country gifted the Statue of Liberty to the USA", "france"),
    ("What is the capital of Australia", "canberra"),
    ("Which planet is known for its rings", "saturn"),
    ("Who wrote The Harry Potter series", "jk rowling"),
    ("What is the freezing point of water in Celsius", ["0","zero"]),
    ("Which is the largest bird in the world", "ostrich"),
    ("Which city is known as the Big Apple", "new york"),
    ("How many players are there in a football team", ["11","eleven"]),
    ("Which metal is liquid at room temperature", "mercury"),
    ("What is the fastest land animal", "cheetah"),
    ("Who discovered penicillin", ["alexander fleming","fleming"]),
    ("Which city will host the 2028 Summer Olympics", "los angeles"),
    ("What is the largest planet in our solar system", "jupiter"),
    ("Which instrument measures temperature", "thermometer"),
    ("Which planet is known as the Blue Planet", "earth"),
    ("What is the capital of Italy", "rome"),
    ("Who was the first woman to win a Nobel Prize", "marie curie"),
    ("Which is the smallest country in the world", "vatican city"),
    ("What is the capital of Egypt", "cairo"),
    ("What is the boiling point of water in Celsius", "100"),
    ("Which is the longest bone in the human body", "femur"),
    ("Who is known as the Father of Computers", "charles babbage"),
    ("Which ocean lies between Africa and Australia", ["indian ocean","indian"]),
    ("How many days are there in a leap year", "366"),
    ("What is the capital of Germany", "berlin"),
    ("Who was the first person to climb Mount Everest", ["edmund hillary","hillary"]),
    ("Which organ purifies blood in the human body", "kidney"),
    ("What is the national flower of Japan", "cherry blossom"),
    ("Which planet is known as the Morning Star", "venus"),
    ("Who invented the light bulb", ["thomas edison","edison"]),
    ("What is the largest continent in the world", "asia"),
    ("Which country has the most population", "india"),
    ("What is the capital of South Korea", "seoul"),
    ("Which festival is known as the Festival of Lights", "diwali"),
    ("Which blood group is known as the universal donor", ["o negative","O-"]),
    ("Which is the slowest animal in the world", "sloth"),
    ("Who wrote The Odyssey", "homer"),
    ("Which organ in the human body is responsible for pumping blood", "heart"),
    ("Which is the longest wall in the world", "great wall of china"),
    ("What is the study of weather called", "meteorology"),
    ("Which country is famous for tulips", ["netherlands","the netherlands"]),
    ("Who painted The Starry Night", ["vincent van gogh","van gogh"]),
    ("What is the capital of Spain", "madrid"),
    ("Which instrument measures earthquakes", "seismograph"),
    ("Who discovered that the Earth rotates around the Sun", ["nicolaus copernicus","copernicus"]),
    ("Which country is known as the Land of Fire and Ice", "iceland"),
    ("Which chemical element is represented by Na", "sodium"),
    ("What is the capital of Russia", "moscow"),
    ("Which is the deepest point on Earth", "mariana trench"),
    ("Which planet has the most moons", "saturn"),
    ("Which vitamin is produced by sunlight", ["vitamin d","d"]),
    ("What is the capital of China", "beijing"),
    ("Which city hosted the 2024 Summer Olympics", "paris"),
    ("What is the main gas found in Earth's atmosphere", "nitrogen"),
    ("What is the capital of Brazil", "brasilia"),
    ("Who discovered America", ["christopher columbus","leif erikson","columbus"]),
    ("What is the capital of Argentina", "buenos aires"),
    ("Which country has the Great Barrier Reef", "australia"),
    ("Who wrote the national anthem of India", ["rabindranath tagore","tagore"]),
    ("Name one of the three capitals of South Africa", ["pretoria","cape town","bloemfontein"]),
    ("Which is the hottest planet in our solar system", "venus"),
    ("What is the largest island in the world", "greenland"),
    ("Which ocean is in between Europe and USA?", ["atlantic ocean","atlantic"]),
    ("Which is the most spoken language in the world", "english"),
    ("Which fruit is known as the king of fruits", "mango"),
    ("Who was the first Indian Prime Minister", ["jawaharlal nehru","nehru"]),
    ("What is the capital of Mexico", "mexico city"),
    ("Which metal is used in making coins", "nickel"),
    ("Who designed the Eiffel Tower", "gustave eiffel"),
    ("Which country invented paper", "china"),
    ("What is the capital of Sweden", "stockholm"),
    ("Which planet is farthest from the Sun", "neptune"),
    ("What is the chemical formula of water", "h2o"),
    ("Which is the largest volcano in the world", "mauna loa")

]

board = [[" " for _ in range(3)] for _ in range(3)]
player = random.choice(["X", "O"])
bank_X = 0
bank_O = 0
used_questions = set()
score_X = 0
score_O = 0
markers_placed_X = 0
markers_placed_O = 0
shuffled_this_turn=False

root = tk.Tk()
root.title("T3: Tic Tac Twist")
root.configure(bg="#121212")

instructions = (
    " HOW TO PLAY T3: TIC TAC TWIST \n\n"
    "1. Answer the questions to earn your move.\n"
    "2. Wrong = Lose your turn.Ain't no mercy here\n"
    "3. You can place your move or bank it.\n"
    "4. Banking gives you a chance to place a second marker later.But beware...chaos exists...\n"
    "Welcome to T3 — where knowledge meets chaos. A game by Sammy boy"
)
messagebox.showinfo("READ THIS SHIT", instructions)
messagebox.showinfo("Coin Toss", f"Coin toss result: Player {player} starts!")

label = tk.Label(root, text=f"Player {player}, it's your turn! Pls dont embarrass me and yourself", font=("Arial", 16, "bold"),
                 fg="white", bg="#222222", pady=10)
label.pack(fill="x")

score_label = tk.Label(root, text="Score — X: 0 | O: 0", font=("Arial", 13),
                       fg="white", bg="#121212")
score_label.pack()

status_frame = tk.Frame(root, bg="#121212")
status_frame.pack(pady=5)
bank_x_label = tk.Label(status_frame, text="Player X Banked: ❌", font=("Arial", 12),
                        fg="#ff6666", bg="#121212")
bank_x_label.grid(row=0, column=0, padx=10)
bank_o_label = tk.Label(status_frame, text="Player O Banked: ❌", font=("Arial", 12),
                        fg="#66b3ff", bg="#121212")
bank_o_label.grid(row=0, column=1, padx=10)

frame = tk.Frame(root, bg="#121212")
frame.pack(pady=10)
buttons = [[None for _ in range(3)] for _ in range(3)]

def update_banks():
    bank_x_label.config(text=f"Player X Banked: {'✅' if bank_X else '❌'}")
    bank_o_label.config(text=f"Player O Banked: {'✅' if bank_O else '❌'}")

def update_turn_label():
    if player == "X":
        label.config(text=f"Player X, it's your turn,time to shine", bg="#330000")
    else:
        label.config(text=f"Player O, it's your turn,time to shine", bg="#001a33")

def update_score():
    score_label.config(text=f"Score — X: {score_X} | O: {score_O}")

def check_winner(p):
    for i in range(3):
        if all(board[i][j] == p for j in range(3)) or all(board[j][i] == p for j in range(3)):
            return True
    if all(board[i][i] == p for i in range(3)) or all(board[i][2 - i] == p for i in range(3)):
        return True
    return False

def is_draw():
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def ask_question():
    global used_questions
    if len(used_questions) == len(questions):
        used_questions.clear()
        messagebox.showinfo("Question Bank", "All questions used! Reloading...")

    while True:
        q, a = random.choice(questions)
        if q not in used_questions:
            used_questions.add(q)
            break

    question_window = tk.Toplevel(root)
    question_window.title(f"Question for Player {player}")
    question_window.geometry("400x250")
    question_window.config(bg="#222222")

    label_q = tk.Label(question_window, text=q, wraplength=350, fg="white", bg="#222222", font=("Arial", 12))
    label_q.pack(pady=20)

    answer_var = tk.StringVar()
    entry = tk.Entry(question_window, textvariable=answer_var, font=("Arial", 12), width=30)
    entry.pack(pady=10)
    entry.focus()

    def submit():
        question_window.destroy()

    submit_btn = tk.Button(question_window, text="Submit", command=submit, font=("Arial", 11))
    submit_btn.pack(pady=10)

    root.wait_window(question_window)
    ans = answer_var.get().strip().lower()

    if not ans:
        choice = messagebox.askquestion("Cancel Detected", "Do u wanna pick another spot instead?")
        if choice == "yes":
            return None
        else:
            messagebox.showinfo("Quit", "Game ended. I spent all this time coding just for cowards to jam")
            root.destroy()
            return False

    if isinstance(a, list):
        correct = any(ans == x.strip().lower() for x in a)
        correct_display = ", ".join([x.title() for x in a])
    else:
        correct = ans == a.strip().lower()
        correct_display = a.title()

    if correct:
        messagebox.showinfo("Correct!!!", "I didnt know u had it in u, marker earned,well done!.")
        return True
    else:
        messagebox.showinfo("Wrong", f"Incorrect.Pls go read some books and watch the news. The correct answer was: {correct_display}")
        return False


def shuffle_both_players():
    players = ["X", "O"]
    reshuffle_limit = 20  
    attempt = 0

    while True:
        attempt += 1
        old_board = [row[:] for row in board]

        for i in range(3):
            for j in range(3):
                if board[i][j] != " ":
                    board[i][j] = " "
                    buttons[i][j].config(text=" ")
        for p in players:
            positions = [(i, j) for i in range(3) for j in range(3) if old_board[i][j] == p]
            empties = [(i, j) for i in range(3) for j in range(3)]
            random.shuffle(positions)
            random.shuffle(empties)
            moves = min(len(positions), len(empties))
            for k in range(moves):
                ni, nj = empties[k]
                board[ni][nj] = p
                buttons[ni][nj].config(text=p, fg="#f54242" if p == "X" else "#4bf542", state="disabled")

        if not (check_winner("X") or check_winner("O")) or attempt >= reshuffle_limit:
            break
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                buttons[i][j].config(state="normal")

    root.config(bg="#550000")
    root.after(300, lambda: root.config(bg="#121212"))
    messagebox.showinfo("CHAOS TIME", "Markers shuffled (but no instant wins this time)!")


def relocate_if_conflict(r, c, player):
    opponent = "O" if player == "X" else "X"
    if board[r][c] == opponent:
        empties = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        if empties:
            new_r, new_c = random.choice(empties)
            board[new_r][new_c] = opponent
            buttons[new_r][new_c].config(text=opponent, fg="#f54242" if opponent == "X" else "#4bf542", state="disabled")
        board[r][c] = " "
        buttons[r][c].config(text=" ")

def make_move(r, c):
    global player, bank_X, bank_O, score_X, score_O, markers_placed_X, markers_placed_O,shuffled_this_turn

    if board[r][c] != " ":
        messagebox.showinfo("Iwe", "Spot already taken. Are you blind?")
        return

    result = ask_question()
    if result is None or result is False:
        switch_turn()
        return

    current_bank = bank_X if player == "X" else bank_O
    opponent = "O" if player == "X" else "X"

    total_X = sum(cell == "X" for row in board for cell in row)
    total_O = sum(cell == "O" for row in board for cell in row)
    can_use_bank = (total_X >= 2 and total_O >= 2)

    if current_bank == 1 and can_use_bank:
        action = messagebox.askquestion("Your Move", "You have a banked move.\nUse it now(Please do)?")
        if action == "yes":
            if not shuffled_this_turn:
                shuffle_both_players()
                shuffled_this_turn = True

        # Place the first marker after the shuffle
            relocate_if_conflict(r, c, player)
            board[r][c] = player
            buttons[r][c].config(
                text=player,
                fg="#f5f542" if player == "X" else "#42f5c5",
                state="disabled"
            )

        # Mark that the banked move was used
            if player == "X":
                bank_X = 0
            else:
                bank_O = 0
            update_banks()

            messagebox.showinfo(
                "Second Move",
                f"Player {player}, place your second marker for your banked move (no more shuffle this time)."
            )

            def second_click(rr, cc):
                global shuffled_this_turn
                if board[rr][cc] in [" ", opponent]:
                    relocate_if_conflict(rr, cc, player)
                    board[rr][cc] = player
                    buttons[rr][cc].config(
                        text=player,
                        fg="#f5f542" if player == "X" else "#42f5c5",
                        state="disabled"
                    )
                    restore_main_commands()

                    if check_winner(player):
                        declare_winner(player)
                        shuffled_this_turn=False
                        return
                    switch_turn()
                    shuffled_this_turn=False
                else:
                    messagebox.showinfo("Invalid", "Spot is taken. Please go to an optician—you need an eye test.")

            for i in range(3):
                for j in range(3):
                    buttons[i][j].config(command=lambda rr=i, cc=j: second_click(rr, cc))

            return

        else:
            board[r][c] = player
            buttons[r][c].config(text=player, fg="#ffff99" if player == "X" else "#99ffff", state="disabled")

    elif (player == "X" and not bank_X) or (player == "O" and not bank_O):
        choice = messagebox.askquestion("Your Move", "Do you want to bank this move for later?")
        if choice == "yes":
            if player == "X":
                bank_X = 1
            else:
                bank_O = 1
            update_banks()
            messagebox.showinfo("Banked", f"Player {player} banked their move.")
            switch_turn()
            return
        else:
            board[r][c] = player
            buttons[r][c].config(text=player, fg="#ffff99" if player == "X" else "#99ffff", state="disabled")
    else:
        board[r][c] = player
        buttons[r][c].config(text=player, fg="#ffff99" if player == "X" else "#99ffff", state="disabled")

    if check_winner(player):
        declare_winner(player)
        return
    if is_draw():
        messagebox.showinfo("Draw", "Fuck,need to rerun this code")
        reset_board()
        return
    switch_turn()

def switch_turn():
    global player
    player = "O" if player == "X" else "X"
    update_turn_label()

def restore_main_commands():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(command=lambda r=i, c=j: make_move(r, c))

def declare_winner(p):
    global score_X, score_O
    if p == "X":
        score_X += 1
    else:
        score_O += 1
    bank_X=0
    bank_O=0
    update_score()
    update_banks()
    again = messagebox.askyesno("Winner winner chicken dinner", f"Player {p} wins!\nPlay again?")
    if again:
        reset_board()
    else:
        root.destroy()

def reset_board():
    global board, player, bank_X, bank_O
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")
    bank_X = 0
    bank_O = 0
    update_banks()
    player = random.choice(["X", "O"])
    update_turn_label()

for i in range(3):
    for j in range(3):
        b = tk.Button(frame, text=" ", font=("Arial", 22, "bold"),
                      width=5, height=2, bg="#1f1f1f", fg="white",
                      activebackground="#444444", relief="ridge", bd=3,
                      command=lambda r=i, c=j: make_move(r, c))
        b.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = b

update_banks()
update_turn_label()
root.mainloop()
