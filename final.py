import random

# Hangman visuals
hangman_graphics = [
    """
    ________
    |      |
    |      
    |      
    | | D E A D |     
    |
    """,
    """
    ________
    |      |
    |      O /
    |       
    |       
    | 
    """,
    """
    ________
    |      |
    |      O
    |     / 
    |       
    |
    """,
    """
    ________
    |      |
    |      O
    |     /| 
    |       
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |       
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |     / 
    |
    """,
    """
    ________
    |      |
    |      O
    |     /|\\
    |     / \\
    |
    """
]

# Word categories and words
word_categories = {
    "Singers": ["adele", "drake", "rihanna", "beyonce", "eminem"],
    "TV Shows": ["friends", "lucifer", "riverdale", "euphoria", "vikings"],
    "Classmates": ["alberto", "guillermo", "natalia", "soraya", "timothy"]
}

# Message Possibilities
possibilities_correct = ["Correct guess", "Great guess", "You're getting closer, good job", "Amazing Intuition", "You have nice techniques"]
possibilities_incorrect = ["Wrong attempt", "You're close, think a bit more", "Your hangman might die :("]

# Function to choose a random word from a category
def choose_word(category):
    return random.choice(word_categories[category])

# Function to choose a random category
def choose_category():
    chosen_category = random.choice(list(word_categories.keys()))
    print(f"Category: {chosen_category}")
    return chosen_category

# Function to display hangman graphic
def display_hangman(guesses):
    print(hangman_graphics[6 - guesses])

# Function to check if the word is guessed
def is_word_guessed(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Function to play Hangman
def play_hangman():
    while True:
        # Introduction
        print("Welcome to Hangman!")
        name = input("Enter your name: ")
        print(f"Hello, {name}! Let's play Hangman.")

        # Choose a category and a word
        category = choose_category()
        word = choose_word(category)
        guessed_letters = []
        incorrect_guesses = 0

        # Game loop
        while incorrect_guesses < 6:
            # Display hangman graphic
            display_hangman(incorrect_guesses)

            # Display word with guessed letters
            display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
            print(display)

            # Player's guess
            guess = input("Guess a letter: ").lower()

            # Check if the guessed letter is correct
            if guess in word:
                correct_message = random.choice(possibilities_correct)
                print(correct_message, name, "!")
                guessed_letters.append(guess)
            else:
                incorrect_message = random.choice(possibilities_incorrect)
                print(incorrect_message, name, "!")
                incorrect_guesses += 1

            # Check if the word is guessed
            if is_word_guessed(word, guessed_letters):
                print(f"Congratulations, {name}! You guessed the word: {word}")
                break

        else:
            print("Sorry, you ran out of lives. The word was:", word)
            print(hangman_graphics[0])

        # Ask the player if they want to play again
        restart = input("Do you wish to restart? (yes/no): ").lower()
        if restart != "yes":
            print("Thanks for playing!")
            break

# Play the game
play_hangman()