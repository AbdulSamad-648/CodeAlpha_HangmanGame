# HANGMAN GAME - PROJECT REPORT
## CodeAlpha Python Programming Internship - Task 1

---

## 📋 Project Information

**Project Name:** Hangman Game  
**Author:** Abdul Samad  
**Organization:** CodeAlpha (Python Programming Internship)  
**Date:** May 31, 2026  
**Task Type:** Task 1 (Compulsory)  
**Status:** ✅ Completed  

---

## 📌 Project Overview

The Hangman Game is a classic text-based game implemented in Python where a player attempts to guess a hidden word by suggesting letters within a limited number of incorrect guesses. This project demonstrates fundamental Python concepts including loops, conditionals, strings, lists, and functions.

### Game Objective
- Guess the randomly selected word letter by letter
- Player has a maximum of 6 incorrect guesses
- Win by revealing all letters before running out of guesses
- Lose if 6 incorrect guesses are made

---

## 🎯 Requirements & Specifications

### Task Requirements (from CodeAlpha)
✅ Create a simple text-based Hangman game  
✅ Use a small list of 5 predefined words  
✅ Limit incorrect guesses to 6  
✅ Basic console input/output  
✅ No graphics or audio required  

### Key Concepts Used
- **random module** - For random word selection
- **while loops** - For game iteration
- **if-else statements** - For game logic
- **strings** - For word manipulation
- **lists** - For storing guessed letters and word progress
- **functions** - For code organization and reusability

---

## 🏗️ Project Structure

```
hangman_game/
│
├── hangman_game.py                 # Main Python script
├── Hangman_Game_CodeAlpha.ipynb    # Jupyter Notebook (Google Colab compatible)
├── PROJECT_REPORT.md               # This file
└── README.md                        # Usage instructions
```

---

## 💻 Technical Implementation

### 1. **Word List & Selection**
```python
WORD_LIST = ['python', 'hangman', 'computer', 'programming', 'internship']
```
- 5 predefined words relevant to programming and the internship
- Random selection ensures variability across games

### 2. **Game State Management**
The game maintains the following state variables:
- `word` - The current word to guess (uppercase)
- `guessed_letters` - List of letters already guessed
- `guessed_word` - Display representation with blanks and revealed letters
- `tries` - Remaining incorrect guess attempts (starts at 6)

### 3. **Core Functions**

#### `initialize_game()`
- Randomly selects a word from the list
- Sets up initial game state
- Returns: word, word_length, guessed_letters, guessed_word, tries

#### `display_hangman(tries)`
- Shows ASCII art representation of hangman
- 7 stages from empty to complete hangman
- Provides visual feedback of progress

#### `display_game_state(guessed_word, guessed_letters, tries)`
- Shows current word progress with blanks
- Lists all guessed letters so far
- Displays remaining attempts

#### `get_valid_guess(guessed_letters)`
- Validates user input (must be single letter)
- Prevents duplicate guesses
- Handles invalid inputs gracefully

#### `process_guess(guess, word, guessed_word, guessed_letters, tries)`
- Checks if guessed letter is in the word
- Updates the guessed_word display if correct
- Decrements tries if incorrect
- Provides appropriate feedback

#### `play_hangman_game()`
- Main game loop
- Orchestrates the flow: display → get input → process → check win/lose
- Handles game completion

#### `main()`
- Allows multiple rounds
- Asks player to continue or exit

### 4. **Game Flow**

```
Start Game
    ↓
Initialize word and game state
    ↓
Display hangman, word progress, remaining tries
    ↓
Get valid letter guess from player
    ↓
Check if letter is in word
    ├─ YES → Update word display, show success message
    └─ NO  → Decrement tries, show failure message
    ↓
Check win condition (all letters revealed)?
    ├─ YES → Display win message with statistics
    └─ NO  → Continue loop
    ↓
Check lose condition (tries = 0)?
    ├─ YES → Display lose message with correct word
    └─ NO  → Continue loop
    ↓
Ask to play again
    ├─ YES → Restart
    └─ NO  → Exit with goodbye message
```

---

## 🎮 Features Implemented

### ✅ Core Features
1. **Random Word Selection** - Picks from 5 predefined words
2. **Letter Guessing** - Players guess one letter at a time
3. **Input Validation** - Ensures valid single letter input, prevents duplicates
4. **Game State Display** - Shows word progress, guessed letters, remaining tries
5. **Hangman Visualization** - ASCII art showing stages of failure
6. **Win/Loss Detection** - Automatically detects game completion
7. **Game Statistics** - Shows number of guesses and incorrect attempts
8. **Multiple Rounds** - Allows continuous play

### ✅ User Experience Enhancements
- Clear formatting with visual separators (=== lines)
- Emoji indicators (✅, ❌, 🎉, 💀) for quick feedback
- Friendly messages and instructions
- Sorted display of guessed letters
- ASCII hangman art progression

---

## 📊 Testing & Validation

### Test Cases Executed

