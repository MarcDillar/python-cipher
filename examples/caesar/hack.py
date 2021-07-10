"""Example of message encryption using the Caesar cipher"""

from ciphers.caesar import CaesarCipher
from hackers.caesar import CaesarCipherHacker

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
KEY = 10

caesar_cipher = CaesarCipher()
caesar_hacker = CaesarCipherHacker()

encrypted_message = caesar_cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
decrypted_messages = caesar_hacker.brute_force(encrypted_message, p=0.95)
print('\n'.join(decrypted_messages))