"""Example of message encryption using the Caesar cipher"""

from simple_ciphers.ciphers.caesar import CaesarCipher

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
KEY = 10

caesar_cipher = CaesarCipher()

encrypted_message = caesar_cipher.encrypt(message=MESSAGE_TO_ENCRYPT, key=KEY)
print(encrypted_message)
