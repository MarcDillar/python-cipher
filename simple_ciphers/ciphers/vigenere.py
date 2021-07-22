"""Vigenere Cipher

Classes:
    VigenereCipher
"""
import string
from simple_ciphers.ciphers.cipher import Cipher
from .exceptions import IncorrectCipherKeyError, IncorrectMessageError


class VigenereCipher(Cipher):
    '''
    Class handling Vigenere Cipher operations

    ...

    Attributes
    ----------
    symbols : str
        List of symbols used by the V cipher

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

    def __init__(self, simple=False, symbols=string.printable):
        '''
        Create a VigenereCipher instance

        Parameters:
            simple (bool, optionnal):
                usage of the cipher's simple mode.
                simple mode preserves the message's characters case
                and only encrypts letters.
                default: False
            symbols (str, optionnal):
                string made of characters used by the VigenereCipher Cipher.
                default: string.printable
        '''
        super().__init__(simple=simple, symbols=symbols)

        self.symbols = "".join(
            sorted(
                list(self.symbols),
                key=lambda x: ord(x)
            )
        )

    def __char_key_to_int(self, char):
        if char in self.symbols:
            return self.symbols.find(char)
        return 0

    def encrypt(self, message, key):
        '''
        Encrypts a message using the Vigenere cipher.

        Parameters:
            message (str): message to encrypt
            key (str): key of the Vigenere cipher

        Returns:
            message (str): encrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
        '''

        return self.cipher(message, key, mode=self.ENCRYPT_MODE)

    def decrypt(self, message, key):
        '''
        Decrypts a message using the Vigenere cipher.

        Parameters:
            message (str): message to decrypt
            key (str): key of the Vigenere cipher

        Returns:
            message (str): decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
        '''

        return self.cipher(message, key, mode=self.DECRYPT_MODE)

    def cipher(self, message, key, mode=None):
        '''
        Encrypts or decrypts a message using the Vigenere cipher.

        Parameters:
            message (str): message to decrypt
            key (str): key of the Vigenere cipher
            mode (string, optionnal): encrypt or decrypt. Default: encrypt

        Returns:
            message (str): encrypted or decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key is not a string or is empty
            ValueError: if mode isn't correct
        '''
        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError

        if not isinstance(key, str) or len(key) == 0:
            raise IncorrectCipherKeyError(
                "The key needs to be a non empty string"
            )

        if mode is None:
            mode = self.ENCRYPT_MODE

        if mode not in [self.DECRYPT_MODE, self.ENCRYPT_MODE]:
            raise ValueError

        translated, i = '', 0

        for symbol in message:
            key_int = self.__char_key_to_int(key[i])
            new_symbol = symbol
            if symbol in self.symbols:
                index = self.symbols.find(symbol)

                if mode == self.DECRYPT_MODE:
                    new_index = index - key_int
                elif mode == self.ENCRYPT_MODE:
                    new_index = index + key_int

                new_symbol = self.symbols[
                    self._handle_index_wraparound(new_index)
                ]

                i = 0 if i == len(key)-1 else i+1

            if self.simple:
                if symbol.islower():
                    new_symbol = new_symbol.lower()
                else:
                    new_symbol = new_symbol.upper()
            translated += new_symbol

        return translated
