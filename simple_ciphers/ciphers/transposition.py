"""Simple Transposition Cipher

Classes:
    SimpleTranspositionCipher
"""

import math
from .exceptions import IncorrectCipherKeyError, IncorrectMessageError

class SimpleTranspositionCipher:
    '''
    Class handling basic Caesar Cipher operations

    ...

    Methods
    -------
    encrypt(message, key):
        Encrypts a message

    derypt(message, key):
        Decrypts a message

    '''

    def encrypt(self, message, key):
        '''
        Encrypts a message using the Transposition cipher.

        Parameters:
            message (str): message to encrypt
            key (int): key of the Transposition cipher

        Returns:
            message (str): encrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        if not isinstance(key, int):
            raise IncorrectCipherKeyError (message="The cipher key has to be an integer")

        cipher_table = [''] * key

        for i in range(key):
            j = i
            while j < len(message):
                cipher_table[i] += message[j]
                j += key

        return ''.join(cipher_table)


    def decrypt(self, message, key):
        '''
        Decrypts a message using the Simple Transposition cipher.

        Parameters:
            message (str): message to decrypt
            key (int): key of the Simple Transposition cipher

        Returns:
            message (str): decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''
        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        if not isinstance(key, int):
            raise IncorrectCipherKeyError(message="The cipher key has to be an integer")

        col_count = math.ceil(len(message) / key)
        rows_count = key
        unused_cells = (col_count*rows_count) - len(message)

        decryption_table = [''] * col_count
        i, j = 0, 0

        for char in message:
            decryption_table[i] += char
            i += 1

            if i == col_count or(
                i == col_count-1 and
                j >= rows_count-unused_cells):
                i, j = 0, j+1

        return ''.join(decryption_table)
