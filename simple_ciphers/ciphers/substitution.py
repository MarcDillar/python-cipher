"""Simple Caesar Cipher

Classes:
    CaesarCipher
"""
import string
from .exceptions import IncorrectCipherKeyError, IncorrectMessageError

class SimpleSubstitutionCipher:
    '''
    Class handling simple Substitution Cipher operations
    ...


    Methods
    -------
    encrypt(message, key):
        Encrypts a message

    decrypt(message, key):
        Decrypts a message
    '''

    ENCRYPT_MODE = "encrypt"
    DECRYPT_MODE = "decrypt"

    def __init__(self, symbols=string.ascii_lowercase):
        '''
        Create a SimpleSubstitutionCipher instance

        Parameters:
            symbols (str, optionnal): string made of characters handled by the Substitution Cipher
        '''

        if not isinstance(symbols, str):
            raise ValueError

        self.symbols = symbols

    def __check_key(self, key):
        key_list = list(key.lower())
        key_list.sort()
        symbols_list = list(self.symbols.lower())
        symbols_list.sort()

        return "".join(key_list) == "".join(symbols_list)

    def encrypt(self, message, key):
        '''
        Encrypts a message using the Simple Substitution cipher.

        Parameters:
            message (str): message to encrypt
            key (str): key of the cipher

        Returns:
            message (str): encrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        return self.cipher(message, key, mode=self.ENCRYPT_MODE)

    def decrypt(self, message, key):
        '''
        Decrypts a message using the Simple Substitution cipher.

        Parameters:
            message (str): message to decrypt
            key (str): key of the cipher

        Returns:
            message (str): decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        return self.cipher(message, key, mode=self.DECRYPT_MODE)

    def cipher(self, message, key, mode=None):
        '''
        Encrypts or decrypts a message using the Simple Substitution cipher.

        Parameters:
            message (str): message to decrypt
            key (str): key of the cipher
            mode (string, optionnal): encrypt or decrypt. Default: encrypt

        Returns:
            result (str): encrypted or decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if the key isn't a string containing all letters cipher's symbols set once
            ValueError: if mode isn't correct
        '''
        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        if not self.__check_key(key):
            raise IncorrectCipherKeyError(message="The key should be a string containing all letters of the cipher's symbols set once")

        if mode is None:
            mode = self.ENCRYPT_MODE

        if mode not in [self.DECRYPT_MODE, self.ENCRYPT_MODE]:
            raise ValueError

        encrypt = mode == self.ENCRYPT_MODE

        source_symbols, dest_symbols = (self.symbols, key) if encrypt else (key, self.symbols)

        result = ""
        for symbol in message:
            if symbol.lower() in source_symbols.lower():
                new_char = dest_symbols[source_symbols.lower().find(symbol.lower())]
                result += new_char.upper() if symbol.isupper() else new_char.lower()
            else:
                result += symbol

        return result
