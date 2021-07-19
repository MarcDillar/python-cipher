"""Simple Caesar Cipher hacker

Classes:
    SimpleTranspositionCipherHacker
"""
from simple_ciphers.ciphers import transposition
from .hacker import Hacker


class SimpleTranspositionCipherHacker(Hacker):
    '''
    Class that allows to decrypt messages encrypted with
    a Simple Transposition Cipher
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

    def brute_force(self, message, p=0):
        '''
        Tries to decrypt by brute force a message
        encrypted using a Simple Transposition Cipher

        Parameters:
            message (str): message that needs to be decrypted
            p (float):
                the method will return all decrypted
                messages where the probability
                that they belong to the searched
                language is higher than this value.
                0 by default (=the method will return
                all messages decrypted by brute force)

        Returns:
            decrypted_messages (list):
                list of the messages decrypted by brute force
        '''

        decrypted_messages = []
        cipher = transposition.SimpleTranspositionCipher()
        for key in range(1, len(message)+1):
            decrypted_message = cipher.decrypt(message, key)
            lang, prob = self.lang_identifier.classify(decrypted_message)

            if lang == self.language and prob >= p:
                decrypted_messages.append({
                    "text": decrypted_message,
                    "p": prob
                })

        decrypted_messages = sorted(
            decrypted_messages,
            key=lambda x: x["p"],
            reverse=True
        )

        return [message["text"] for message in decrypted_messages]
