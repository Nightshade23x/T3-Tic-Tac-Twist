import random
from tkinter import messagebox

# ---------------------------
#  INSTRUCTIONS TEXT
# ---------------------------
instructions = (
    " HOW TO PLAY T3: TIC TAC TWIST \n\n"
    "1. Answer the questions to earn your move.\n"
    "2. Wrong = Lose your turn.\n"
    "3. You can place your move or bank it.\n"
    "4. Banking gives you a chance to place a second marker later.\n"
    "   But beware... CHAOS MODE may shuffle everything!\n\n"
    "Welcome to T3 — where knowledge meets chaos."
)


# ---------------------------
#  QUESTION BANK (ADD MORE)
# ---------------------------
questions = [
    ("What is the capital of Namibia", "windhoek"),
    ("Who painted the Mona Lisa", ["leonardo da vinci","da vinci"]),
    ("Who made this game", ["samar","sammy"]),
    ("What is the capital of Canada", "ottawa"),
    ("What is the capital of Switzerland", "bern"),
    ("Who wrote the play Romeo and Juliet", ["william shakespeare","shakespeare"]),
    ("What is the largest ocean on Earth",[ "pacific ","pacific ocean"]),
    ("Who was the first president of Zambia", ["kenneth kaunda","kaunda"]),
    ("Which gas do plants absorb from the atmosphere", ["carbon dioxide","CO2"]),
    ("What is the hardest natural substance on Earth", "diamond"),
    ("Which country's flag is not a quadrilateral", "nepal"),
    ("How many continents are there in the world",[ "seven","7"]),
    ("Which element has the chemical symbol K", "potassium"),
    ("Who discovered gravity", ["isaac newton","newton"]),
    ("What is the name of the tallest waterfall in the world ", ["angel falls","angel"]),
    ("Which is the largest desert in the world(in general)", ["antarctic","antarctic desert"]),
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
    ("Who wrote the Harry Potter series", "jk rowling"),
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
    ("Who was the first woman to win a Nobel Prize", ["marie curie","curie"]),
    ("Which is the smallest country in the world", "vatican city"),
    ("What is the capital of Egypt", "cairo"),
    ("What is the boiling point of water in Celsius", "100"),
    ("Which is the longest bone in the human body", "femur"),
    ("Who is known as the Father of Computers", ["charles babbage","babbage"]),
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
    ("Which blood group is known as the universal donor", ["o negative","o-","O-"]),
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
    ("Which is the largest volcano in the world", "mauna loa"),
    ("What is the capital of Finland", "helsinki"),
    ("Which planet is known as the Gas Giant", "jupiter"),
    ("Who invented the World Wide Web", ["tim berners lee","berners lee"]),
    ("What is the largest lake in the world", ["caspian sea","caspian"]),
    ("What is the longest river in Asia", ["yangtze","yangtze river"]),
    ("Which scientist proposed the three laws of motion", ["isaac newton","newton"]),
    ("What is the capital of Turkey", "ankara"),
    ("Which city is famous for the Colosseum", "rome"),
    ("Who wrote the play Hamlet", ["william shakespeare","shakespeare"]),
    ("What is the capital of Japan", "tokyo"),
    ("Which is the coldest place on Earth", ["antarctica","vostok station"]),
    ("Which animal is known as the Ship of the Desert", "camel"),
    ("What is the capital of Norway", "oslo"),
    ("What is the largest ocean predator", ["great white shark","great white"]),
    ("Which metal is the best conductor of electricity", "silver"),
    ("Who discovered electricity", ["benjamin franklin","franklin"]),
    ("What is the capital of Portugal", "lisbon"),
    ("Which country is known as the Land of the Rising Sun", "japan"),
    ("Which organ controls the nervous system", "brain"),
    ("Which country has the largest number of islands", "sweden"),
    ("What is the largest internal organ in the human body", "liver"),
    ("Which city is known as the City of Love", "paris"),
    ("What is the capital of Thailand", "bangkok"),
    ("What do bees collect to make honey", "nectar"),
    ("Which planet has the Great Red Spot", "jupiter"),
    ("What is the square root of 144", ["12","twelve"]),
    ("Which scientist proposed the theory of evolution", ["charles darwin","darwin"]),
    ("What is the capital of Netherlands", ["amsterdam","the hague"]),
    ("Which is the hottest continent on Earth", "africa"),
    ("Who was the first woman to go to space", ["valentina tereshkova","tereshkova"]),
    ("How many teeth does an adult human have", ["32","thirty two"]),
    ("What is the largest reptile in the world", "saltwater crocodile"),
    ("Which gas do humans exhale", "carbon dioxide"),
    ("Who is the author of The Lord of the Rings", ["jrr tolkien","tolkien"]),
    ("What is the capital of Indonesia", "jakarta"),
    ("Which country is the largest producer of coffee", "brazil"),
    ("Which continent has the most countries", "africa"),
    ("What is the hardest rock", "diamond"),
    ("What is the capital of France", "paris"),
    ("Which planet is known as the Red Planet", "mars"),
    ("Who wrote The Jungle Book", ["rudyard kipling","kipling"]),
    ("Which is the largest river in Europe", ["volga","volga river"]),
    ("What is the national currency of Japan", "yen"),
    ("Who invented the airplane", ["wright brothers","wright"]),
    ("Which animal is known as the King of the Jungle", "lion"),
    ("Who painted The Last Supper", ["leonardo da vinci","da vinci"]),
    ("Which is the largest flower in the world", "rafflesia"),
    ("What is the capital of Saudi Arabia", "riyadh"),
    ("Who discovered the theory of radioactivity", ["marie curie","curie"]),
    ("Which is the deepest ocean", "pacific"),
    ("What is the longest river in the world", "nile"),
    ("Who built the Taj Mahal", ["shah jahan","jahan"]),
    ("Which is the tallest building in the world", ["burj khalifa","burj"]),
    ("What is the capital of New Zealand", "wellington"),
    ("Who is known as the Iron Man of India", ["sardar patel","patel"]),
    ("What is the capital of Sri Lanka", ["colombo","sri jayawardenepura kote"]),
    ("Which planet is called Earth's Twin", "venus"),
    ("Which organ helps in breathing", "lungs"),
    ("Who wrote The Da Vinci Code", ["dan brown","brown"]),
    ("What is the currency of China", "yuan"),
    ("What is the capital of Nepal", "kathmandu"),
    ("What is the largest coral reef system in the world", "great barrier reef"),
    ("Which is the largest peninsula in the world", ["arabian peninsula","arabia"]),
    ("Who invented the computer mouse", ["douglas engelbart","engelbart"]),
    ("What is the capital of Denmark", "copenhagen"),
    ("Which planet has a day longer than a year", "venus"),
    ("Which is the largest bay in the world", ["bay of bengal","bengal"]),
    ("Who discovered the law of planetary motion", ["johannes kepler","kepler"]),
    ("What is the brightest star in the night sky", "sirius"),
    ("What is the capital of Philippines", "manila"),
    ("Which is the hottest place on Earth", ["death valley","death valley california"]),
    ("What is the capital of Iran", "tehran"),
    ("Which is the longest mountain range in the world", "andes"),
    ("What is the national animal of China", ["giant panda","panda"])
]



# You will later paste ALL your questions into this list.


# ---------------------------
#  GET A RANDOM UNUSED QUESTION
# ---------------------------
def get_question():
    """
    Returns a fresh (question, answer) pair.
    Uses a simple reload mechanism if all questions are used.
    """

    from state import used_questions  # import inside to avoid circular loops

    if len(used_questions) == len(questions):
        used_questions.clear()
        messagebox.showinfo("Question Bank", "All questions used! Reloading...")

    # pick a question not used yet
    while True:
        q, a = random.choice(questions)
        if q not in used_questions:
            used_questions.add(q)
            return (q, a)
