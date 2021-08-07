"""Simple Caesar Cipher hacker

Classes:
    CaesarCipherHacker
"""

from simple_ciphers.ciphers import caesar
from .hacker import Hacker


class CaesarCipherHacker(Hacker):
    '''
    Class that allows to decrypt messages encrypted with a Caesar Cipher
    with an unknown key, using brute force
    ...

    Attributes
    ----------
    language : str
        Language code (ISO 639-1) used by the message
        that needs to be decrypted

    Methods
    -------
    brute_force(message):
        Decodes a message using brute force
    '''

    def __brute_fore(self, cipher, message, p=0):
        decrypted_messages = []
        for key in range(1, len(cipher.symbols)):
            candidate = self._get_candidate(
                    cipher,
                    p,
                    message=message,
                    key=key                    
                )

            if candidate:
                decrypted_messages.append(candidate)                

        return decrypted_messages

    def brute_force(self, message, p=0):
        '''
        Tries to decrypt by brute force a message
        encrypted using a Caesar Cipher

        Parameters:
            message (str): message that needs to be decrypted
            p (float):
                the method will return all decrypted
                messages where the probability
                that they belong to the searched
                language is higher than this value.
                0 by default (=the method will return all
                messages decrypted by brute force)

        Returns:
            decrypted_messages (list):
                list of the messages decrypted by brute force
        '''

        decrypted_messages = []
        caesar_cipher = caesar.CaesarCipher()
        decrypted_messages += self.__brute_fore(caesar_cipher, message, p=p)

        for symbols_set in self.symbols_sets:
            caesar_cipher = caesar.CaesarCipher(simple=False, symbols=symbols_set)
            decrypted_messages += self.__brute_fore(caesar_cipher, message, p=p)

        return Hacker._clean_list(decrypted_messages)
