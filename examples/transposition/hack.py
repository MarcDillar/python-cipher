"""Example of message encryption using the Caesar cipher"""

from simple_ciphers.ciphers.transposition import SimpleTranspositionCipher
from simple_ciphers.hackers.transposition import SimpleTranspositionCipherHacker

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted. For instance, adding another sentence makes it harder to uncipher"
KEY = 20

simple_transposition_cipher = SimpleTranspositionCipher()
simple_transposition_hacker = SimpleTranspositionCipherHacker()

encrypted_message = simple_transposition_cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
decrypted_messages = simple_transposition_hacker.brute_force(encrypted_message, p=0.999)
print('\n'.join(decrypted_messages))
