"""Examples of message encryption using the Affine cipher"""

from simple_ciphers.ciphers.affine import AffineCipher

MESSAGE_TO_ENCRYPT = "This is the message that will be encrypted"
KEY_A = 7
KEY_B = 47

# Cipher using simple mode
cipher = AffineCipher()
encrypted_text = cipher.encrypt(MESSAGE_TO_ENCRYPT, KEY_A, KEY_B)

print(encrypted_text)

# Cipher using all ASCII Printable characters
cipher = AffineCipher(simple=False)
encrypted_text = cipher.encrypt(MESSAGE_TO_ENCRYPT, KEY_A, KEY_B)

print(encrypted_text)
