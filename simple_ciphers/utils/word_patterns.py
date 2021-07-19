"""
Word patterns util functions

Functions:
    word_pattern
    language_patterns
"""

from .dictionary import Dictionary


def word_pattern(word):
    '''
        Returns the pattern of a given word

        Parameters:
            word (str)

        Returns:
            word pattern (str):
                String representing the letters distribution in a word.
                Example:
                    - word_pattern("cat") =>
                        "0.1.2" because all letters are different
                    - word_pattern("motorcycle") =>
                        "0.1.2.1.3.4.5.4.6.7"
    '''
    word = word.upper()
    i, letterNums, pattern = 0, {}, []

    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(i)
            i += 1
        pattern.append(letterNums[letter])
    return ".".join(pattern)


def language_patterns(lang="en"):
    '''
        Returns thes pattern of all the words of a given language

        Parameters:
            lang (str, optionnal):
                2-letter language code. "en" by default.
                The list of words is read from the corresponding
                file in the "words_list" folder.

        Returns:
            patterns (list)
    '''
    patterns = {}

    words = Dictionary(lang).words

    for word in words:
        pattern = word_pattern(word)

        if pattern not in patterns:
            patterns[pattern] = [word]
        else:
            patterns[pattern].append(word)

    return patterns
