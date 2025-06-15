# Wordle Solver

Wordle is a word-guessing game where the player has 6 attempts to guess a hidden 5-letter word. After each guess, feedback is provided indicating which letters are correct and in the correct position, which letters are present but in the wrong position, and which letters do not appear in the word.

## Project Structure

The project consists of the following key files:

- **game.py**  
  Coordinates multiple games of Wordle and handles scoring. You can use this script to run multiple rounds of the game automatically for testing and evaluation.
  
- **wordle.py**  
  Implements the core Wordle game mechanics: choosing a target word, processing guesses, and returning feedback.
  
- **guesser.py**  
  This file contains the guessing algorithm. This is where the Wordle solver logic is implemented. The current version includes the implemented solver that selects guesses based on feedback.
  
- **mymethods.py**  
  Contains helper methods used by `guesser.py` to assist in generating the next guess based on previous feedback.

- **wordlist.yaml / dev_wordlist.yaml / sample_words.yaml**  
  Word lists used by the game. These files contain valid 5-letter words for both possible answers and guesses.

## How to Run

You can run multiple games using the following command:

```bash
python game.py --r 10
```

This will simulate 10 games of Wordle and display performance statistics at the end.

## Project Details

- I was provided with:
  - A template guessing system (`guesser.py`).
  - A fully functional game engine (`wordle.py` and `game.py`).
  - Word lists containing valid words.
  
- My task was focused on implementing and improving the guessing algorithm inside `guesser.py`. The algorithm processes previous feedback (`+`, `-`, or a letter for partial match) and outputs the next best guess.

- **Important:**  
  Do not modify `game.py` or `wordle.py`, as the evaluation depends on these files remaining unchanged.

## Feedback Encoding

The solver uses the following feedback encoding after each guess:

- `'+'` — Correct letter in correct position.
- `'-'` — Letter not present in the word.
- A lowercase letter — Letter present but in the wrong position.

## Example

A typical game cycle:

1. `guesser.py` makes a guess.
2. `wordle.py` checks the guess and returns feedback.
3. `guesser.py` processes feedback and selects the next guess.


## Credits

Assignment developed as part of coursework in the Natural Language Processing course at Bocconi University, academic year 2024-2025.

## Notes

This solver works entirely offline and does not require any external API calls. Ensure that all wordlist files are present in the same directory when running the program.

## Questions & Queries

If you have any questions, thoughts, or comments on this project, please contact me: ioannis.thomopoulos@studbocconi.it