| Test Case | Scenario | Result |
|-----------|----------|--------|
| TC1 | Correct guess | ✅ Letter revealed, feedback shown |
| TC2 | Incorrect guess | ✅ Try counter decremented, feedback shown |
| TC3 | Duplicate guess | ✅ Warning shown, input rejected |
| TC4 | Invalid input (number) | ✅ Validation error, input rejected |
| TC5 | Invalid input (multiple letters) | ✅ Validation error, input rejected |
| TC6 | Win condition (all letters) | ✅ Win message and stats displayed |
| TC7 | Lose condition (6 wrong) | ✅ Lose message and correct word shown |
| TC8 | Play again option | ✅ New game starts or exits correctly |

---

## 📁 Files Delivered

### 1. **hangman_game.py**
Main Python script with complete implementation. Can be run directly from command line:
```bash
python hangman_game.py
```

### 2. **Hangman_Game_CodeAlpha.ipynb**
Google Colab compatible Jupyter notebook with:
- Structured sections with explanations
- Executable code cells
- Test examples for each function
- Full game implementation
- Summary and statistics

### 3. **PROJECT_REPORT.md**
This comprehensive report documenting:
- Project overview and objectives
- Technical implementation details
- Features and capabilities
- Testing results
- User guide and instructions

---

## 🚀 How to Run the Project

### Option 1: Run Python Script Locally
```bash
cd c:\Users\PMLS\Desktop
python hangman_game.py
```

### Option 2: Run Jupyter Notebook
```bash
jupyter notebook Hangman_Game_CodeAlpha.ipynb
```
Then run all cells in order.

### Option 3: Run on Google Colab
1. Upload `Hangman_Game_CodeAlpha.ipynb` to Google Colab
2. Run all cells
3. Follow the prompts to play

---

## 📖 User Guide

### Starting a Game
The program displays:
```
==================================================
WELCOME TO HANGMAN GAME!
==================================================
The word has X letters.
You have 6 incorrect guesses allowed.
==================================================
```

### During Gameplay
- View the hangman ASCII art (updates as you make wrong guesses)
- See word progress with blanks: `_ _ _ _ _`
- See list of already guessed letters
- See remaining attempts counter
- Enter a letter when prompted

### Win Condition
Successfully guess all letters before reaching 6 incorrect guesses:
```
🎉 CONGRATULATIONS! YOU WON! 🎉
The word was: PYTHON
```

### Lose Condition
Reach 6 incorrect guesses:
```
💀 GAME OVER! YOU LOST! 💀
The correct word was: PYTHON
```

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

### Python Fundamentals
✅ Variables and data types (strings, lists, integers)  
✅ Control flow (if-else, while loops)  
✅ Functions and parameters  
✅ List operations and string manipulation  
✅ Input/output operations  
✅ Error handling and validation  

### Programming Best Practices
✅ Code organization with functions  
✅ Clear naming conventions  
✅ Comments and documentation  
✅ Input validation and error handling  
✅ User-friendly interface design  
✅ Game state management  

---

## 📈 Possible Enhancements (Future Versions)

1. **Difficulty Levels** - Easy (8 tries), Normal (6 tries), Hard (4 tries)
2. **Word Categories** - Animals, Countries, Programming Terms, etc.
3. **Hints System** - Provide hints after certain wrong guesses
4. **Scoring System** - Calculate scores based on guesses used
5. **Leaderboard** - Track high scores and statistics
6. **File-based Words** - Load words from external file or API
7. **GUI Interface** - Convert to graphical interface using Tkinter or PyQt
8. **Multiplayer Mode** - Network play or turn-based gameplay
9. **Word Difficulty Rating** - Randomize difficulty within the game
10. **Statistics Tracking** - Save player stats to file

---

## 🏆 Project Summary

This Hangman Game successfully demonstrates:
- ✅ All required Python fundamentals
- ✅ Proper code organization and structure
- ✅ User-friendly interface design
- ✅ Input validation and error handling
- ✅ Game logic and state management
- ✅ Complete documentation

The project is **production-ready** for submission to CodeAlpha and suitable for adding to a professional portfolio for master's scholarship applications.

---

## 📝 Submission Checklist

- [x] Task 1 completed (Hangman Game)
- [x] Code uploaded to GitHub (CodeAlpha_HangmanGame repository)
- [x] Python script created (hangman_game.py)
- [x] Jupyter Notebook created (Google Colab compatible)
- [x] Project report generated (this document)
- [x] All code tested and validated
- [x] User guide and documentation provided
- [ ] Video explanation posted on LinkedIn (Next step)
- [ ] LinkedIn post with GitHub link (Next step)
- [ ] Form submission (Next step)

---

## 📞 Contact & References

**CodeAlpha Information:**
- Website: www.codealpha.tech
- WhatsApp: +91 8052293611
- Email: services@codealpha.tech

**Project Author:**
- Name: Abdul Samad
- Education: BS Mathematics, Sukkur IBA University
- Internship: CodeAlpha Python Programming (Virtual)

---

**Report Generated:** May 31, 2026  
**Project Status:** ✅ COMPLETE  
**Ready for Submission:** YES

---

*This report is part of the CodeAlpha Python Programming Internship completion.*
