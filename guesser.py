from random import choice
import yaml
from rich.console import Console
import mymethods


class Guesser:
    '''
        INSTRUCTIONS: This function should return your next guess. 
        Currently it picks a random word from wordlist and returns that.
        You will need to parse the output from Wordle:
        - If your guess contains that character in a different position, Wordle will return a '-' in that position.
        - If your guess does not contain thta character at all, Wordle will return a '+' in that position.
        - If you guesses the character placement correctly, Wordle will return the character. 

        You CANNOT just get the word from the Wordle class, obviously :)
    '''
    def __init__(self, manual):
        self.word_list = yaml.load(open('dev_wordlist.yaml'), Loader=yaml.FullLoader)
        self._manual = manual
        self.console = Console()
        self._tried = []
        self.words_left = set(self.word_list)       #ADDED 
        self._precomputed = {}                      #ADDED


    def restart_game(self):
        self._tried = []
        self.words_left = set(self.word_list)       #ADDED
    
    
    def get_guess(self, result):
        
        if self._tried and result and len(result) == 5:
            prev_guess = self._tried[-1]
            self.words_left = mymethods.eliminate_words(prev_guess, result, self.words_left)
        
        if not self._tried:
            guess = mymethods.starter_word(self.words_left)
            self._tried.append(guess)
            return guess
        
        if self._manual=='manual':
            return self.console.input('Your guess:\n')
        else:
            guess = mymethods.best_guess(self.words_left, self._precomputed)
            self._tried.append(guess)
            self.console.print(guess)
            return guess

