"""Simple Caesar Cipher hacker

Classes:
    SimpleTranspositionCipherHacker
"""

import string
from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
from ciphers import transposition

class SimpleTranspositionCipherHacker:
    '''
    Class that allows to decrypt messages encrypted with a Simple Transposition Cipher
    with an unknown key, using brute force
    ...

    Attributes
    ----------
    language : str
        Language code (ISO 639-1) used by the message that needs to be decrypted

    Methods
    -------
    brute_force(message):
        Decodes a message using brute force
    '''

    def __init__(self, language="en"):
        '''
        Create a CaesarCipherHacker instance

        Parameters:
            language (str, optionnal):
                Language code (ISO 639-1) used by the message that needs to be decrypted.
                'en' by default.
        '''

        self.symbols_sets=[
            string.printable,
            string.ascii_letters,
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.ascii_letters + string.whitespace,
            string.ascii_lowercase + string.whitespace,
            string.ascii_uppercase + string.whitespace
        ]
        self.language = language

    def brute_force(self, message, p=0):
        '''
        Corrects an index if out of the symbols list bounds.

        Parameters:
            message (str): message that needs to be decrypted
            p (float):
                the method will return all decrypted messages where the probability
                that they belong to the searched language is higher than this value.
                0 by default (=the method will return all messages decrypted by brute force)

        Returns:
            decrypted_messages (list):
                list of the messages decrypted by brute force
        '''

        decrypted_messages = []
        for symbols_set in self.symbols_sets:
            simple_transposition_cipher = transposition.SimpleTranspositionCipher()
            for key in range(1,len(message)+1):
                decrypted_message = simple_transposition_cipher.decrypt(message=message, key=key)

                if p == 0:
                    decrypted_messages.append(decrypted_message)
                    continue
                try:
                    for detected_lang in detect_langs(decrypted_message):
                        if (detected_lang.lang == self.language.lower() and
                            detected_lang.prob > p):
                            decrypted_messages.append(decrypted_message)
                except LangDetectException:
                    pass

        return decrypted_messages
