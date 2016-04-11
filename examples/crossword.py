# crossword.py

import re
from collections import Counter

def find_crossword_candidates(wordlist, entry):
    pattern = '^' + entry.replace('_', '.') + '$'
    return {word for word in wordlist if len(entry) == len(word) and re.search(pattern, word)}

def find_jumble_candidates(wordlist, entry):
    sorted_entry = sorted(entry)

##scrabble_points_text = '''
##1: E, A, I, O, N, R, T, L, S, U
##2: D, G
##3: B, C, M, P
##4: F, H, V, W, Y
##5: K
##8: J, X
##10: Q, Z
##'''
##scrabble_points = {}
##for line in scrabble_points_text.strip().splitlines():
##    point_value, tiles = line.split(':')
##    point_value = int(point_value)
##    for tile in tiles.split(','):
##        tile = tile.strip().lower()
##        scrabble_points[tile] = point_value

scrabble_points = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2,
                   'g': 2, 'f': 4, 'i': 1, 'h': 4, 'k': 5,
                   'j': 8, 'm': 3, 'l': 1, 'o': 1, 'n': 1,
                   'q': 10, 'p': 3, 's': 1, 'r': 1, 'u': 1,
                   't': 1, 'w': 4, 'v': 4, 'y': 4, 'x': 8, 'z': 10}

def scrabble_score(word):
    return sum([scrabble_points[c] for c in word])

def find_scrabble_candidates(wordlist, entry):
    hist = Counter(entry)
    pattern = '^' + ''.join([(letter + '?' if count == 1 else letter + '{,%d}' % count) for letter, count in sorted(hist.items())] ) + '$'
    candidates = {word for word in wordlist if re.search(pattern, ''.join(sorted(word)))}
    return candidates

def load_wordlist(filename = 'notes/words.txt'):
    with open(filename) as f:
        wordlist = { line.strip().lower() for line in f if line.strip() }
    return wordlist

if __name__ == '__main__':
    wordlist = load_wordlist()
    
    print find_crossword_candidates(wordlist, 'f__d')
    print find_jumble_candidates(wordlist, 'nophyt')
    print find_jumble_candidates(wordlist, 'fde')

    print find_scrabble_candidates(wordlist, 'phtyons')
    print max(find_scrabble_candidates(wordlist, 'phytons'), key=scrabble_score)

    
