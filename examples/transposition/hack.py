"""
Example of message brute force decryption
of a message encrypted with a simple transposition cipher
"""

from simple_ciphers.ciphers import transposition as transposition_cipher
from simple_ciphers.hackers import transposition as transposition_hacker

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted."
KEY = 20

cipher = transposition_cipher.SimpleTranspositionCipher()
hacker = transposition_hacker.SimpleTranspositionCipherHacker()

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
decrypted_messages = hacker.brute_force(encrypted_message, p=0.999)
print('\n'.join(decrypted_messages))
