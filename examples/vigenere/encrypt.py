"""Examples of message encryption using the Vigenere cipher"""

from simple_ciphers.ciphers.vigenere import VigenereCipher

message = "Here is the message that will be encrypted."
key = "This is my key"

# Cipher using simple mode
simple_cipher = VigenereCipher()
encrypted_message = simple_cipher.encrypt(message, key)
print(encrypted_message)

# Cipher using all ASCII Printable characters
cipher = VigenereCipher(simple=False)
encrypted_message = cipher.encrypt(message, key)
print(encrypted_message)

# Cipher using a different character set
cipher = VigenereCipher(
    simple=False,
    symbols="AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn "
    )
encrypted_message = cipher.encrypt(message, key)
print(encrypted_message)
