"""Vigenere Cipher hacker

Classes:
    VigenereCipherHacker
"""

import itertools
from simple_ciphers.ciphers.vigenere import VigenereCipher
from .hacker import Hacker
from ..utils.word_patterns import find_repeated_sequences_spacings
from ..utils.math import factors
from ..utils.lists import most_common
from ..utils.frequency import frequency_score
from ..utils.strings import remove_non_letters


class VigenereCipherHacker(Hacker):
    '''
    Class that tries to decrypt messages encrypted
    with a Vigenere Cipher
    with an unknown key.
    ...

    Attributes
    ----------
    language (str):
        Language code (ISO 639-1) used by the message
        that needs to be decrypted.
        Default: en

    Methods
    -------
    hack(message):
        Try to decrypt the message without knowing the encryption key
    '''

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUM_MOST_FREQ_LETTERS = 6

    def get_possible_key_lengths(self, message):
        """
        Using the Kasiski examination method
        """
        message = remove_non_letters(message).upper()

        sequence_spacings = find_repeated_sequences_spacings(message)
        possible_key_lengths = []

        for spacings in sequence_spacings.values():
            for spacing in spacings:
                possible_key_lengths += factors(spacing)

        return possible_key_lengths

    def get_possible_keys(self, message, key_length):

        possible_keys = []

        cipher = VigenereCipher()

        all_frequency_scores = []
        for n in range(0, key_length):
            substring = message[n::key_length]

            frequency_scores = []
            for key in self.LETTERS:
                decryptedText = cipher.decrypt(substring, key)
                frequency_scores.append(
                    (key, frequency_score(decryptedText, lang=self.language))
                )
            frequency_scores.sort(key=lambda x: x[1], reverse=True)

            all_frequency_scores.append(
                frequency_scores[:self.NUM_MOST_FREQ_LETTERS]
            )

        # loop through all possible keys
        # among the most likely possibilities
        iterator = itertools.product(
            range(self.NUM_MOST_FREQ_LETTERS),
            repeat=key_length
        )

        for indexes in iterator:

            key = ''
            for i in range(key_length):
                key += all_frequency_scores[i][indexes[i]][0]

            possible_keys.append(key)

        return possible_keys

    def hack(self, message, simple=True, p=0.99):
        '''
        Tries to decrypt by a message
        encrypted using a Vigenere Cipher

        Parameters:
            message (str): message that needs to be decrypted

        Returns:
            decrypted_messages (str):
                decrypted message
        '''
        decrypted_messages = []
        cipher = VigenereCipher()

        message_to_analyze = message
        if simple:
            message_to_analyze = remove_non_letters(message_to_analyze).upper()

        possible_key_lengths = self.get_possible_key_lengths(
            message_to_analyze
        )

        frequent_keys_lengths = most_common(possible_key_lengths, n=2)

        possible_keys = []
        for key_length in frequent_keys_lengths:
            possible_keys += self.get_possible_keys(
                message_to_analyze,
                key_length
            )

        for key in possible_keys:
            candidate = self._get_candidate(
                cipher,
                p,
                message=message,
                key=key
            )
            if candidate:
                decrypted_messages.append(candidate)

        return Hacker._clean_list(decrypted_messages)
