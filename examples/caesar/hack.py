"""
Example of message brute force decryption
of a message encrypted with a Caesar cipher
"""

from simple_ciphers.ciphers.caesar import CaesarCipher
from simple_ciphers.hackers.caesar import CaesarCipherHacker

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
KEY = 10

caesar_cipher = CaesarCipher()
caesar_hacker = CaesarCipherHacker()

encrypted_message = caesar_cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
decrypted_messages = caesar_hacker.brute_force(encrypted_message, p=0.95)
print('\n'.join(decrypted_messages))
