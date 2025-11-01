import random
import tkinter as tk
from tkinter import messagebox, simpledialog

questions = [
    ("What is the capital of Zambia", "lusaka"),
    ("Who painted the Mona Lisa", ["leonardo da vinci","da vinci"]),
    ("Who made this game", "samar"),
    ("What is the capital of Canada", "ottawa"),
    ("What is the longest river in the world", "nile"),
    ("What is the capital of France", "paris"),
    ("Who wrote the play Romeo and Juliet", ["william shakespeare","shakespeare"]),
    ("Which planet is known as the Red Planet", "mars"),
    ("What is the largest ocean on Earth",[ "pacific ","pacific ocean"]),
    ("Who was the first President of the United States", "george washington"),
    ("Which gas do plants absorb from the atmosphere", ["carbon dioxide","CO2"]),
    ("What is the hardest natural substance on Earth", "diamond"),
    ("What is the capital of Japan", "tokyo"),
    ("How many continents are there in the world",[ "seven","7"]),
    ("Which element has the chemical symbol K", "potassium"),
    ("Who discovered gravity", ["isaac newton","newton"]),
    ("Which country is known as the Land of the Rising Sun", "japan"),
    ("Which is the largest desert in the world", ["antarctic","antarctic desert"]),
    ("In which country were the Olympic Games invented", "greece"),
    ("Who was the first man to walk on the moon", "neil armstrong"),
    ("Which is the largest mammal in the world", "blue whale"),
    ("What is the smallest prime number", "2"),
    ("What is the currency of the United Kingdom", ["pound","pound sterling"]),
    ("Who developed the theory of relativity", ["albert einstein","einstein"]),
    ("Which is the tallest mountain in the world", ["mount everest","mt everest","everest"]),
    ("How many colors are there in a rainbow", "7"),
    ("Which planet is closest to the Sun", "mercury"),
    ("Who invented the telephone", "alexander graham bell"),
    ("What is the national animal of India", ["bengal tiger","tiger"]),
    ("Which language has the most native speakers worldwide", "mandarin"),
    ("Which country gifted the Statue of Liberty to the USA", "france"),
    ("What is the capital of Australia", "canberra"),
    ("Which planet is known for its rings", "saturn"),
    ("Who wrote The Harry Potter series", ["j k rowling","jk rowling"]),
    ("What is the freezing point of water in Celsius", "0"),
    ("Which is the largest bird in the world", "ostrich"),
    ("Which city is known as the Big Apple", "new york"),
    ("How many players are there in a football team", "11"),
    ("Which metal is liquid at room temperature", "mercury"),
    ("What is the fastest land animal", "cheetah"),
    ("Who discovered penicillin", "alexander fleming"),
    ("Which country hosted the 2016 Summer Olympics", "brazil"),
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
    ("Who was the first person to climb Mount Everest", "edmund hillary"),
    ("Which organ purifies blood in the human body", "kidney"),
    ("What is the national flower of Japan", "cherry blossom"),
    ("Which planet is known as the Morning Star", "venus"),
    ("Who invented the light bulb", "thomas edison"),
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
    ("What is the national sport of Japan", ["sumo wrestling","sumo"]),
    ("Which country is known as the Land of Fire and Ice", "iceland"),
    ("Which chemical element is represented by Na", "sodium"),
    ("What is the capital of Russia", "moscow"),
    ("Which is the deepest point on Earth", "mariana trench"),
    ("Which planet has the most moons", "saturn"),
    ("Which vitamin is produced by sunlight", ["vitamin d","d"]),
    ("What is the capital of China", "beijing"),
    ("Which city hosted the 2020 Summer Olympics", "tokyo"),
    ("What is the main gas found in Earth's atmosphere", "nitrogen"),
    ("What is the capital of Brazil", "brasilia"),
    ("Who discovered America", ["christopher columbus","leif erikson"]),
    ("What is the capital of Argentina", "buenos aires"),
    ("Which country has the Great Barrier Reef", "australia"),
    ("Who wrote the national anthem of India", "rabindranath tagore"),
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
wrong_X = 0
wrong_O = 0

root = tk.Tk()
root.title("T3: Tic Tac Twist")

instructions = (
    " HOW TO PLAY T3: TIC TAC TWIST \n\n"
    "1️⃣ Each turn, answer a GK question to earn your move.\n\n"
    "2️⃣ Wrong = Turn is lost,no mercy in this game my guy\n\n"
    "3️⃣ After answering correctly, you can:\n"
    "    Place a marker\n"
    "    Bank it for later (you can only have ONE banked move)\n"
    "    Use a banked move anytime (CAUTION — your markers randomly shuffle doing so!)\n\n"
    "4️⃣ Banking skips your turn now, but lets you unleash chaos later.\n\n"
    "5️⃣ 3 in a row = win, full board = draw.\n\n"
    " Welcome to T3 — where knowledge meets chaos!"
)

messagebox.showinfo("How to Play", instructions)
messagebox.showinfo("Coin Toss", f" Coin toss result: Player{player} starts!")

label = tk.Label(root, text=f"Player {player}, its ur turn, pls dont embarass urself",
                 font=("Arial", 16, "bold"), fg="white", bg="black", pady=10)
label.pack(fill="x")

status_frame = tk.Frame(root)
status_frame.pack(pady=5)

bank_x_label = tk.Label(status_frame, text="Player X Banked: ❌", font=("Arial", 12))
bank_x_label.grid(row=0, column=0, padx=10)
bank_o_label = tk.Label(status_frame, text="Player O Banked: ❌", font=("Arial", 12))
bank_o_label.grid(row=0, column=1, padx=10)

frame = tk.Frame(root)
frame.pack(pady=10)

buttons = [[None for _ in range(3)] for _ in range(3)]


def update_banks():
    bank_x_label.config(text=f"Player X Banked: {'✅' if bank_X else '❌'}")
    bank_o_label.config(text=f"Player O Banked: {'✅' if bank_O else '❌'}")

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw():
    return all(board[i][j] != " " for i in range(3) for j in range(3))


used_questions = set()

def ask_question():
    global used_questions
    if len(used_questions) == len(questions):
        used_questions.clear()
        messagebox.showinfo("Question bank full")
    while True:
        q, a = random.choice(questions)
        if q not in used_questions:
            used_questions.add(q)
            break

    question, answer = q, a
    ans = simpledialog.askstring(
        f"GK Question for Player {player}",
        f"Get this question correct to place a marker!\n\n{question}"
    )

    if ans is None:
        choice = messagebox.askquestion(
            "Cancel Detected",
            "You pressed cancel!\nDo you want to pick another spot instead or quit?"
        )
        if choice == "yes":
            return None
        else:
            messagebox.showinfo("Quit", "Game ends because this one is a coward ")
            root.destroy()
            return False

    ans = ans.strip().lower()
    if isinstance(answer, list):
        correct = any(ans == a.strip().lower() for a in answer)
        correct_answers = [a.strip().title() for a in answer]
    else:
        correct = ans == answer.strip().lower()
        correct_answers = [answer.strip().title()]

    if correct:
        messagebox.showinfo("Correct", "Damn ok, I'm surprised u had it in u! Marker secured ")
        return True
    else:
        correct_display = ", ".join(correct_answers)
        messagebox.showinfo(
            "Wrong",
            f"Player{player}... Honestly, I ain't even surprised — you're wrong mf \n\n"
            f"The correct answer was: {correct_display}"
        )
        return False



def shuffle_markers(opponent):
    
    positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == opponent]
    empties = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

    if not positions:
        messagebox.showinfo("Chaos", f"Player{opponent} had no markers — chaos did nothing 😅")
        return

    random.shuffle(positions)
    random.shuffle(empties)

    moves = min(len(positions), len(empties)) if empties else len(positions)

    for i, j in positions[:moves]:
        board[i][j] = " "
        buttons[i][j].config(text=" ")
    for k in range(moves):
        if empties:
            ni, nj = empties[k % len(empties)]
            board[ni][nj] = opponent
            buttons[ni][nj].config(text=opponent, state="disabled")
        else:
            ni, nj = random.choice([(x, y) for x in range(3) for y in range(3)])
            board[ni][nj] = opponent
            buttons[ni][nj].config(text=opponent, state="disabled")

    messagebox.showinfo("CHAOS!!", f" Player{opponent}'s markers have been shuffled across the board! CHAOS TIME!")
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                buttons[i][j].config(state="normal")
def relocate_if_conflict(r, c, player):

    opponent = "O" if player == "X" else "X"
    if board[r][c] == opponent:
        empties = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

        if empties:
            new_r, new_c = random.choice(empties)
            board[new_r][new_c] = opponent
            buttons[new_r][new_c].config(text=opponent, state="disabled")
        board[r][c] = " "
        buttons[r][c].config(text=" ")



