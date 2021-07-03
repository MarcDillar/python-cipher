"""Example of message decryption using the Caesar cipher"""

from ciphers.caesar import CaesarCipher

MESSAGE_TO_DECRYPT = "$rsC4sC4Dro4woCCkqo4DrkD4GkC4oxmBIzDon"
KEY = 10

caesar_cipher = CaesarCipher()

decrypted_message = caesar_cipher.decrypt(message=MESSAGE_TO_DECRYPT, key=KEY)
print(decrypted_message)
