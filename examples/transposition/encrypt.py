"""Example of message encryption using the Simple Transposition cipher"""

from ciphers.transposition import SimpleTranspositionCipher

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
KEY = 10

cipher = SimpleTranspositionCipher()

encrypted_message = cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(encrypted_message)
