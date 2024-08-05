import itertools
import nltk
from nltk.corpus import words

nltk.download('words')

DICTIONARY = set(words.words())

def find_anagrams(word):
    anagrams = set()
    
    for i in range(3, len(word) + 1):  
        subsets = itertools.combinations(word, i)
        for subset in subsets:
            permutations = set([''.join(p) for p in itertools.permutations(subset)])
            valid_anagrams = permutations.intersection(DICTIONARY)
            anagrams.update(valid_anagrams)
    
    sorted_anagrams = sorted(anagrams, key=lambda x: (-len(x), x))
    
    return sorted_anagrams

input_word = input("Enter a 6-letter word: ").strip().lower()

anagrams = find_anagrams(input_word)
print("Anagrams found:", anagrams)
