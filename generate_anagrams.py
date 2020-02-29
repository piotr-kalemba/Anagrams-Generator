from collections import Counter
from load_vocab import load_words
import sys


def fit_in(word, name):
    """the boolean function that checks for every character in 'word' parameter if it occurs in the 'name' parameter
    at least as many times as it does in 'word' -
    if this is the case the function returns True, otherwise it returns False """
    name_map = Counter(name)
    word_map = Counter(word)
    for letter in word:
        if letter not in name_map:
            return False
        if name_map[letter] < word_map[letter]:
            return False
    return True


def anagrams(name, words, p, phrase, file, ind, maximum):
    """Recursive function that generates all anagrams of the 'phrase' parameter comprised of words from the list
    'words' and write them to the 'file' parameter. Each anagram of the 'phrase' is given in the order of the
    'words'-list, which excludes generation of permutations of the same anagram."""
    used = list(''.join(phrase[:p]))
    index = 0 if p == 0 else words.index(phrase[p-1])
    if len(used) == len(name):
        file.write(' '.join(phrase[:p]) + '\n')
        index = ind[0] + 1
        ind[0] = index
        "when the number maximum of lines written down in the file is reached, the program terminates"
        if index == maximum:
            sys.exit()
    else:
        left_over = list(name)
        for letter in used:
            left_over.remove(letter)
        for word in words[index:]:
            "the slicing of the list 'words' ensures that the phrases in the generated anagram" \
                             "occur in the order of words-list"
            if fit_in(word, left_over):
                phrase[p] = word
                anagrams(name, words, p+1, phrase, file, ind, maximum)


def gen_anagrams(name, words, file, maximum):
    phrase = [''] * len(name)
    ind = [0]
    anagrams(name, words, 0, phrase, file, ind, maximum)


def main():
    words = set(load_words())
    name = input('Enter your name: ')
    maximum = int(input('Set limit on the number of anagrams to write down in the file: '))
    name = name.replace('-', '')
    name = ''.join(name.split(' ')).lower()
    words = [word for word in words if fit_in(word, name)]
    with open(f'{name}_anagrams.txt', 'w') as file:
        gen_anagrams(name, words, file, maximum)


if __name__ == '__main__':
    main()