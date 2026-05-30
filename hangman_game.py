"""
Hangman Game - CodeAlpha Internship Task 1
Author: Abdul Samad
Description: A simple text-based Hangman game where players guess letters to find the hidden word.
"""

import random


def display_hangman(tries):
    """
    Display the hangman stages based on remaining tries.
    """
    stages = [  # Final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # Head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # Head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def get_word():
    """
    Randomly select a word from the predefined list.
    """
    word_list = ['python', 'hangman', 'computer', 'programming', 'internship']
    return random.choice(word_list).upper()


def play_game():
    """
    Main game logic for Hangman.
    """
    word = get_word()
    word_length = len(word)
    guessed = False
    guessed_letters = []
    guessed_word = ['_' for _ in range(word_length)]
    tries = 6
    
    print("\n" + "="*50)
    print("WELCOME TO HANGMAN GAME!")
    print("="*50)
    print(f"The word has {word_length} letters.")
    print("You have 6 incorrect guesses allowed.")
    print("="*50 + "\n")
    
    # Main game loop
    while not guessed and tries > 0:
        print(display_hangman(tries))
        print("\nWord to guess: " + ' '.join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Remaining tries: {tries}\n")
        
        # Get user input
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"❌ You already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guessed letter is in the word
        if guess in word:
            print(f"✅ Correct! '{guess}' is in the word!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"❌ Wrong! '{guess}' is not in the word.")
            tries -= 1
        
        # Check if player won
        if '_' not in guessed_word:
            guessed = True
            print("\n" + "="*50)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"The word was: {word}")
            print("="*50 + "\n")
    
    # Game over - player lost
    if not guessed:
        print(display_hangman(tries))
        print("\n" + "="*50)
        print("💀 GAME OVER! YOU LOST! 💀")
        print(f"The correct word was: {word}")
        print("="*50 + "\n")


def main():
    """
    Main function to run the game loop.
    Allows players to play multiple rounds.
    """
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\n" + "="*50)
            print("Thanks for playing! Goodbye! 👋")
            print("="*50 + "\n")
            break


if __name__ == "__main__":
    main()
