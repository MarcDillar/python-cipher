"""Parent Cipher class

Classes:
    Cipher
"""
import string
from .exceptions import IncorrectMessageError, IncorrectCipherKeyError


class Cipher:
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
        '''
        Create a Cipher instance

        Parameters:
            simple (bool, optionnal):
                usage of the cipher's simple mode.
                simple mode preserves the message's characters case
                and only encrypts letters.
                default: True
            symbols (str, optionnal):
                string made of characters used by the Caesar Cipher.
                Is ignored if simple mode is activated.
                default: string.printable
        '''
        self.simple = simple
        if simple:
            self.symbols = string.ascii_letters
        else:
            if not isinstance(symbols, str):
                raise ValueError

            self.symbols = symbols

    def _handle_index_wraparound(self, index):
        '''
        Proteted method. Corrects an index if out of the symbols list bounds.

        Parameters:
            index (int): an index

        Returns:
            index (int):
                corrected index that lies between the symbols list's bounds

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

    def _check_message(self, message):
        if not isinstance(message, str) or len(message) == 0:
            raise IncorrectMessageError
        return True

    def check_key(self, key):
        if not isinstance(key, int):
            raise IncorrectCipherKeyError(
                "The cipher key must be an integer"
            )
        return True
