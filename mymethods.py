from collections import Counter
import math
import numpy as np

def eliminate_words(guess, result, words_left):
    return [word for word in words_left if get_matches(word, guess) == result]

def best_guess(words_left, precomputed):
    best_word, best_entropy = None, -1.0
    for word in words_left:
        entropy = 0
        matches = Counter(stored_results(wordle, word, precomputed) for wordle in words_left)
        total = sum(matches.values())
        for count in matches.values():
            p = count / total
            entropy -= p * math.log2(p)
        if entropy > best_entropy:
            best_entropy = entropy
            best_word = word
    return best_word

def get_matches(word, guess):
    counts = Counter(word)   
    results = []
#FINDS THE GREENS
    for i, letter in enumerate(guess):
        if guess[i] == word[i]:    
            results.append(guess[i])
            counts[guess[i]] -= 1
        else:                      
            results.append('+')
#FINDS THE YELLOWS
    for i, letter in enumerate(guess):    
        if guess[i] != word[i] and guess[i] in word:    
            if counts[guess[i]] > 0:
                counts[guess[i]] -= 1
                results[i] = '-'
    return ''.join(results)

def stored_results(wordle, guess, precomputed):
        if (wordle, guess) in precomputed:
            return precomputed[(wordle, guess)]
        result = get_matches(wordle, guess)
        precomputed[(wordle, guess)] = result
        return result

def starter_word(word_list):

    pos_freq = [Counter() for _ in range(5)]
    for word in word_list:
        for pos, letter in enumerate(word):
            pos_freq[pos][letter] += 1

    best_word = None
    best_score = -1

    for word in word_list:
        score = 0
        seen = set()
        for pos, letter in enumerate(word):
            score += pos_freq[pos][letter]
            if letter in seen:
                score *= 0.9  #reduce score if duplicate letter found
            else:
                seen.add(letter)
        if score > best_score:
            best_score = score
            best_word = word
    return best_word

# 100.00%,2.9500,0.70 -- 0.9
# 100.00%,2.9740,0.75 -- 0.8
# 100.00%,2.9720,0.74 -- 0.7
# 100.00%,2.9660,0.74 -- 0.4
# 100.00%,3.1120,0.82 -- 1.0


 

