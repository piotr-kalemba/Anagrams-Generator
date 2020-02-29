from collections import Counter
from load_vocab import load_words


def fit_in(word, name):
    name_map = Counter(name)
    word_map = Counter(word)
    for letter in word:
        if letter not in name_map:
            return False
        if name_map[letter] < word_map[letter]:
            return False
    return True


def anagrams(name, words, p, phrase, file):
    used = list(''.join(phrase[:p]))
    index = 0 if p == 0 else words.index(phrase[p-1])
    if len(used) == len(name):
        file.write(' '.join(phrase[:p]) + '\n')
    else:
        left_over = list(name)
        for letter in used:
            left_over.remove(letter)
        for word in words[index:]:
            if fit_in(word, left_over):
                phrase[p] = word
                anagrams(name, words, p+1, phrase, file)


def gen_anagrams(name, words, file):
    phrase = [''] * len(name)
    anagrams(name, words, 0, phrase, file)


def main():
    words = set(load_words())
    name = input('Enter your name: ')
    name = name.replace('-', '')
    name = ''.join(name.split(' ')).lower()
    words = [word for word in words if fit_in(word, name)]
    with open(f'{name}_anagrams.txt', 'w') as file:
        gen_anagrams(name, words, file)


if __name__ == '__main__':
    main()