import itertools
import nltk
from nltk.corpus import words

# Download the words corpus if not already downloaded
nltk.download('words')

# Load the dictionary of English words from nltk
DICTIONARY = set(words.words())

def find_anagrams(word):
    # Create a set to hold all valid anagrams
    anagrams = set()
    
    # Generate all subsets of the input word
    for i in range(2, len(word) + 1):  # Starting from 2 to avoid single-letter words
        subsets = itertools.combinations(word, i)
        for subset in subsets:
            # Generate all permutations of the current subset
            permutations = set([''.join(p) for p in itertools.permutations(subset)])
            # Filter permutations that are in the dictionary
            valid_anagrams = permutations.intersection(DICTIONARY)
            anagrams.update(valid_anagrams)
    
    # Convert set to list and sort first alphabetically, then by length (largest to smallest)
    sorted_anagrams = sorted(anagrams, key=lambda x: (-len(x), x))
    
    return sorted_anagrams

# User input for a 6-letter word
input_word = input("Enter a 6-letter word: ").strip().lower()

# Find and print the anagrams
anagrams = find_anagrams(input_word)
print("Anagrams found:", anagrams)
