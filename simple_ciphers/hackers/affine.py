"""Simple Affine Cipher hacker

Classes:
    AffineCipherHacker
"""

import string
from langdetect import detect_langs
from langdetect.lang_detect_exception import LangDetectException
from simple_ciphers.ciphers import affine

class AffineCipherHacker:
    '''
    Class that allows to decrypt messages encrypted with an Affine Cipher
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
        Create a AffineCipherHacker instance

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
        Tries to decrypt by brute force a message encrypted using an Affine Cipher

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
            affine_cipher = affine.AffineCipher(symbols=symbols_set)
            for key_a in range(2, len(symbols_set)):
                
                valid_keys = affine_cipher.check_keys(key_a=key_a)[0]
                if not valid_keys:
                    continue

                for key_b in range(2, len(symbols_set)):
                    decrypted_message = affine_cipher.decrypt(message, key_a, key_b)
                    try:
                        for detected_lang in detect_langs(decrypted_message):
                            
                                if (detected_lang.lang == self.language.lower()
                                    and detected_lang.prob > p):
                                    decrypted_messages.append({
                                        "text": decrypted_message,
                                        "p": detected_lang.prob
                                    })
                    except LangDetectException:
                        pass

        return [message["text"] for message in sorted(decrypted_messages, key=lambda x: x["p"], reverse=True)]
