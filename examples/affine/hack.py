"""
Example of message brute force decryption
of a message encrypted with an Affine cipher
"""

from simple_ciphers.ciphers.affine import AffineCipher
from simple_ciphers.hackers.affine import AffineCipherHacker

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"

cipher = AffineCipher()
hacker = AffineCipherHacker()


encrypted_message = cipher.encrypt(MESSAGE_TO_ENCRYPT, 17, 20)
decrypted_messages = hacker.brute_force(encrypted_message, p=0.95)
print('\n'.join(decrypted_messages))
