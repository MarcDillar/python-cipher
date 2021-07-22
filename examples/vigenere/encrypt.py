"""Examples of message encryption using the Vigenere cipher"""

from simple_ciphers.ciphers.vigenere import VigenereCipher

message = "Here is the message that will be encrypted."
key = "This is my key"

"""
Encryption using the simple mode
The simple mode preserves the characters' case 
and only encrypts letters
"""
simple_cipher = VigenereCipher(simple=True)
encrypted_message = simple_cipher.encrypt(message, key)
print(encrypted_message)

"""
Encryption using the default mode
"""
cipher = VigenereCipher()
encrypted_message = cipher.encrypt(message, key)
print(encrypted_message)
