from string import ascii_uppercase

frequencies = {
    "en":  {
        "A": 8.12,
        "B": 1.49,
        "C": 2.71,
        "D": 4.32,
        "E": 12.02,
        "F": 2.30,
        "G": 2.03,
        "H": 5.92,
        "I": 7.31,
        "J": 0.10,
        "K": 0.69,
        "L": 3.98,
        "M": 2.61,
        "N": 6.95,
        "O": 7.68,
        "P": 1.82,
        "Q": 0.11,
        "R": 6.02,
        "S": 6.28,
        "T": 9.10,
        "U": 2.88,
        "V": 1.11,
        "W": 2.09,
        "X": 0.17,
        "Y": 2.11,
        "Z": 0.07
    },
    "fr":  {
        "A": 7.11,
        "B": 1.14,
        "C": 3.18,
        "D": 3.67,
        "E": 12.10,
        "F": 1.11,
        "G": 1.23,
        "H": 1.11,
        "I": 6.59,
        "J": 0.34,
        "K": 0.29,
        "L": 4.96,
        "M": 2.62,
        "N": 6.39,
        "O": 5.02,
        "P": 2.49,
        "Q": 0.65,
        "R": 6.07,
        "S": 6.51,
        "T": 5.92,
        "U": 4.49,
        "V": 1.11,
        "W": 0.17,
        "X": 0.38,
        "Y": 0.46,
        "Z": 0.15
    }
}


def letters_frequency(message):
    message = message.upper()
    counts = {}
    for letter in ascii_uppercase:
        counts[letter] = message.count(letter)*100/len(message)
    return counts


def frequency_score(message, lang="en"):
    freq = letters_frequency(message)
    score = 0
    for letter in freq.keys():
        score += abs(freq[letter]-frequencies[lang][letter])

    return 100/score
