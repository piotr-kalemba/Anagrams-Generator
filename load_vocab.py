
def load_words():
    words = []
    with open('corncob_lowercase.txt') as file:
        for line in file:
            words.append(line.strip().lower())
    words = [word for word in words if len(word) > 1]
    words.append('a')
    words.append('i')
    return words
