"""Simple Caesar Cipher

Classes:
    CaesarCipher
"""
from string import ascii_lowercase
from random import sample
from .cipher import Cipher
from .exceptions import IncorrectCipherKeyError


class SimpleSubstitutionCipher(Cipher):
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
    PLACEHOLDER = "_"

    def __init__(self, simple=True, symbols=ascii_lowercase):
        super().__init__(simple=simple)
        self.symbols = symbols

    def check_key(self, key):
        if not isinstance(key, str):
            raise IncorrectCipherKeyError(
                """The key must be a string containing all letters
                of the cipher's symbols set once (case insensitive)""")

        
        key_list = list(key.lower())
        key_list.sort()

        if self.simple:

            symbols_list = list(set(self.symbols.lower()))
            symbols_list.sort()
            
        else:
            symbols_list = list(set(self.symbols))
            symbols_list.sort()

        if key_list == symbols_list:
                return True

        raise IncorrectCipherKeyError(
            """The key must be a string containing all letters
            of the cipher's symbols set once (case insensitive)""")

    def __get_mapping(self, key, mapping):
        if key and not mapping:
            self.check_key(key)
            keys = self.symbols
            values = key
        elif mapping:
            keys = "".join(list(mapping.keys()))
            values = "".join([
                mapping[key][0] if len(mapping[key]) == 1 else self.PLACEHOLDER
                for key in keys
            ])
        return keys, values

    def generate_random_key(self):
        '''
        Generate a random valid key

        Returns:
            key (str): a valid key
        '''
        return ''.join(sample(self.symbols, len(self.symbols)))

    def encrypt(self, message, key=None, mapping=None):
        '''
        Encrypts a message using the Simple Substitution cipher.

        Parameters:
            message (str): message to encrypt
            key (str, optionnal): key of the cipher
            mapping (dict, optionnal):
                dictionary where keys are the source characters
                and values are the destination characters

        Returns:
            message (str): encrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        return self.cipher(
            message,
            key=key,
            mapping=mapping,
            mode=self.ENCRYPT_MODE
        )

    def decrypt(self, message, key=None, mapping=None):
        '''
        Decrypts a message using the Simple Substitution cipher.

        Parameters:
            message (str): message to decrypt
            key (str, optionnal): key of the cipher
            mapping (dict, optionnal):
                dictionary where keys are the source characters
                and values are the destination characters

        Returns:
            message (str): decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError: if key isn't an integer
        '''

        return self.cipher(
            message,
            key=key,
            mapping=mapping,
            mode=self.DECRYPT_MODE
        )

    def cipher(self, message, key=None, mapping=None, mode=ENCRYPT_MODE):
        '''
        Encrypts or decrypts a message using the Simple Substitution cipher.

        Parameters:
            message (str): message to decrypt
            key (str, optionnal): key of the cipher
            mapping (dict, optionnal):
                dictionary where keys are the source characters
                and values are the destination characters
            mode (string, optionnal): encrypt or decrypt. Default: encrypt

        Returns:
            result (str): encrypted or decrypted message

        Raises:
            IncorrectMessageError: if message is not a string or is empty
            IncorrectCipherKeyError:
                if the key isn't a string containing
                all letters cipher's symbols set once
            ValueError: if mode isn't correct
        '''

        self._check_message(message)

        if mode not in [self.DECRYPT_MODE, self.ENCRYPT_MODE]:
            raise ValueError

        keys, values = self.__get_mapping(key, mapping)

        if mode == self.ENCRYPT_MODE:
            source_symbols, dest_symbols = keys, values
        else:
            source_symbols, dest_symbols = values, keys

        if self.simple:
            source_symbols = source_symbols.lower()

        result = ""
        for symbol in message:
            symbol_to_search = symbol
            if self.simple:
                symbol_to_search = symbol_to_search.lower()

            if symbol_to_search in source_symbols:
                new_char = dest_symbols[
                    source_symbols.find(symbol_to_search)
                ]

                if self.simple:
                    if symbol.isupper():
                        result += new_char.upper()
                    else:
                        result += new_char.lower()
                else:
                    result += new_char
            else:
                result += symbol

        return result
