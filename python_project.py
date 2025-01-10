import random
import requests

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
        ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
        ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
        ---
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |      
        ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
        ---
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        ---
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        ---
        """,
    ]
    return stages[tries]

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()
        word = response.json()[0]
        return word.upper()
    except requests.RequestException:
        print("Error fetching a random word. Using a fallback word.")
        return "FALLBACK".upper()

def play_game():
    word = get_random_word()
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}.")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word correctly!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Better luck next time!")

if __name__ == "__main__":
    play_game()
