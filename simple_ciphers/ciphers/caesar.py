"""Simple Caesar Cipher

Classes:
    CaesarCipher
"""
import string
from .exceptions import IncorrectCipherKeyError, IncorrectMessageError

class CaesarCipher:
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

    def __init__(self, symbols=string.printable):
        '''
        Create a CaesarCipher instance

        Parameters:
            symbols (str, optionnal): string made of characters used by the Caesar Cipher
        '''

        if not isinstance(symbols, str):
            raise ValueError

        self.symbols = symbols

    def __handle_index_wraparound(self, index):
        '''
        Private method. Corrects an index if out of the symbols list bounds.

        Parameters:
            index (int): an index

        Returns:
            index (int): corrected index that lies between the symbols list's bounds

        Raises:
            ValueError: if key isn't an integer
        '''
        if not isinstance(index, int):
            raise ValueError

        if index >= len(self.symbols):
            return index - len(self.symbols)
        if index < 0:
            return index + len(self.symbols)
        return index

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
        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        if not isinstance(key, int):
            raise IncorrectCipherKeyError(message="The cipher key has to be an integer")

        if mode is None:
            mode = self.ENCRYPT_MODE

        if mode not in [self.DECRYPT_MODE, self.ENCRYPT_MODE]:
            raise ValueError

        translated = ''
        symbols=self.symbols

        for symbol in message:
            new_symbol = symbol
            if symbol in symbols:
                index = symbols.find(symbol)

                if mode==self.DECRYPT_MODE:
                    new_index = index - key
                elif mode==self.ENCRYPT_MODE:
                    new_index = index + key

                new_symbol = symbols[self.__handle_index_wraparound(new_index)]

            translated += new_symbol

        return translated
