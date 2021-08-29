"""Example of message decryption using the Caesar cipher"""

from simple_ciphers.ciphers.caesar import CaesarCipher

KEY = 10

# Cipher using simple mode
message_to_decrypt = "Drsc sc dro wocckqo drkd gsvv lo oxmbizdon"
caesar_cipher = CaesarCipher()

decrypted_message = caesar_cipher.decrypt(message=message_to_decrypt, key=KEY)
print(decrypted_message)

# Cipher using all ASCII Printable characters
message_to_decrypt = "$rsC4sC4Dro4woCCkqo4DrkD4Gsvv4lo4oxmBIzDon"
caesar_cipher = CaesarCipher(simple=False)

decrypted_message = caesar_cipher.decrypt(message=message_to_decrypt, key=KEY)
print(decrypted_message)
