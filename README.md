# 🎮 Hangman Game - CodeAlpha Python Programming Internship

A fun and interactive text-based Hangman game built with Python. Guess the word letter by letter before running out of attempts!

## 🎯 Overview

This is **Task 1** (compulsory) from the CodeAlpha Python Programming Internship. It demonstrates fundamental Python concepts through a classic guessing game.

### Game Rules
- The computer picks a random word from a predefined list
- You have **6 incorrect guesses** before losing
- Guess letters one at a time
- Reveal the complete word to win
- Game ends when you win or run out of guesses

## ✨ Features

- ✅ Random word selection from 5 predefined words
- ✅ Input validation to ensure valid letter guesses
- ✅ Duplicate guess prevention
- ✅ ASCII art hangman visualization (7 stages)
- ✅ Real-time game state display
- ✅ Win/Loss detection with statistics
- ✅ Multiple round support
- ✅ User-friendly console interface

## 📦 Project Files

```
CodeAlpha_HangmanGame/
├── hangman_game.py                      # Main executable Python script
├── Hangman_Game_CodeAlpha.ipynb         # Jupyter Notebook (Google Colab compatible)
├── PROJECT_REPORT.md                    # Detailed project documentation
├── README.md                            # This file
└── WORD_LIST.txt                        # Predefined words (optional reference)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No additional libraries required (only uses built-in `random` module)

### Run the Game

**Option 1: Direct Python Execution**
```bash
python hangman_game.py
```

**Option 2: Jupyter Notebook (Local)**
```bash
jupyter notebook Hangman_Game_CodeAlpha.ipynb
```

**Option 3: Google Colab (Cloud)**
1. Upload `Hangman_Game_CodeAlpha.ipynb` to [Google Colab](https://colab.research.google.com)
2. Run all cells
3. Play in the browser

## 📖 How to Play

1. **Start the game** - The program will display a welcome message
2. **See the word** - Blanks represent letters: `_ _ _ _`
3. **Guess a letter** - Type any letter (A-Z) when prompted
4. **Get feedback** - See if your guess is correct or wrong
5. **Track progress** - Watch the hangman build with each wrong guess
6. **Win or Lose** - Reveal the word to win, or run out of guesses to lose
7. **Play again** - Choose to play another round or exit

## 🎓 Python Concepts Demonstrated

| Concept | Usage |
|---------|-------|
| **Variables** | Storing word, guessed letters, tries |
| **Data Types** | Strings, Lists, Integers |
| **Lists** | Word list, guessed letters tracking |
| **Strings** | Word manipulation, display formatting |
| **Loops** | `while` loops for game iteration |
| **Conditionals** | `if-else` for game logic |
| **Functions** | Modular code organization |
| **Input/Output** | User interaction and feedback |
| **Random Module** | Random word selection |
| **Error Handling** | Input validation |

## 📊 Game Example

```
==================================================
WELCOME TO HANGMAN GAME!
==================================================
The word has 6 letters.
You have 6 incorrect guesses allowed.
==================================================

         --------
         |      |
         |      
         |    
         |      
         |     
         -

==================================================
Word to guess: _ _ _ _ _ _
Guessed letters: None
Remaining tries: 6
==================================================

Guess a letter: e
✅ Correct! 'E' is in the word!

==================================================
Word to guess: _ _ _ _ _ E
Guessed letters: E
Remaining tries: 6
==================================================

Guess a letter: a
✅ Correct! 'A' is in the word!

[... continue playing ...]

==================================================
🎉 CONGRATULATIONS! YOU WON! 🎉
The word was: PYTHON
Total guesses: 8
Incorrect guesses: 2
==================================================
```

## 🛠️ Technical Details

### Word List
```python
['python', 'hangman', 'computer', 'programming', 'internship']
```

### Main Functions
- `initialize_game()` - Set up game state
- `display_hangman(tries)` - Show ASCII art
- `display_game_state()` - Show progress
- `get_valid_guess()` - Validate input
- `process_guess()` - Handle guess logic
- `play_hangman_game()` - Main game loop
- `main()` - Allow multiple rounds

### Game States
- **Running**: Word not fully guessed, tries > 0
- **Won**: All letters revealed
- **Lost**: Tries reached 0 before completing word

## 📝 Code Quality

✅ **Well-commented** - Clear explanations throughout  
✅ **Modular design** - Functions for each component  
✅ **Input validation** - Handles invalid inputs gracefully  
✅ **User-friendly** - Clear prompts and feedback  
✅ **Error-free** - Tested on Python 3.6+  

## 🧪 Testing

All game features have been tested:
- ✅ Correct/incorrect guess handling
- ✅ Duplicate guess prevention
- ✅ Input validation
- ✅ Win condition detection
- ✅ Loss condition detection
- ✅ Multiple rounds
- ✅ ASCII art progression

## 🔄 Future Enhancements

Potential improvements for future versions:
- Difficulty levels (Easy/Normal/Hard)
- Word categories (Animals, Countries, etc.)
- Hints system
- Scoring and leaderboard
- External word file or API
- GUI interface
- Multiplayer mode
- Statistics tracking

## 👤 Author

**Abdul Samad**
- Education: BS Mathematics, Sukkur IBA University
- Internship: CodeAlpha Python Programming
- Location: Pakistan (Remote)
- LinkedIn: [Abdul Samad](https://linkedin.com)

## 🎓 Internship Information

**Organization:** CodeAlpha  
**Program:** Python Programming Internship  
**Duration:** Virtual/Remote  
**Task:** Task 1 - Hangman Game (Compulsory)  
**Status:** ✅ Completed  

## 🤝 Attribution

This project is completed as part of the CodeAlpha Python Programming Internship.

**CodeAlpha Information:**
- Website: www.codealpha.tech
- WhatsApp: +91 8052293611
- Email: services@codealpha.tech

## 📄 License

This project is open-source and available for educational purposes.

## 🙏 Acknowledgments

- CodeAlpha for the internship opportunity
- Python community for excellent documentation
- Sukkur IBA University for the educational foundation

---

**Last Updated:** May 31, 2026  
**Status:** ✅ Complete and Ready for Submission

**Next Steps:**
1. Create video explanation for LinkedIn
2. Upload to GitHub with this README
3. Share on LinkedIn with project link
4. Submit via CodeAlpha submission form

Happy playing! 🎮
