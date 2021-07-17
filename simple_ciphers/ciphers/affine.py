"""Affine Cipher

Classes:
    AffineCipher
"""
import string
import math
from .exceptions import IncorrectCipherKeyError, IncorrectMessageError
from ..utils.math import modinv


class AffineCipher:
    '''
    Class handling basic Affine Cipher operations

    ...

    Attributes
    ----------
    symbols : str
        List of symbols used by the cipher

    Methods
    -------
    encrypt(message, key):
        Encrypts a message

    decrypt(message, key):
        Decrypts a message
    '''

    def __init__(self, symbols=string.printable):
        '''
        Create a CaesarCipher instance

        Parameters:
            symbols (str, optionnal): string made of characters used by the Caesar Cipher
        '''

        if not isinstance(symbols, str):
            raise ValueError

        self.symbols = symbols

    def __check_keys(self, key_a, key_b):
        if not isinstance(key_a, int) or not isinstance(key_b, int):
            raise IncorrectCipherKeyError('Keys must be integers')
        if key_a < 0 or key_b < 0:
            raise IncorrectCipherKeyError('Keys must be greater than 0')
        if math.gcd(key_a, len(self.symbols)) != 1:
            raise IncorrectCipherKeyError(f'Key A ({key_a}) and the symbol set size ({len(self.symbols)}) are not relatively prime.')


    def encrypt(self, message, key_a, key_b):
        '''
        Encrypts a message using the Affine cipher.

        Parameters:
            message (str): message to encrypt
            key_a, key_b (int, int): keys of the Affine cipher

        Returns:
            encrypted_message (str): encrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if keys are not valid
        '''

        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        # Check if both keys are valid
        self.__check_keys(key_a, key_b)
        encrypted_message = ''
        for symbol in message:
            if symbol in self.symbols:
                symbolIndex = self.symbols.find(symbol)
                encrypted_message += self.symbols[(symbolIndex * key_a + key_b) % len(self.symbols)]
            else:
                encrypted_message += symbol
        return encrypted_message

    def decrypt(self, message, key_a, key_b):
        '''
        Decrypts a message using the Affine cipher.

        Parameters:
            message (str): message to encrypt
            key_a, key_b (int, int): keys of the Affine cipher

        Returns:
            decrypted_message (str): decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if keys are not valid
        '''

        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        # Check if both keys are valid
        self.__check_keys(key_a, key_b)

        decrypted_message = ''
        inv_key_a = modinv(key_a, len(self.symbols))

        for symbol in message:
            if symbol in self.symbols:
                symbolIndex = self.symbols.find(symbol)
                decrypted_message += self.symbols[(symbolIndex - key_b) * inv_key_a % len(self.symbols)]
            else:
                decrypted_message += symbol
        return decrypted_message
