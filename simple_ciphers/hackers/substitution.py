"""Simple Substitution Cipher hacker

Classes:
    SimpleSubstitutionCipherHacker
"""

import re
import copy
from string import ascii_lowercase
from simple_ciphers.ciphers import substitution
from .hacker import Hacker
from ..utils.word_patterns import language_patterns, word_pattern


class SimpleSubstitutionCipherHacker(Hacker):
    '''
    Class that allows to decrypt messages encrypted
    with a Simple Substitution Cipher
    with an unknown key, using a dictionary
    ...

    Attributes
    ----------
    language : str
        Language code (ISO 639-1) used by the message
        that needs to be decrypted

    Methods
    -------
    hack(message):
        Runs a dictionary attack to try to decrypt the message
    '''

    def __init__(self, language="en", symbols=ascii_lowercase):
        '''
        Create a SimpleSubstitutionCipherHacker instance

        Parameters:
            language (str, optionnal):
                Language code (ISO 639-1) used by the message
                that needs to be decrypted.
                'en' by default.
            symbols (str, optionnal):
                string made of characters used by the cipher
        '''
        self.symbols = symbols
        self.language = language
        self.word_patterns = language_patterns(language)

    def __empty_mapping(self):
        return {char: [] for char in self.symbols}

    def __get_words_list(self, message):
        return re.compile('[^a-z\s]').sub('', message.lower()).split()

    def __intersect_mappings(self, map_a, map_b):
        intersection = self.__empty_mapping()
        for letter in self.symbols:

            if map_a[letter] == []:
                intersection[letter] = copy.deepcopy(map_b[letter])
            elif map_b[letter] == []:
                intersection[letter] = copy.deepcopy(map_a[letter])
            else:
                intersection[letter] = [
                    val for val in map_a[letter] if val in map_b[letter]
                ]
        self.mapping = intersection
        return self

    def __clean_solved_letters(self):
        loop = True
        while loop:
            loop = False
            solved = [
                self.mapping[c][0] for c in self.symbols
                if len(self.mapping[c]) == 1
            ]

            for c in self.symbols:
                for s in solved:
                    if len(self.mapping[c]) != 1 and s in self.mapping[c]:
                        self.mapping[c].remove(s)
                        loop = len(self.mapping[c]) == 1
        return self

    def hack(self, message):
        '''
        Tries to decrypt by a message
        encrypted using a Simple Substitution Cipher,
        using a dictionary

        Parameters:
            message (str): message that needs to be decrypted

        Returns:
            decrypted_messages (str):
                decrypted message
        '''
        self.mapping = self.__empty_mapping()
        word_list = self.__get_words_list(message.lower())

        for word in word_list:
            pattern = word_pattern(word)
            if pattern not in self.word_patterns:
                continue

            mapping = self.__empty_mapping()

            for candidate in self.word_patterns[pattern]:
                for i in range(len(word)):
                    if candidate[i] not in mapping[word[i]]:
                        mapping[word[i]].append(candidate[i])

            self.__intersect_mappings(self.mapping, mapping)
        self.__clean_solved_letters()

        cipher = substitution.SimpleSubstitutionCipher()
        return cipher.encrypt(message, mapping=self.mapping)
