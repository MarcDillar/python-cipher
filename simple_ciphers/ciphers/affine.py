"""Affine Cipher

Classes:
    AffineCipher
"""
import string
from math import gcd
from random import randint
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
        '''
        Private method. Check if keys are valid

        Parameters:
            key_a, key_b (int, int): 2 keys

        Returns:
            bool: True if the keys are valid

        Raises:
            IncorrectCipherKeyError if the keys are not valid
        '''

        error_message = None
        if not isinstance(key_a, int) or not isinstance(key_b, int):
            error_message = 'Keys must be integers'
        elif key_a < 0 or key_b < 0:
            error_message = 'Keys must be greater than 0'
        elif gcd(key_a, len(self.symbols)) != 1:
            error_message = f'Key A ({key_a}) and the symbol set size ({len(self.symbols)}) are not relatively prime.'

        if error_message:
            raise IncorrectCipherKeyError(message=error_message)

        return True

    def generate_random_keys(self):
        '''
        Generate 2 valid random keys for the Affine Cipher

        Returns:
            key_a, key_b (int, int): 2 valid keys
        '''
        valid_keys = False
        while not valid_keys:
            key_a = randint(2, len(self.symbols))
            key_b = randint(2, len(self.symbols))
            try:
                self.__check_keys(key_a, key_b)
                valid_keys = True
            except IncorrectCipherKeyError:
                valid_keys = False
        
        return key_a, key_b            

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
