"""Affine Cipher

Classes:
    AffineCipher
"""
from string import printable
from math import gcd
from random import randint
from .cipher import Cipher
from .exceptions import IncorrectCipherKeyError
from ..utils.math import modinv


class AffineCipher(Cipher):
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

    def __init__(self, symbols=printable):
        super().__init__(symbols=symbols)

    def check_keys(self, key_a=0, key_b=0):
        '''
        Check if keys are valid

        Parameters:
            key_a, key_b (int, int): 2 keys

        Returns:
            bool, error:
                bool: True if the keys are valid else False
                error: error to be raised if the keys are not valid
        '''

        error_message = None
        if not isinstance(key_a, int) or not isinstance(key_b, int):
            error_message = 'Keys must be integers'
        elif key_a < 0 or key_b < 0:
            error_message = 'Keys must be greater than 0'
        elif gcd(key_a, len(self.symbols)) != 1:
            error_message = f"""Key A ({key_a}) and the symbol set size ({len(self.symbols)})
            are not relatively prime."""

        if error_message:
            return False, IncorrectCipherKeyError(message=error_message)

        return True, None

    def generate_random_keys(self):
        '''
        Generate 2 valid random keys for the Affine Cipher

        Returns:
            key_a, key_b (int, int): 2 valid keys
        '''
        while True:
            key_a = randint(2, len(self.symbols))
            key_b = randint(2, len(self.symbols))

            valid_keys = self.check_keys(key_a=key_a, key_b=key_b)[0]
            if valid_keys:
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

        self._check_message(message)

        # Check if both keys are valid
        valid_keys, error = self.check_keys(key_a=key_a, key_b=key_b)
        if not valid_keys:
            raise error

        encrypted_message = ''
        for symbol in message:
            if symbol in self.symbols:
                symbolIndex = self.symbols.find(symbol)
                encrypted_message += self.symbols[
                    (symbolIndex * key_a + key_b) % len(self.symbols)
                ]
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

        self._check_message(message)

        # Check if both keys are valid
        valid_keys, error = self.check_keys(key_a, key_b)
        if not valid_keys:
            raise error

        decrypted_message = ''
        inv_key_a = modinv(key_a, len(self.symbols))

        for symbol in message:
            if symbol in self.symbols:
                symbolIndex = self.symbols.find(symbol)
                decrypted_message += self.symbols[
                    (symbolIndex - key_b) * inv_key_a % len(self.symbols)
                ]
            else:
                decrypted_message += symbol
        return decrypted_message
