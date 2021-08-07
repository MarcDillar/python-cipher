"""Simple Caesar Cipher

Classes:
    CaesarCipher
"""
import string
from .cipher import Cipher


class CaesarCipher(Cipher):
    '''
    Class handling basic Caesar Cipher operations

    ...

    Attributes
    ----------
    symbols : str
        List of symbols used by the Caesar cipher

    Methods
    -------
    encrypt(message, key):
        Encrypts a message

    decrypt(message, key):
        Decrypts a message

    cipher(message, key, mode=None)
        Encrypts of decrypts a message depending on the selected mode
    '''

    ENCRYPT_MODE = "encrypt"
    DECRYPT_MODE = "decrypt"

    def __init__(self, simple=True, symbols=string.printable):
        super().__init__(simple=simple, symbols=symbols)

    def encrypt(self, message, key):
        '''
        Encrypts a message using the Caesar cipher.

        Parameters:
            message (str): message to encrypt
            key (int): key of the Caesar cipher

        Returns:
            message (str): encrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        return self.cipher(message, key, mode=self.ENCRYPT_MODE)

    def decrypt(self, message, key):
        '''
        Decrypts a message using the Caesar cipher.

        Parameters:
            message (str): message to decrypt
            key (int): key of the Caesar cipher

        Returns:
            message (str): decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        return self.cipher(message, key, mode=self.DECRYPT_MODE)

    def cipher(self, message, key, mode=None):
        '''
        Encrypts or decrypts a message using the Caesar cipher.

        Parameters:
            message (str): message to decrypt
            key (int): key of the Caesar cipher
            mode (string, optionnal): encrypt or decrypt. Default: encrypt

        Returns:
            message (str): encrypted or decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
            ValueError: if mode isn't correct
        '''

        self._check_message(message)
        self.check_key(key)

        if mode is None:
            mode = self.ENCRYPT_MODE

        if mode not in [self.DECRYPT_MODE, self.ENCRYPT_MODE]:
            raise ValueError

        translated = ''
        symbols = self.symbols

        for symbol in message:
            new_symbol = symbol
            if symbol in symbols:
                index = symbols.find(symbol)

                if mode == self.DECRYPT_MODE:
                    new_index = index - key
                elif mode == self.ENCRYPT_MODE:
                    new_index = index + key

                new_symbol = symbols[self._handle_index_wraparound(new_index)]
            if self.simple:
                if symbol.islower():
                    new_symbol = new_symbol.lower()
                else:
                    new_symbol = new_symbol.upper()
            translated += new_symbol

        return translated