def make_move(r, c):
    global player, bank_X, bank_O, wrong_X, wrong_O

    if board[r][c] != " ":
        messagebox.showinfo("Taken", "Spot is taken, cant u see?")
        return
    result = ask_question()
    if result is None:
        return
    elif not result:
        if player == "X":
            wrong_X += 1
        else:
            wrong_O += 1
        player = "O" if player == "X" else "X"
        label.config(text=f"Player{player}, its ur turn, pls dont embarass urself")
        return
    current_bank = bank_X if player == "X" else bank_O
    opponent = "O" if player == "X" else "X"
    has_bank_text = "✅ You already have a banked move ready!" if current_bank else "❌ No banked move yet."

    if current_bank == 1:
        action = messagebox.askquestion(
            "Your Move",
            f"{has_bank_text}\n\nDo u want to:\n\n"
            "Yes = Use ur banked chaos move NOW (and play 2 markers!)\n"
            "No = Place normally (skip banking this turn)"
        )

        if action == "yes":
            shuffle_markers(opponent)  
            relocate_if_conflict(r, c, player)
            board[r][c] = player
            buttons[r][c].config(text=player, state="disabled")
            messagebox.showinfo("Second Move", f"Player{player}, place your 2nd marker for your banked move!")
            
            def second_click(rr, cc):
                if board[rr][cc] == " " or board[rr][cc] == opponent:
                    relocate_if_conflict(rr, cc, player)
                    board[rr][cc] = player
                    buttons[rr][cc].config(text=player, state="disabled")

                    if player == "X":
                        bank_X = 0
                    else:
                        bank_O = 0
                    update_banks()
                    for i in range(3):
                        for j in range(3):
                            buttons[i][j].config(command=lambda r=i, c=j: make_move(r, c))
                    if check_winner(player):
                        messagebox.showinfo("Winner", f"Player{player} wins with chaos!")
                        root.destroy()
                        return
                    switch_turn()
                else:
                    messagebox.showinfo("Invalid", "That spot is taken!")

            for i in range(3):
                for j in range(3):
                    buttons[i][j].config(command=lambda rr=i, cc=j: second_click(rr, cc))
            return

        else:
            board[r][c] = player
            buttons[r][c].config(text=player, state="disabled")

    else:
        choice = messagebox.askquestion(
            "Your Move",
            f"{has_bank_text}\n\nDo u want to BANK this move for later?\n\nYes = Bank it, No = Place now."
        )
        if choice == "yes":
            if player == "X":
                bank_X = 1
            else:
                bank_O = 1
            update_banks()
            messagebox.showinfo("Banked", f"Ayt Player{player}, ur marker is banked.")
            switch_turn()
            return
        else:
            board[r][c] = player
            buttons[r][c].config(text=player, state="disabled")

    if check_winner(player):
        messagebox.showinfo("Winner", f"Wowwww player{player} wins!..the worst player to ever win.")
        root.destroy()
        return

    if is_draw():
        messagebox.showinfo("Drawwww", "Fuck, need to rerun this code again ffs.")
        root.destroy()
        return

    switch_turn()

def switch_turn():
    global player
    player = "O" if player == "X" else "X"
    label.config(text=f"Player{player}, its ur turn, pls dont embarass urself")

for i in range(3):
    for j in range(3):
        b = tk.Button(frame, text=" ", font=("Arial", 22), width=5, height=2,
                      command=lambda r=i, c=j: make_move(r, c))
        b.grid(row=i, column=j)
        buttons[i][j] = b

update_banks()
root.mainloop()
